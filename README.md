# Title 
QMzyme: Automated and Systematic QM-based Enzyme Model Construction

# Contents
This repository contains all the data files that were used for geometry optimizations, electric field calculations and model generation , including final optimized structures. It also contains the scripts used to parse the electric field data, to determine RMSD and to plot them. All the raw data is also present in an excel sheet.

# Data structure

QMzyme-Data-Repository/
├── 19nt_gaussian_efg_calculations
│   ├── mm_minimized_starting_structure
│   └── xstal_starting_structure
├── 19nt_optimizations
│   ├── mm_minimized_starting_structure
│   └── xstal_starting_structure
├── 19nt_qchem_spade_ef_calculations
│   ├── mm_min_starting_structures
│   └── xstal_starting_structure
├── MD Simulations
│   ├── EQU_parameterizatin
│   ├── TUPA Data
│   └── tleap.in
├── README.md
├── Scripts
│   ├── determine_rmsd_for_specific_residues.py
│   ├── determine_rmsd_full.py
│   ├── gaussian_elecfield_parse.py
│   ├── plot_elecfield.py
│   ├── plot_rmsd.py
│   └── qchem_elecfield_parse.py
├── cluster_model_generation
│   ├── 19nt_ligand_from_5kp4.pdb
│   ├── 1oh0_19nt_crystal_distance_cutoff3_dft.csv
│   ├── 1oh0_19nt_crystal_distance_cutoff3_dft.pdb
│   ├── 1oh0_19nt_crystal_distance_cutoff3_dft.pkl
│   ├── 1oh0_19nt_crystal_distance_cutoff3_dft.png
│   ├── 1oh0_19nt_crystal_distance_cutoff3_xtb.csv
│   ├── 1oh0_19nt_crystal_distance_cutoff3_xtb.pdb
│   ├── 1oh0_19nt_crystal_distance_cutoff3_xtb.pkl
│   ├── 1oh0_19nt_crystal_distance_cutoff3_xtb.png
│   ├── 1oh0_19nt_crystal_distance_cutoff4_dft.csv
│   ├── 1oh0_19nt_crystal_distance_cutoff4_dft.pdb
│   ├── 1oh0_19nt_crystal_distance_cutoff4_dft.pkl
│   ├── 1oh0_19nt_crystal_distance_cutoff4_dft.png
│   ├── 1oh0_19nt_crystal_distance_cutoff4_xtb.csv
│   ├── 1oh0_19nt_crystal_distance_cutoff4_xtb.pdb
│   ├── 1oh0_19nt_crystal_distance_cutoff4_xtb.pkl
│   ├── 1oh0_19nt_crystal_distance_cutoff4_xtb.png
│   ├── 1oh0_19nt_crystal_distance_cutoff5_dft.csv
│   ├── 1oh0_19nt_crystal_distance_cutoff5_dft.pdb
│   ├── 1oh0_19nt_crystal_distance_cutoff5_dft.pkl
│   ├── 1oh0_19nt_crystal_distance_cutoff5_dft.png
│   ├── 1oh0_19nt_crystal_distance_cutoff5_xtb.csv
│   ├── 1oh0_19nt_crystal_distance_cutoff5_xtb.pdb
│   ├── 1oh0_19nt_crystal_distance_cutoff5_xtb.pkl
│   ├── 1oh0_19nt_crystal_distance_cutoff5_xtb.png
│   ├── 1oh0_19nt_crystal_distance_cutoff6_dft.csv
│   ├── 1oh0_19nt_crystal_distance_cutoff6_dft.pdb
│   ├── 1oh0_19nt_crystal_distance_cutoff6_dft.pkl
│   ├── 1oh0_19nt_crystal_distance_cutoff6_dft.png
│   ├── 1oh0_19nt_crystal_distance_cutoff6_xtb.csv
│   ├── 1oh0_19nt_crystal_distance_cutoff6_xtb.pdb
│   ├── 1oh0_19nt_crystal_distance_cutoff6_xtb.pkl
│   ├── 1oh0_19nt_crystal_distance_cutoff6_xtb.png
│   ├── 1oh0_19nt_crystal_distance_cutoff7_dft.csv
│   ├── 1oh0_19nt_crystal_distance_cutoff7_dft.pdb
│   ├── 1oh0_19nt_crystal_distance_cutoff7_dft.pkl
│   ├── 1oh0_19nt_crystal_distance_cutoff7_dft.png
│   ├── 1oh0_19nt_crystal_distance_cutoff7_xtb.csv
│   ├── 1oh0_19nt_crystal_distance_cutoff7_xtb.pdb
│   ├── 1oh0_19nt_crystal_distance_cutoff7_xtb.pkl
│   ├── 1oh0_19nt_crystal_distance_cutoff7_xtb.png
│   ├── 1oh0_19nt_crystal_distance_cutoff8_dft.csv
│   ├── 1oh0_19nt_crystal_distance_cutoff8_dft.pdb
│   ├── 1oh0_19nt_crystal_distance_cutoff8_dft.pkl
│   ├── 1oh0_19nt_crystal_distance_cutoff8_dft.png
│   ├── 1oh0_19nt_crystal_distance_cutoff8_xtb.csv
│   ├── 1oh0_19nt_crystal_distance_cutoff8_xtb.pdb
│   ├── 1oh0_19nt_crystal_distance_cutoff8_xtb.pkl
│   ├── 1oh0_19nt_crystal_distance_cutoff8_xtb.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_dft.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_dft.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_dft.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_dft.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_no_wat_dft.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_no_wat_dft.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_no_wat_dft_v2.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_no_wat_dft_v2.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_no_wat_xtb.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_no_wat_xtb.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_no_wat_xtb_v2.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_no_wat_xtb_v2.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_xtb.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_xtb.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_xtb.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_xtb.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_dft.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_dft.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_dft.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_dft.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_no_wat_dft.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_no_wat_dft.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_no_wat_dft_v2.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_no_wat_dft_v2.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_no_wat_xtb.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_no_wat_xtb.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_no_wat_xtb_v2.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_no_wat_xtb_v2.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_xtb.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_xtb.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_xtb.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_xtb.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_dft.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_dft.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_dft.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_dft.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_no_wat_dft.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_no_wat_dft.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_no_wat_dft_v2.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_no_wat_dft_v2.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_no_wat_xtb.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_no_wat_xtb.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_no_wat_xtb_v2.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_no_wat_xtb_v2.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_xtb.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_xtb.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_xtb.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_xtb.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_dft.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_dft.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_dft.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_dft.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_no_wat_dft.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_no_wat_dft.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_no_wat_dft_v2.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_no_wat_dft_v2.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_no_wat_xtb.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_no_wat_xtb.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_no_wat_xtb_v2.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_no_wat_xtb_v2.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_xtb.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_xtb.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_xtb.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_xtb.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_dft.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_dft.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_dft.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_dft.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_no_wat_dft.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_no_wat_dft.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_no_wat_dft_v2.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_no_wat_dft_v2.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_no_wat_xtb.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_no_wat_xtb.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_no_wat_xtb_v2.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_no_wat_xtb_v2.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_xtb.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_xtb.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_xtb.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_xtb.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff8_dft.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff8_dft.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff8_dft.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff8_dft.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff8_no_wat_dft.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff8_no_wat_dft.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff8_no_wat_dft_v2.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff8_no_wat_dft_v2.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff8_no_wat_xtb.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff8_no_wat_xtb.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff8_no_wat_xtb_v2.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff8_no_wat_xtb_v2.png
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff8_xtb.csv
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff8_xtb.pdb
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff8_xtb.pkl
│   ├── 1oh0_19nt_mm_minimized_distance_cutoff8_xtb.png
│   ├── 1oh0_equ_crystal.pdb
│   ├── 1oh0_equ_mm_minimized.pdb
│   ├── QCALC
│   ├── add_Hs.in
│   ├── ksi_19nt_model_generation.out
│   └── ksi_19nt_model_generation.py
└── ksi_composed_data_qmzyme.xlsx
