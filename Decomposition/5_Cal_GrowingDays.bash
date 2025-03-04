#!/bin/bash
#-----------------------------Mail address-----------------------------

#-----------------------------Output files-----------------------------
#SBATCH --output=HPCReport/output_%j.txt
#SBATCH --error=HPCReport/error_output_%j.txt

#-----------------------------Required resources-----------------------
#SBATCH --time=600
#SBATCH --mem=250000

#--------------------Environment, Operations and Job steps-------------
# Step 1 - Extract maturity date and sowing date from the original crop mask .nc files, calculate growing lengths and transform it from dekad to days
module load python/3.12.0
python /lustre/nobackup/WUR/ESG/zhou111/Code/Data_Processing/N_cycling_Parameters/Decomposition/5_1_Trans_GrowingLength.py

# Step 2 - Invert the latitude of the growing lengths files
module load cdo

input_dir='/lustre/nobackup/WUR/ESG/zhou111/Data/Processed/CropMask/Sow_Mat_Date'
output_dir='/lustre/nobackup/WUR/ESG/zhou111/Data/Para_N_Cycling/GrowingLength'
InvertLat () {
    for input_file in $input_dir/*.nc; do

        # Get the filename without the directory path
        filename=$(basename $input_file)
        output_file="$output_dir/$filename"
        
        # Invert latitude using cdo
        cdo -invertlat $input_file $output_file
        
        # Optional: Print status message
        echo "Inverted latitudes for $filename"
    done
}

InvertLat