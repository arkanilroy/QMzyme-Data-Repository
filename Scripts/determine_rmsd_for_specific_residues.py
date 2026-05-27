#!/usr/bin/env python3

import sys
import numpy as np
import MDAnalysis as mda
from MDAnalysis.analysis import align
from MDAnalysis.analysis.rms import rmsd

# ============================================================
# Symmetric atom groups
# Handles aromatic/resonance equivalent atom swapping
# ============================================================

SYMMETRIC_GROUPS = {
    "PHE": [("CD1", "CD2"), ("CE1", "CE2")],
    "TYR": [("CD1", "CD2"), ("CE1", "CE2")],
    "ASP": [("OD1", "OD2")],
    "ASH": [("OD1", "OD2")],
    "GLU": [("OE1", "OE2")],
    "GLH": [("OE1", "OE2")],
    "ARG": [("NH1", "NH2")],
}


# ============================================================
# Convert AtomGroup -> dict(atom_name : coordinates)
# ============================================================

def get_atom_dict(atomgroup):

    return {
        atom.name: atom.position.copy()
        for atom in atomgroup
    }


# ============================================================
# Build properly ordered coordinate arrays
# while handling symmetric atom swaps
# ============================================================

def build_ordered_positions(ref_res, target_res, resname):

    ref_dict = get_atom_dict(ref_res)
    target_dict = get_atom_dict(target_res)

    common_atoms = sorted(
        set(ref_dict.keys()).intersection(
            set(target_dict.keys())
        )
    )

    if len(common_atoms) == 0:
        return None, None, None

    # Default atom mapping
    mapping = {a: a for a in common_atoms}

    # Handle symmetry-aware swaps
    if resname in SYMMETRIC_GROUPS:

        for a1, a2 in SYMMETRIC_GROUPS[resname]:

            if a1 in common_atoms and a2 in common_atoms:

                # Direct assignment
                direct = (
                    np.linalg.norm(
                        ref_dict[a1] - target_dict[a1]
                    )**2
                    +
                    np.linalg.norm(
                        ref_dict[a2] - target_dict[a2]
                    )**2
                )

                # Swapped assignment
                swapped = (
                    np.linalg.norm(
                        ref_dict[a1] - target_dict[a2]
                    )**2
                    +
                    np.linalg.norm(
                        ref_dict[a2] - target_dict[a1]
                    )**2
                )

                if swapped < direct:
                    mapping[a1] = a2
                    mapping[a2] = a1

    ref_positions = []
    target_positions = []
    used_atoms = []

    for atom_name in common_atoms:

        mapped_name = mapping[atom_name]

        ref_positions.append(ref_dict[atom_name])
        target_positions.append(target_dict[mapped_name])

        used_atoms.append(
            f"{atom_name}->{mapped_name}"
        )

    return (
        np.array(ref_positions),
        np.array(target_positions),
        used_atoms
    )


# ============================================================
# Main RMSD routine
# ============================================================

def calculate_residue_rmsd(
        ref_pdb,
        target_pdb,
        residue_ids,
        output_aligned_pdb):

    u_ref = mda.Universe(ref_pdb)
    u_target = mda.Universe(target_pdb)

    # ========================================================
    # ROBUST GLOBAL ALIGNMENT
    # ========================================================

    align_sel = "protein and name CA"

    old_rmsd, new_rmsd = align.alignto(
        u_target,
        u_ref,
        select=align_sel
    )

    print("\nGlobal alignment RMSD")
    print("----------------------------------------------")
    print(f"Before alignment : {old_rmsd:.4f} Å")
    print(f"After alignment  : {new_rmsd:.4f} Å")

    # ========================================================
    # Write aligned structure
    # ========================================================

    u_target.atoms.write(output_aligned_pdb)

    print(f"\nAligned structure written to:")
    print(output_aligned_pdb)

    # ========================================================
    # Per-residue RMSD
    # ========================================================

    print("\nPer-residue sidechain RMSD")
    print("--------------------------------------------------")

    total_ref = []
    total_target = []

    for resid in residue_ids:

        # Heavy-atom sidechain only
        ref_res = u_ref.select_atoms(
            f"protein and resid {resid} "
            f"and not backbone and not name H*"
        )

        target_res = u_target.select_atoms(
            f"protein and resid {resid} "
            f"and not backbone and not name H*"
        )

        if len(ref_res) == 0 or len(target_res) == 0:

            print(f"Residue {resid}: NOT FOUND")
            continue

        resname = ref_res.residues[0].resname

        ref_pos, target_pos, used_atoms = (
            build_ordered_positions(
                ref_res,
                target_res,
                resname
            )
        )

        if ref_pos is None:

            print(f"Residue {resid}: No common atoms")
            continue

        value = rmsd(
            target_pos,
            ref_pos,
            center=False,
            superposition=False
        )

        print(
            f"Residue {resid:4d} "
            f"({resname}): "
            f"{value:.4f} Å   "
            f"(atoms used: {len(ref_pos)})"
        )

        # Uncomment for debugging atom mappings
        # print("   ", used_atoms)

        total_ref.append(ref_pos)
        total_target.append(target_pos)

    # ========================================================
    # Total RMSD
    # ========================================================

    if len(total_ref) > 0:

        total_ref = np.vstack(total_ref)
        total_target = np.vstack(total_target)

        total_rmsd = rmsd(
            total_target,
            total_ref,
            center=False,
            superposition=False
        )

        print("\nTotal RMSD over selected residues")
        print("--------------------------------------------------")
        print(f"{total_rmsd:.4f} Å")

    else:

        print("\nNo atoms available for total RMSD")


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":

    if len(sys.argv) < 5:

        print("\nUsage:")
        print(
            "python get_rmsd.py "
            "reference.pdb target.pdb "
            "aligned_output.pdb "
            "16 40 103"
        )

        sys.exit(1)

    ref_pdb = sys.argv[1]
    target_pdb = sys.argv[2]
    output_pdb = sys.argv[3]

    residue_ids = [
        int(r)
        for r in sys.argv[4:]
    ]

    calculate_residue_rmsd(
        ref_pdb,
        target_pdb,
        residue_ids,
        output_pdb
    )
