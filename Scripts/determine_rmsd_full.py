#!/usr/bin/env python3

import sys
import numpy as np
import MDAnalysis as mda
from MDAnalysis.analysis import align, rms


# ==========================================================
# Chemically equivalent atom mappings
# ==========================================================

EQUIVALENT_ATOMS = {
    "ASP": [("OD1", "OD2")],
    "GLU": [("OE1", "OE2")],
    "PHE": [("CD1", "CD2"), ("CE1", "CE2")],
    "TYR": [("CD1", "CD2"), ("CE1", "CE2")],
    "ARG": [("NH1", "NH2")],
    "LEU": [("CD1", "CD2")],
    "VAL": [("CG1", "CG2")]
}


def get_atom_positions(atomgroup):
    """
    Return dictionary:
    {(resid, resname, atomname): position}
    """

    atom_dict = {}

    for atom in atomgroup:
        key = (atom.resid, atom.resname, atom.name)
        atom_dict[key] = atom.position.copy()

    return atom_dict


def apply_equivalent_atom_swaps(ref_dict, target_dict):
    """
    Swap chemically equivalent atoms in target structure
    if doing so lowers RMSD.
    """

    for resname, pairs in EQUIVALENT_ATOMS.items():

        resids = set(
            resid for resid, rname, aname in target_dict.keys()
            if rname == resname
        )

        for resid in resids:

            for atom1, atom2 in pairs:

                key1 = (resid, resname, atom1)
                key2 = (resid, resname, atom2)

                if (
                    key1 in target_dict and
                    key2 in target_dict and
                    key1 in ref_dict and
                    key2 in ref_dict
                ):

                    # Current assignment
                    d_current = (
                        np.sum((target_dict[key1] - ref_dict[key1])**2) +
                        np.sum((target_dict[key2] - ref_dict[key2])**2)
                    )

                    # Swapped assignment
                    d_swapped = (
                        np.sum((target_dict[key1] - ref_dict[key2])**2) +
                        np.sum((target_dict[key2] - ref_dict[key1])**2)
                    )

                    if d_swapped < d_current:
                        tmp = target_dict[key1].copy()
                        target_dict[key1] = target_dict[key2]
                        target_dict[key2] = tmp

    return target_dict


def calculate_residue_rmsd(ref_dict, target_dict):

    residue_data = {}

    for key in ref_dict:

        if key not in target_dict:
            continue

        resid, resname, atomname = key

        if resid not in residue_data:
            residue_data[resid] = {
                "resname": resname,
                "ref": [],
                "target": []
            }

        residue_data[resid]["ref"].append(ref_dict[key])
        residue_data[resid]["target"].append(target_dict[key])

    residue_rmsd = {}

    for resid in sorted(residue_data.keys()):

        ref_coords = np.array(residue_data[resid]["ref"])
        target_coords = np.array(residue_data[resid]["target"])

        rmsd_value = rms.rmsd(
            target_coords,
            ref_coords,
            center=False,
            superposition=False
        )

        residue_rmsd[resid] = (
            residue_data[resid]["resname"],
            rmsd_value
        )

    return residue_rmsd


def main():

    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} reference.pdb target.pdb")
        sys.exit(1)

    ref_pdb = sys.argv[1]
    target_pdb = sys.argv[2]

    # =========================
    # LOAD STRUCTURES
    # =========================

    u_ref = mda.Universe(ref_pdb)
    u_target = mda.Universe(target_pdb)

    # =========================
    # ALIGN USING CA ATOMS
    # =========================

    target_ca = u_target.select_atoms("protein and name CA")

    if len(target_ca) == 0:
        raise ValueError("No protein CA atoms found in target structure.")

    target_resids = target_ca.resids
    resid_string = " ".join(map(str, target_resids))

    ref_ca = u_ref.select_atoms(
        f"protein and name CA and resid {resid_string}"
    )

    if len(ref_ca) != len(target_ca):
        raise ValueError(
            f"Mismatch in CA atom counts:\n"
            f"Reference: {len(ref_ca)}\n"
            f"Target: {len(target_ca)}"
        )

    # Align target to reference
    align.alignto(
        u_target,
        u_ref,
        select=f"protein and name CA and resid {resid_string}"
    )

    # ==========================================
    # SELECT SIDECHAIN HEAVY ATOMS
    # ==========================================

    target_sidechain = u_target.select_atoms(
        "protein and not backbone and not name H*"
    )

    target_indices = []
    ref_indices = []

    # Match atoms by residue ID + atom name
    for atom in target_sidechain:

        resid = atom.resid
        atom_name = atom.name

        ref_match = u_ref.select_atoms(
            f"protein and resid {resid} and name {atom_name}"
        )

        if len(ref_match) == 1:
            target_indices.append(atom.index)
            ref_indices.append(ref_match[0].index)

    target_atoms = u_target.atoms[target_indices]
    ref_atoms = u_ref.atoms[ref_indices]

    if len(target_atoms) == 0:
        raise ValueError("No matching sidechain heavy atoms found.")

    print(f"Matched sidechain heavy atoms: {len(target_atoms)}")

    # ==========================================
    # HANDLE CHEMICALLY EQUIVALENT ATOMS
    # ==========================================

    ref_dict = get_atom_positions(ref_atoms)
    target_dict = get_atom_positions(target_atoms)

    target_dict = apply_equivalent_atom_swaps(
        ref_dict,
        target_dict
    )

    # ==========================================
    # BUILD GLOBAL COORDINATE ARRAYS
    # ==========================================

    ref_coords = []
    target_coords = []

    for key in sorted(ref_dict.keys()):

        if key in target_dict:
            ref_coords.append(ref_dict[key])
            target_coords.append(target_dict[key])

    ref_coords = np.array(ref_coords)
    target_coords = np.array(target_coords)

    # =========================
    # GLOBAL RMSD
    # =========================

    global_rmsd = rms.rmsd(
        target_coords,
        ref_coords,
        center=False,
        superposition=False
    )

    print(f"\nGlobal sidechain heavy-atom RMSD: {global_rmsd:.3f} Å")

    # =========================
    # PER-RESIDUE RMSD
    # =========================

    residue_rmsd = calculate_residue_rmsd(
        ref_dict,
        target_dict
    )

    print("\nPer-residue sidechain heavy-atom RMSD:")
    print("Resid\tResname\tRMSD (Å)")

    for resid in sorted(residue_rmsd.keys()):

        resname, rmsd_value = residue_rmsd[resid]

        print(f"{resid}\t{resname}\t{rmsd_value:.3f}")


if __name__ == "__main__":
    main()
