import QMzyme
import pandas

# Add unknown residue charges
QMzyme.data.residue_charges.update({'EQU': -1}) # EQU ligand
QMzyme.data.residue_charges.update({'6VW': 0}) # 19nt ligand

# Define calculation methods to make input files for DFT and xTB optimizations
calculation_methods = []
dft = QMzyme.QM_Method(
    program='gaussian', 
    basis_set="6-31G(d)", 
    functional="wb97xd", 
    qm_input="opt freq prop=efg"
)
xtb = QMzyme.QM_Method(
    program='orca', 
    basis_set="", 
    functional="", 
    qm_input="XTB2 opt"
)

# Make QMzymeRegion for 19nt ligand
ligand_19nt_file = '19nt_ligand_from_5kp4.pdb'
ligand_model = QMzyme.GenerateModel(ligand_19nt_file)
ligand_model.set_region(selection = 'all', name='ligand_19nt')
region_19nt = ligand_model.ligand_19nt

for starting_structure in ['1oh0_equ_crystal.pdb', '1oh0_equ_mm_minimized.pdb']:
    name_base = f"1oh0_19nt_{starting_structure.split('equ_')[-1].split('.pdb')[0]}"
    for calculation_method in [dft, xtb]:
        for cutoff in [3, 4, 5, 6, 7, 8]:
            print('='*100)
            waters = ''
            calc_type = 'dft'
            mem = "64GB"
            if 'XTB' in calculation_method.qm_input:
                calc_type = 'xtb'
                mem = 2000
            name = name_base + f"_distance_cutoff{cutoff}{waters}_{calc_type}"
            ksi_model = QMzyme.GenerateModel(starting_structure, name=name)
            ksi_model.set_catalytic_center(selection='resname EQU and segid A')
            ksi_model.set_region(selection=QMzyme.SelectionSchemes.DistanceCutoff, cutoff=cutoff, name=f"cutoff_{cutoff}")
        
            # Align new ligand to EQU coords
            region_19nt.align_to(other=ksi_model.catalytic_center, self_selection="element C", other_selection="element C")
        
            # Combine new ligand and protein in new QMzymeRegion
            new_region_name = f"1oh0_19nt"
            new_region = ksi_model.get_region(f"cutoff_{cutoff}").combine(region_19nt, name=new_region_name)
        
            # Remove old ligand
            new_region = new_region.subtract(ksi_model.catalytic_center)
        
            # Add new region to ksi_model
            ksi_model.set_region(selection=new_region, name=f"ksi_19nt_cutoff{cutoff}")
        
            # Assign alpha carbon constraints
            ca_atoms = ksi_model.regions[-1].get_atoms(attribute="name", value="CA")
            ksi_model.regions[-1].set_fixed_atoms(atoms=ca_atoms)
        
            # Assign QM method
            calculation_method.assign_to_region(ksi_model.regions[-1])
        
            # Truncate to only include atoms in this region
            ksi_model.truncate(scheme = QMzyme.TruncationSchemes.TerminalAlphaCarbon)

            # Write input file
            ksi_model.write_input(
                memory=str(mem), 
                nprocs=32, 
                filename=name
            )
            df = pandas.DataFrame(ksi_model.regions[-1].summarize())
            df.to_csv(name+'.csv')
            print(df)

            # Generate no_waters QMzymeModels for mm_minimized models:
            if 'mm_min' in starting_structure:
                waters = '_no_wat'
                name = name_base + f"_distance_cutoff{cutoff}{waters}_{calc_type}"
                ksi_model.name = name
                for atom in ksi_model.regions[-1].get_atoms(attribute="resname", value="WAT"):
                    ksi_model.regions[-1].remove_atom(atom)
                ksi_model.write_input(
                    memory=str(mem), 
                    nprocs=32, 
                    filename=name
                )
                df = pandas.DataFrame(ksi_model.regions[-1].summarize())
                df.to_csv(name+'.csv')
                print(df)