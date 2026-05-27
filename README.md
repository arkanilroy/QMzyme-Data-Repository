# Title 
QMzyme: Automated and Systematic QM-based Enzyme Model Construction

# Contents
This repository contains all the data files that were used for geometry optimizations, electric field calculations and model generation , including final optimized structures. It also contains the scripts used to parse the electric field data, to determine RMSD and to plot them. All the raw data is also present in an excel sheet.

QMzyme-Data-Repository/
├── 19nt_gaussian_efg_calculations
│   ├── mm_minimized_starting_structure
│   │   ├── 19nt_mm_min_distance_cutoff3_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff3_from_cutoff6_nowat_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff3_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff3_nowat_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff3_nowat_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff3_nowat_xtb_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff3_nowat_xtb_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff3_xtb_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff3_xtb_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff4_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff4_from_cutoff6_nowat_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff4_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff4_nowat_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff4_nowat_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff4_nowat_xtb_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff4_nowat_xtb_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff4_xtb_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff4_xtb_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff5_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff5_from_cutoff6_nowat_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff5_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff5_nowat_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff5_nowat_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff5_nowat_xtb_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff5_nowat_xtb_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff5_xtb_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff5_xtb_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff6_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff6_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff6_nowat_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff6_nowat_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff6_nowat_xtb_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff6_nowat_xtb_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff6_xtb_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff6_xtb_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff7_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff7_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff7_nowat_optimized_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff7_nowat_optimized_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff7_nowat_xtb_optimized_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff7_nowat_xtb_optimized_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff7_xtb_optimized_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff7_xtb_optimized_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff8_nowat_optimized_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff8_nowat_optimized_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff8_nowat_xtb_optimized_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff8_nowat_xtb_optimized_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff8_optimized_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff8_optimized_ligand.log
│   │   ├── 19nt_mm_min_distance_cutoff8_xtb_optimized_efg.log
│   │   ├── 19nt_mm_min_distance_cutoff8_xtb_optimized_ligand.log
│   │   └── README.md
│   └── xstal_starting_structure
│       ├── 19nt_xstal_distance_cutoff3_efg.log
│       ├── 19nt_xstal_distance_cutoff3_ligand.log
│       ├── 19nt_xstal_distance_cutoff3_xtb_efg.log
│       ├── 19nt_xstal_distance_cutoff3_xtb_ligand.log
│       ├── 19nt_xstal_distance_cutoff4_efg.log
│       ├── 19nt_xstal_distance_cutoff4_ligand.log
│       ├── 19nt_xstal_distance_cutoff4_xtb_efg.log
│       ├── 19nt_xstal_distance_cutoff4_xtb_ligand.log
│       ├── 19nt_xstal_distance_cutoff5_efg.log
│       ├── 19nt_xstal_distance_cutoff5_ligand.log
│       ├── 19nt_xstal_distance_cutoff5_xtb_efg.log
│       ├── 19nt_xstal_distance_cutoff5_xtb_ligand.log
│       ├── 19nt_xstal_distance_cutoff6_efg.log
│       ├── 19nt_xstal_distance_cutoff6_ligand.log
│       ├── 19nt_xstal_distance_cutoff6_xtb_efg.log
│       ├── 19nt_xstal_distance_cutoff6_xtb_ligand.log
│       ├── 19nt_xstal_distance_cutoff7_efg.log
│       ├── 19nt_xstal_distance_cutoff7_ligand.log
│       ├── 19nt_xstal_distance_cutoff7_xtb_efg.log
│       ├── 19nt_xstal_distance_cutoff7_xtb_ligand.log
│       ├── 19nt_xstal_distance_cutoff8_efg.log
│       ├── 19nt_xstal_distance_cutoff8_ligand.log
│       ├── 19nt_xstal_distance_cutoff8_xtb_efg.log
│       ├── 19nt_xstal_distance_cutoff8_xtb_ligand.log
│       └── README.md
├── 19nt_optimizations
│   ├── mm_minimized_starting_structure
│   │   ├── 19nt_mm_min_distance_cutoff3_from_cutoff6_nowat_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff3_nowat_optimized.log
│   │   ├── 19nt_mm_min_distance_cutoff3_nowat_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff3_nowat_xtb_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff3_optimized.log
│   │   ├── 19nt_mm_min_distance_cutoff3_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff3_xtb_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff4_from_cutoff6_nowat_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff4_nowat_optimized.log
│   │   ├── 19nt_mm_min_distance_cutoff4_nowat_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff4_nowat_xtb_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff4_optimized.log
│   │   ├── 19nt_mm_min_distance_cutoff4_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff4_xtb_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff5_from_cutoff6_nowat_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff5_nowat_optimized.log
│   │   ├── 19nt_mm_min_distance_cutoff5_nowat_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff5_nowat_xtb_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff5_optimized.log
│   │   ├── 19nt_mm_min_distance_cutoff5_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff5_xtb_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff6_nowat_optimized.log
│   │   ├── 19nt_mm_min_distance_cutoff6_nowat_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff6_nowat_xtb_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff6_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff6_xtb_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff7_nowat_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff7_nowat_xtb_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff7_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff7_xtb_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff8_nowat_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff8_nowat_xtb_optimized.pdb
│   │   ├── 19nt_mm_min_distance_cutoff8_optimized.pdb
│   │   └── 19nt_mm_min_distance_cutoff8_xtb_optimized.pdb
│   └── xstal_starting_structure
│       ├── 19nt_xstal_distance_cutoff3_optimized.pdb
│       ├── 19nt_xstal_distance_cutoff3_xtb_optimized.pdb
│       ├── 19nt_xstal_distance_cutoff4_optimized.log
│       ├── 19nt_xstal_distance_cutoff4_optimized.pdb
│       ├── 19nt_xstal_distance_cutoff4_xtb_optimized.pdb
│       ├── 19nt_xstal_distance_cutoff5_optimized.log
│       ├── 19nt_xstal_distance_cutoff5_optimized.pdb
│       ├── 19nt_xstal_distance_cutoff5_xtb_optimized.pdb
│       ├── 19nt_xstal_distance_cutoff6_optimized.pdb
│       ├── 19nt_xstal_distance_cutoff6_xtb_optimized.pdb
│       ├── 19nt_xstal_distance_cutoff7_optimized.pdb
│       ├── 19nt_xstal_distance_cutoff7_xtb_optimized.pdb
│       ├── 19nt_xstal_distance_cutoff8_optimized.pdb
│       ├── 19nt_xstal_distance_cutoff8_xtb_optimized.pdb
│       └── aligned_optimized_structures.pse
├── 19nt_qchem_spade_ef_calculations
│   ├── mm_min_starting_structures
│   │   ├── 19nt_mm_min_distance_cutoff3_nowat_optimized_spade_wb97x-v_631gd.efield
│   │   ├── 19nt_mm_min_distance_cutoff3_nowat_optimized_spade_wb97x-v_631gd.out
│   │   ├── 19nt_mm_min_distance_cutoff3_nowat_optimized_spade_wb97x-v_631gd_efield.out
│   │   ├── 19nt_mm_min_distance_cutoff3_nowat_xtb_optimized_spade_wb97x-v_631gd.efield
│   │   ├── 19nt_mm_min_distance_cutoff3_nowat_xtb_optimized_spade_wb97x-v_631gd.out
│   │   ├── 19nt_mm_min_distance_cutoff3_nowat_xtb_optimized_spade_wb97x-v_631gd_efield.out
│   │   ├── 19nt_mm_min_distance_cutoff3_optimized_spade_wb97x-v_631gd.efield
│   │   ├── 19nt_mm_min_distance_cutoff3_optimized_spade_wb97x-v_631gd.out
│   │   ├── 19nt_mm_min_distance_cutoff3_optimized_spade_wb97x-v_631gd_efield.out
│   │   ├── 19nt_mm_min_distance_cutoff3_xtb_optimized_spade_wb97x-v_631gd.efield
│   │   ├── 19nt_mm_min_distance_cutoff3_xtb_optimized_spade_wb97x-v_631gd.out
│   │   ├── 19nt_mm_min_distance_cutoff3_xtb_optimized_spade_wb97x-v_631gd_efield.out
│   │   ├── 19nt_mm_min_distance_cutoff4_nowat_optimized_spade_wb97x-v_631gd.efield
│   │   ├── 19nt_mm_min_distance_cutoff4_nowat_optimized_spade_wb97x-v_631gd.out
│   │   ├── 19nt_mm_min_distance_cutoff4_nowat_optimized_spade_wb97x-v_631gd_efield.out
│   │   ├── 19nt_mm_min_distance_cutoff4_nowat_xtb_optimized_spade_wb97x-v_631gd.efield
│   │   ├── 19nt_mm_min_distance_cutoff4_nowat_xtb_optimized_spade_wb97x-v_631gd.out
│   │   ├── 19nt_mm_min_distance_cutoff4_nowat_xtb_optimized_spade_wb97x-v_631gd_efield.out
│   │   ├── 19nt_mm_min_distance_cutoff4_optimized_spade_wb97x-v_631gd.efield
│   │   ├── 19nt_mm_min_distance_cutoff4_optimized_spade_wb97x-v_631gd.out
│   │   ├── 19nt_mm_min_distance_cutoff4_optimized_spade_wb97x-v_631gd_efield.out
│   │   ├── 19nt_mm_min_distance_cutoff4_xtb_optimized_spade_wb97x-v_631gd.efield
│   │   ├── 19nt_mm_min_distance_cutoff4_xtb_optimized_spade_wb97x-v_631gd.out
│   │   ├── 19nt_mm_min_distance_cutoff4_xtb_optimized_spade_wb97x-v_631gd_efield.out
│   │   ├── 19nt_mm_min_distance_cutoff5_nowat_optimized_spade_wb97x-v_631gd.efield
│   │   ├── 19nt_mm_min_distance_cutoff5_nowat_optimized_spade_wb97x-v_631gd.out
│   │   ├── 19nt_mm_min_distance_cutoff5_nowat_optimized_spade_wb97x-v_631gd_efield.out
│   │   ├── 19nt_mm_min_distance_cutoff5_nowat_xtb_optimized_spade_wb97x-v_631gd.efield
│   │   ├── 19nt_mm_min_distance_cutoff5_nowat_xtb_optimized_spade_wb97x-v_631gd.out
│   │   ├── 19nt_mm_min_distance_cutoff5_nowat_xtb_optimized_spade_wb97x-v_631gd_efield.out
│   │   ├── 19nt_mm_min_distance_cutoff5_optimized_spade_wb97x-v_631gd.efield
│   │   ├── 19nt_mm_min_distance_cutoff5_optimized_spade_wb97x-v_631gd.out
│   │   ├── 19nt_mm_min_distance_cutoff5_optimized_spade_wb97x-v_631gd_efield.out
│   │   ├── 19nt_mm_min_distance_cutoff5_xtb_optimized_spade_wb97x-v_631gd.efield
│   │   ├── 19nt_mm_min_distance_cutoff5_xtb_optimized_spade_wb97x-v_631gd.out
│   │   ├── 19nt_mm_min_distance_cutoff5_xtb_optimized_spade_wb97x-v_631gd_efield.out
│   │   ├── 19nt_mm_min_distance_cutoff6_nowat_optimized_spade_wb97x-v_631gd.efield
│   │   ├── 19nt_mm_min_distance_cutoff6_nowat_optimized_spade_wb97x-v_631gd.out
│   │   ├── 19nt_mm_min_distance_cutoff6_nowat_optimized_spade_wb97x-v_631gd_efield.out
│   │   ├── 19nt_mm_min_distance_cutoff6_nowat_xtb_optimized_spade_wb97x-v_631gd.efield
│   │   ├── 19nt_mm_min_distance_cutoff6_nowat_xtb_optimized_spade_wb97x-v_631gd.out
│   │   ├── 19nt_mm_min_distance_cutoff6_nowat_xtb_optimized_spade_wb97x-v_631gd_efield.out
│   │   ├── 19nt_mm_min_distance_cutoff6_xtb_optimized_spade_wb97x-v_631gd.efield
│   │   ├── 19nt_mm_min_distance_cutoff6_xtb_optimized_spade_wb97x-v_631gd.out
│   │   ├── 19nt_mm_min_distance_cutoff6_xtb_optimized_spade_wb97x-v_631gd_efield.out
│   │   └── README.md
│   └── xstal_starting_structure
│       ├── 19nt_xstal_distance_cutoff3_optimized_spade_wb97x-v_631gd.efield
│       ├── 19nt_xstal_distance_cutoff3_optimized_spade_wb97x-v_631gd.out
│       ├── 19nt_xstal_distance_cutoff3_xtb_optimized_spade_wb97x-v_631gd.efield
│       ├── 19nt_xstal_distance_cutoff3_xtb_optimized_spade_wb97x-v_631gd.out
│       ├── 19nt_xstal_distance_cutoff4_optimized_spade_wb97x-v_631gd.efield
│       ├── 19nt_xstal_distance_cutoff4_optimized_spade_wb97x-v_631gd.out
│       ├── 19nt_xstal_distance_cutoff4_xtb_optimized_spade_wb97x-v_631gd.efield
│       ├── 19nt_xstal_distance_cutoff4_xtb_optimized_spade_wb97x-v_631gd.out
│       ├── 19nt_xstal_distance_cutoff5_optimized_spade_wb97x-v_631gd.efield
│       ├── 19nt_xstal_distance_cutoff5_optimized_spade_wb97x-v_631gd.out
│       ├── 19nt_xstal_distance_cutoff5_xtb_optimized_spade_wb97x-v_631gd.efield
│       ├── 19nt_xstal_distance_cutoff5_xtb_optimized_spade_wb97x-v_631gd.out
│       ├── 19nt_xstal_distance_cutoff6_optimized_spade_wb97x-v_631gd.efield
│       ├── 19nt_xstal_distance_cutoff6_optimized_spade_wb97x-v_631gd.out
│       ├── 19nt_xstal_distance_cutoff6_xtb_optimized_spade_wb97x-v_631gd.efield
│       ├── 19nt_xstal_distance_cutoff6_xtb_optimized_spade_wb97x-v_631gd.out
│       ├── 19nt_xstal_distance_cutoff7_optimized_spade_wb97x-v_631gd.efield
│       ├── 19nt_xstal_distance_cutoff7_optimized_spade_wb97x-v_631gd.out
│       ├── 19nt_xstal_distance_cutoff7_xtb_optimized_spade_wb97x-v_631gd.efield
│       ├── 19nt_xstal_distance_cutoff7_xtb_optimized_spade_wb97x-v_631gd.out
│       ├── 19nt_xstal_distance_cutoff8_optimized_spade_wb97x-v_631gd.efield
│       ├── 19nt_xstal_distance_cutoff8_optimized_spade_wb97x-v_631gd.out
│       ├── 19nt_xstal_distance_cutoff8_xtb_optimized_spade_wb97x-v_631gd.efield
│       ├── 19nt_xstal_distance_cutoff8_xtb_optimized_spade_wb97x-v_631gd.out
│       └── README.md
├── MD Simulations
│   ├── EQU_parameterizatin
│   │   ├── 1st.chg
│   │   ├── 1st.esp
│   │   ├── 1st.in
│   │   ├── 1st.out
│   │   ├── 2nd.chg
│   │   ├── 2nd.esp
│   │   ├── 2nd.in
│   │   ├── 2nd.out
│   │   ├── EQU.mol2
│   │   ├── EQU_b3lyp_opt.xyz
│   │   ├── EQU_b3lyp_opt_esp.dat
│   │   ├── EQU_b3lyp_opt_esp.log
│   │   ├── EQU_geom_labeled.png
│   │   └── pyresp.run
│   ├── TUPA Data
│   │   ├── 1oh0_equ.prmtop
│   │   ├── ElecField_proj_onto_bond1-500.dat
│   │   ├── ElecField_proj_onto_bond1001-1500.dat
│   │   ├── ElecField_proj_onto_bond1501-2000.dat
│   │   ├── ElecField_proj_onto_bond2001-2500.dat
│   │   ├── ElecField_proj_onto_bond501-1000.dat
│   │   ├── config_chainA.conf
│   │   ├── full_md_representative_pdbs
│   │   │   ├── max_md_rep.pdb
│   │   │   ├── median_md_rep.pdb
│   │   │   └── min_md_rep.pdb
│   │   ├── min_middle_max_centered.nc
│   │   └── truncated_md_representative_pdbs
│   │       ├── models_based_on_largest_model_cutoffs
│   │       │   ├── max
│   │       │   │   ├── cutoff3_max.pdb
│   │       │   │   ├── cutoff4_max.pdb
│   │       │   │   ├── cutoff5_max.pdb
│   │       │   │   ├── cutoff6_max.pdb
│   │       │   │   ├── cutoff7_max.pdb
│   │       │   │   └── cutoff8_max.pdb
│   │       │   ├── median
│   │       │   │   ├── cutoff3_median.pdb
│   │       │   │   ├── cutoff4_median.pdb
│   │       │   │   ├── cutoff5_median.pdb
│   │       │   │   ├── cutoff6_median.pdb
│   │       │   │   ├── cutoff7_median.pdb
│   │       │   │   └── cutoff8_median.pdb
│   │       │   └── min
│   │       │       ├── cutoff3_min.pdb
│   │       │       ├── cutoff4_min.pdb
│   │       │       ├── cutoff5_min.pdb
│   │       │       ├── cutoff6_min.pdb
│   │       │       ├── cutoff7_min.pdb
│   │       │       └── cutoff8_min.pdb
│   │       └── models_based_on_mm_min_residues
│   │           ├── max
│   │           │   ├── cutoff3_max.pdb
│   │           │   ├── cutoff4_max.pdb
│   │           │   ├── cutoff5_max.pdb
│   │           │   ├── cutoff6_max.pdb
│   │           │   ├── cutoff7_max.pdb
│   │           │   └── cutoff8_max.pdb
│   │           ├── median
│   │           │   ├── cutoff3_median.pdb
│   │           │   ├── cutoff4_median.pdb
│   │           │   ├── cutoff5_median.pdb
│   │           │   ├── cutoff6_median.pdb
│   │           │   ├── cutoff7_median.pdb
│   │           │   └── cutoff8_median.pdb
│   │           └── min
│   │               ├── cutoff3_min.pdb
│   │               ├── cutoff4_min.pdb
│   │               ├── cutoff5_min.pdb
│   │               ├── cutoff6_min.pdb
│   │               ├── cutoff7_min.pdb
│   │               └── cutoff8_min.pdb
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
│   │   ├── 1oh0_19nt_crystal_distance_cutoff3_dft.com
│   │   ├── 1oh0_19nt_crystal_distance_cutoff3_xtb.inp
│   │   ├── 1oh0_19nt_crystal_distance_cutoff4_dft.com
│   │   ├── 1oh0_19nt_crystal_distance_cutoff4_xtb.inp
│   │   ├── 1oh0_19nt_crystal_distance_cutoff5_dft.com
│   │   ├── 1oh0_19nt_crystal_distance_cutoff5_xtb.inp
│   │   ├── 1oh0_19nt_crystal_distance_cutoff6_dft.com
│   │   ├── 1oh0_19nt_crystal_distance_cutoff6_xtb.inp
│   │   ├── 1oh0_19nt_crystal_distance_cutoff7_dft.com
│   │   ├── 1oh0_19nt_crystal_distance_cutoff7_xtb.inp
│   │   ├── 1oh0_19nt_crystal_distance_cutoff8_dft.com
│   │   ├── 1oh0_19nt_crystal_distance_cutoff8_xtb.inp
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_dft.com
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_no_wat_dft.com
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_no_wat_xtb.inp
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff3_xtb.inp
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_dft.com
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_no_wat_dft.com
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_no_wat_xtb.inp
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff4_xtb.inp
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_dft.com
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_no_wat_dft.com
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_no_wat_xtb.inp
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff5_xtb.inp
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_dft.com
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_no_wat_dft.com
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_no_wat_xtb.inp
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff6_xtb.inp
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_dft.com
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_no_wat_dft.com
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_no_wat_xtb.inp
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff7_xtb.inp
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff8_dft.com
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff8_no_wat_dft.com
│   │   ├── 1oh0_19nt_mm_minimized_distance_cutoff8_no_wat_xtb.inp
│   │   └── 1oh0_19nt_mm_minimized_distance_cutoff8_xtb.inp
│   ├── add_Hs.in
│   ├── ksi_19nt_model_generation.out
│   └── ksi_19nt_model_generation.py
└── ksi_composed_data_qmzyme.xlsx
