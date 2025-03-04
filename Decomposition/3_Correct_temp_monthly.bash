#!/bin/bash
#-----------------------------Mail address-----------------------------

#-----------------------------Output files-----------------------------
#SBATCH --output=HPCReport/output_%j.txt
#SBATCH --error=HPCReport/error_output_%j.txt

#-----------------------------Required resources-----------------------
#SBATCH --time=600
#SBATCH --mem=250000

#--------------------Environment, Operations and Job steps-------------

input_dir="/lustre/nobackup/WUR/ESG/zhou111/Data/Climate_Forcing/WFDE5/Tair_Monthly_1981-2019.nc"
process_dir="/lustre/nobackup/WUR/ESG/zhou111/Data/Processed/Climate/WFDE5/Monthly"

# cdo mulc,0 ${process_dir}/T_offset.nc ${process_dir}/zero.nc            # Create a zero-filled file
# cdo addc,106.6 ${process_dir}/zero.nc ${process_dir}/constant_106.nc  # Create a constant 106.6 file
# cdo addc,47.91 ${process_dir}/zero.nc ${process_dir}/constant_47.nc  # Create a constant 106.6 file

module load cdo
#cdo addc,18.27 $temp_data ${process_dir}/T_offset.nc             
cdo setrtoc,-1.3,1.3,1.5 ${process_dir}/T_offset.nc  ${process_dir}/T_offset_adj.nc  # Step 1: T + 18.27

cdo div ${process_dir}/constant_106.nc ${process_dir}/T_offset_adj.nc ${process_dir}/T_div.nc  # Step 2: 106.6 / (T + 18.27)

module load python/3.12.0
cdo exp ${process_dir}/T_div_no_nan.nc ${process_dir}/T_exp.nc          # Step 3: e^(106.6 / (T + 18.27))

cdo addc,1.0 ${process_dir}/T_exp.nc ${process_dir}/T_denominator.nc    # Step 4: 1 + e^(106.6 / (T + 18.27))
cdo div, ${process_dir}/constant_47.nc ${process_dir}/T_denominator.nc ${process_dir}/m_temp.nc # Step 5: 47.91 / (1 + e^(106.6 / (T + 18.27)))