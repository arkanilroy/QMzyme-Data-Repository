# Title 
QMzyme: Automated and Systematic QM-based Enzyme Model Construction

# Contents
The following list contains all the files and directories in the parent directory:

* 19nt_gaussian_efg_calculations: Contains output files for the gaussian16(prop=efg) electric field calculations for starting structures for both MM minimzied as well as crystal starting structures

* 19nt_optimizations: Contains structure files for optimized models with 19NT in the active site

* 19nt_qchem_spade_ef_calculations: Contains output files for the QChem SPADE electric field calculations for starting structures for both MM minimzied as well as crystal starting structures

* MD simulations: Contains parameterization data for equilenin, as well as TUPA results

* Scripts: Contains scripts for parsing electric field data, determining RMSD and plotting the data

* cluster_model_generation: Contains all starting models for optimizations, and the script to align and replace equilenin with 19NT.

* ksi_composed_data_qmzyme.xlsx: Contains raw values of all the data in the paper
# Data structure

QMzyme-Data-Repository/ \
├── 19nt_gaussian_efg_calculations \
│   ├── mm_minimized_starting_structure \
│   └── xstal_starting_structure \
├── 19nt_optimizations \
│   ├── mm_minimized_starting_structure \
│   └── xstal_starting_structure \
├── 19nt_qchem_spade_ef_calculations \
│   ├── mm_min_starting_structures \
│   └── xstal_starting_structure \
├── MD Simulations \
│   ├── EQU_parameterizatin \
│   ├── TUPA Data \
│   └── tleap.in \
├── README.md \
├── Scripts \
├── cluster_model_generation \
└── ksi_composed_data_qmzyme.xlsx 

