import numpy as np
import argparse
import MDAnalysis as mda

"""
Usage: python calculate_bond_efield_gaussian.py --log_file [file] --pdb_file --atom1_sel [idx] --atom2_sel [idx]
"""

ef_from_au = 5.14220674763e11 # 1 V/m = 1 a.u.
conv = ef_from_au*1e-6/100 # to MV/cm

parser = argparse.ArgumentParser(description='Process EF at two atoms from gaussian prop=efg calculation. Typically atom1 is chosen to be the less electronegative atom.')
parser.add_argument('--log_file', type=str, help="Path to Gaussian log file.")
parser.add_argument('--pdb_file', type=str, help="Path to corresponding PDB file (atom order must be the same!).", default='')
parser.add_argument('--atom1_sel', type=str, help="Atom MDAnalysis selection command.", default='resname 6VW and name C1')
parser.add_argument('--atom2_sel', type=str, help="Atom MDAnalysis selection command.", default='resname 6VW and name O1')
parser.add_argument('--atom1_idx', type=int, help="Index of atom 1 (indices start from 0).", default=0)
parser.add_argument('--atom2_idx', type=int, help="Index of atom 2 (indices start from 0).", default=1)

args = parser.parse_args()

log_file = args.log_file
pdb_file = args.pdb_file
atom1_sel = args.atom1_sel
atom2_sel = args.atom2_sel
atom1_idx = args.atom1_idx
atom2_idx = args.atom2_idx

# useful functions
def get_index(pdb_file, atom_selection):
    u = mda.Universe(pdb_file)
    sel = u.select_atoms(atom_selection)
    return u.select_atoms(atom_selection).indices[0]

def get_electric_field(log_file, atom1_id, atom2_id):
    '''
    To calculate the electric field from a Gaussian prop=efg calculation.

    Notes
    ----- 
    - Atom order will alter sign of electric field. Typical to define atom1 as the less electronegative atom, 
    such that the bond vector will be in the direction of the bond dipole.

    Parameters
    ----------
    log_file : str, required
        Path to Gaussian log file.
    atom1_id : int, required
        0 indexed id for starting atom.
    atom2_id : int, required
        0 indexed id for ending atom.
    
    Returns
    -------
    ef1, ef2 : float
        scalar electric field magnitudes at atom 1 and atom 2
    unit_vec : array
        unit vector along the direction of the atom 1 and atom 2 bond dipole.
    '''
    with open(log_file) as f:
        data = f.readlines()
    center_start = None
    ef_start = None

    for i, line in enumerate(data):
        #if center_start == None:
        #    if 'Atomic Center' in line:
        #        center_start = i
        if 'Electrostatic Properties Using The SCF Density' in line:
            center_start = i+4
        if '-------- Electric Field --------' in line:
            ef_start = i+3
            #break #removing break because if you also do opt then the 
            #  EF is save to the file twice!! We want the optimized EF 
            #  so save on the second encounter.

    
    print(f"EF Start Line: {ef_start}")    
    coords1 = np.array([float(x) for x in data[center_start+atom1_id].split()[-3:]])
    coords2 = np.array([float(x) for x in data[center_start+atom2_id].split()[-3:]])
    
    print(f"Atom1 coords: {coords1}")
    print(f"Atom2 coords: {coords2}")
    
    unit_vec =  unit_vector(coords1,coords2)

    ef1 = np.array([float(x) for x in data[ef_start+atom1_id].split()[-3:]])
    ef2 = np.array([float(x) for x in data[ef_start+atom2_id].split()[-3:]])
    print(f"Atom 1 EF tensor: {ef1}")
    print(f"Atom 2 EF tensor: {ef2}")

    return ef1, ef2, unit_vec


def electric_field_avg(ef1, ef2, unit_vec):
    '''
    Returns
    -------
    Scalar electric field value in units MV/cm averaged over the electric 
    field magnitude at atom1 and atom2.
    '''
    #return (0.5*(np.dot(ef1, unit_vec)+np.dot(ef2, unit_vec)))*conv # in units MV/cm
    return (0.5*(np.dot(ef1, unit_vec)+np.dot(ef2, unit_vec)))*conv # in units MV/cm


def electric_field_drop(ef1, ef2, unit_vec):
    '''
    Returns
    -------
    Scalar electric field value in units MV/cm taken as the difference in 
    electric field magnitude at atom1 and atom2.
    '''
    return (np.dot(ef1, unit_vec)-np.dot(ef2, unit_vec))*conv # in units MV/cm

def unit_vector(coords_start, coords_end):
    '''
    To calculate the normalized vector between two points in cartesian space.

    Parameters
    ----------
    coords_start : array or list of floats, required
        Starting point coordinates
    coords_end : array or list of floats, required
        Ending point coordinates

    Returns 
    -------
    unit vector array
    '''
    if type(coords_start) is list:
        coords_start = np.array(coords_start)
    if type(coords_end) is list:
        coords_end = np.array(coords_end)
    bond_length = np.linalg.norm(coords_end-coords_start)
    bond_vec = coords_end-coords_start
    return bond_vec/bond_length

if pdb_file != '':
    atom1_idx = get_index(pdb_file, atom1_sel)
    atom2_idx = get_index(pdb_file, atom2_sel)
print(f"Processing electric field from file {log_file} on atoms {atom1_idx} and {atom2_idx}.")
ef1, ef2, unit_vec = get_electric_field(log_file, atom1_idx, atom2_idx)
ef_avg = electric_field_avg(ef1, ef2, unit_vec)
print(f"Electric field at atom {atom1_idx}: {ef1} MV/cm")
print(f"Electric field at atom {atom2_idx}: {ef2} MV/cm")
print(f"Electric field bond average: {ef_avg} MV/cm")
print("Do not forget to subtract ligand self-field.")
print("---------------------------------------------------")

