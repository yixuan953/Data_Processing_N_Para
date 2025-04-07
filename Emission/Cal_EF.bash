#!/bin/bash
#-----------------------------Mail address-----------------------------

#-----------------------------Output files-----------------------------
#SBATCH --output=HPCReport/output_%j.txt
#SBATCH --error=HPCReport/error_output_%j.txt

#-----------------------------Required resources-----------------------
#SBATCH --time=600
#SBATCH --mem=250000

#--------------------Environment, Operations and Job steps-------------
# Step 1 - Calculate EF_NOx 
# module load python/3.12.0
# python /lustre/nobackup/WUR/ESG/zhou111/Code/Data_Processing/N_cycling_Parameters/Emission/1_EF_NOx.py

# Step 2 - Calculate EF_NO2
module load cdo
input_dir="/lustre/nobackup/WUR/ESG/zhou111/Data/Raw/Climate/ERA5"
process_dir="/lustre/nobackup/WUR/ESG/zhou111/Data/Processed/Climate/ERA5"

get_mean_annual_T(){
    cdo seldate,1985-01-01,2015-12-31 \
    ${input_dir}/t_ERA5-Land_mon_195001-202212.nc \
    ${process_dir}/t_1985_2015.nc

    cdo yearmean ${process_dir}/t_1985_2015.nc ${process_dir}/t_annual_1985_2015.nc
    
    cdo remapcon,grid_0.5.txt ${process_dir}/t_mean_1985_2015.nc ${input_dir}/t_mean_1985_2015_05deg.nc

    echo "Mean annual temperature at 0.5 degree has been calculated"
}

get_mean_ET(){
    cdo seldate,1985-01-01,2015-12-31 \
    ${input_dir}/pr_ERA5-Land_mon_195001-202212.nc \
    ${process_dir}/pr_1985_2015.nc
    cdo seldate,1985-01-01,2015-12-31 \
    ${input_dir}/evspsbl_ERA5-Land_mon_195001-202212.nc \
    ${process_dir}/et_1985_2015.nc

    cdo ydaysum ${process_dir}/pr_1985_2015.nc ${process_dir}/pr_annual_1985_2015.nc
    cdo ydaysum ${process_dir}/et_1985_2015.nc ${process_dir}/et_annual_1985_2015.nc

    cdo sub ${process_dir}/et_annual_1985_2015.nc ${process_dir}/pr_annual_1985_2015.nc ${process_dir}/wb_annual_1985_2015.nc

    cdo timmean ${process_dir}/wb_annual_1985_2015.nc ${process_dir}/wb_mean_1985_2015.nc

    cdo remapcon,grid_0.5.txt ${process_dir}/wb_mean_1985_2015.nc ${input_dir}/wb_mean_1985_2015_05deg.nc 

    echo "Mean annual ET-P at 0.5 degree has been calculated"
}

get_mean_annual_T
get_mean_annual_ET