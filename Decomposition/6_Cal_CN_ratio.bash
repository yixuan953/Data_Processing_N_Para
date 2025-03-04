#!/bin/bash
#-----------------------------Mail address-----------------------------

#-----------------------------Output files-----------------------------
#SBATCH --output=HPCReport/output_%j.txt
#SBATCH --error=HPCReport/error_output_%j.txt

#-----------------------------Required resources-----------------------
#SBATCH --time=600
#SBATCH --mem=250000

#--------------------Environment, Operations and Job steps-------------

# Step1. Reproject the original .tif files 
# This part does not work properly. I gave up. I did the reprojection using ArcGIS pro and it is way easier.
Reproject(){
    module load gdal
    for file in /lustre/nobackup/WUR/ESG/zhou111/Data/Raw/Soil/CN_ratio_cal/*.tif; do
        gdalwarp -s_srs EPSG:54008 -t_srs EPSG:4326 -r bilinear \
        -srcnodata -32768 -dstnodata -32768 \
        $file \
        "/lustre/nobackup/WUR/ESG/zhou111/Data/Raw/Soil/CN_ratio_cal/Reproject_$(basename "$file" .tif).tif"
    done

}
# Reproject

# Python scripts
module load python/3.12.0

# Step2. Calculate total SOC and soil nitrogen amount at 5 km resoution
python /lustre/nobackup/WUR/ESG/zhou111/Code/Data_Processing/N_cycling_Parameters/Decomposition/6_1_Cal_CN_amount_5km.py

# Step3. Upscale total SOC and soil nitrogen to 0.5 degree and calculate the CN ratio
python /lustre/nobackup/WUR/ESG/zhou111/Code/Data_Processing/N_cycling_Parameters/Decomposition/6_2_Res_Trans_Upscale_05d.py

# Step4. Calculate the CN ratio at half degree & rename the variable
module load cdo
module load nco
cdo -div /lustre/nobackup/WUR/ESG/zhou111/Data/Processed/Soil/SOC_top30cm_05d.nc /lustre/nobackup/WUR/ESG/zhou111/Data/Processed/Soil/N_top30cm_05d.nc /lustre/nobackup/WUR/ESG/zhou111/Data/Processed/Soil/CNratio_05d.nc
ncrename -v SOC,CN_ratio /lustre/nobackup/WUR/ESG/zhou111/Data/Processed/Soil/CNratio_05d.nc