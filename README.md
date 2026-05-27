# Title 
QMzyme: Automated and Systematic QM-based Enzyme Model Construction

# Contents
This repository contains all the data files that were used for geometry optimizations, electric field calculations and model generation , including final optimized structures. It also contains the scripts used to parse the electric field data, to determine RMSD and to plot them. All the raw data is also present in an excel sheet.

# Data structure

cluster_model_generation: Contains all starting models for optimizations, and the script to align and replace equilenin with 19NT.
MD simulations: Contains parameterization data for equilenin, as well as TUPA results. 
19nt_optimizations: Contains structure files for optimized models with 19NT in the active site
19nt_gaussian_efg_calculations: Contains output files for the gaussian16(prop=efg) electric field calculations for starting structures for both MM minimzied as well as crystal starting structures
19nt_qchem_spade_ef_calculations: Contains output files for the QChem SPADE electric field calculations for starting structures for both MM minimzied as well as crystal starting structures
Scripts: Contains scripts for parsing electric field data, determining RMSD and plotting the data.
ksi_composed_data_qmzyme.xlsx: Contains raw values of all the data in the paper

