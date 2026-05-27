#! /usr/bin/env python

import os, glob, sys, re, math
import argparse
import cclib
import numpy as np
import pandas as pd

"""
Usage: python calculate_bond_efield.py --qchem_file [file] --atom1_idx [idx] --atom2_idx [idx]
"""

parser = argparse.ArgumentParser(description='Process EF at two atoms. Typically atom1 is chosen to be the less electronegative atom.')
parser.add_argument('--qchem_file', type=str, help="Full path to Q-Chem output file.")
parser.add_argument('--atom1_idx', type=int, help="Index of atom 1 (indices start from 0).")
parser.add_argument('--atom2_idx', type=int, help="Index of atom 2 (indices start from 0).")

args = parser.parse_args()
file = args.qchem_file
atom1_idx = args.atom1_idx
atom2_idx = args.atom2_idx

au_to_MV_cm = 5.14220675112e3  

def calc_unit_vector(coords, atom1_idx, atom2_idx):
    unit_vec = coords[atom2_idx] - coords[atom1_idx]
    unit_vec /= np.linalg.norm(unit_vec) 
    return unit_vec

def parse_efield(file):
    start_parsing = False
    efield = np.array([])
    efield_temp = None
    with open(file, 'r') as f:
        for line in f.readlines():
            l = line.split()
            if len(l) == 1 and l[0] == 'EField':
                start_parsing = True
                counter = 0
                continue
            if len(l) > 2 and l[1] == 'DONE':
                np.savetxt(file.split(".out")[0]+".efield", efield, fmt="%.7f")
                break
            if start_parsing:
                if counter == 0:
                    begin = int(l[0])
                    end = int(l[-1])
                    n = end-begin+1
                    efield_tmp = np.zeros((n,3))
                    counter +=1
                else:
                    for idx in range(n):
                        efield_tmp[idx][counter-1] = float(l[idx+1])
                    if counter == 3:
                        if len(efield) == 0:
                            efield = efield_tmp
                        else:
                            efield = np.vstack((efield, efield_tmp))
                        counter = 0
                    else:
                        counter += 1
    return efield

#print(f"Processing electric field from file {file} on atoms {atom1_idx} and {atom2_idx}.")
data = cclib.io.ccread(file)
coords = data.atomcoords[-1]
efield = parse_efield(file)
ef1_xyz = efield[atom1_idx]
ef2_xyz = efield[atom2_idx]
unit_vector = calc_unit_vector(coords, atom1_idx, atom2_idx)
ef1 = np.dot(ef1_xyz*au_to_MV_cm, unit_vector)
ef2 = np.dot(ef2_xyz*au_to_MV_cm, unit_vector)
ef_bond_avg = 0.5*(ef1+ef2)
print(f"Electric field at atom {atom1_idx}: {ef1} MV/cm")
print(f"Electric field at atom {atom2_idx}: {ef2} MV/cm")
print(f"Electric field bond average: {ef_bond_avg} MV/cm")
print("---------------------------------------------------")