# This code is used to calculate the growing length of each crop, and transforming dekad to days

import xarray as xr
import numpy as np
import glob
import os

input_dir = '/lustre/nobackup/WUR/ESG/zhou111/Data/Raw/Crop_SPAM2005v3.2_Sacks_CC'
process_dir = '/lustre/nobackup/WUR/ESG/zhou111/Data/Processed/CropMask/Sow_Mat_Date'
output_dir = '/lustre/nobackup/WUR/ESG/zhou111/Data/Para_N_Cycling/GrowingLength'

crop_types = ["mainrice", "maize", "secondrice", "soybean", "springwheat", "winterwheat"]

for crop in crop_types:

    input_file = os.path.join(input_dir, f"{crop}-char-05d_C3S-glob-agric_2005_v5.nc")
    ds = xr.open_dataset(input_file) 

    time = ds["time"].values
    lat = ds["lat"].values
    lon = ds["lon"].values

    mat_a1 = ds["mat_a1"][:]
    sow_a1 = ds["sow_a1"][:]

    GrowingLength = mat_a1 - sow_a1
    # For some regions, sowing and maturity do not happen in the same year. For these regions:
    GrowingLength = np.where(GrowingLength < 0, 36 - sow_a1 + mat_a1, GrowingLength)
    
    GrowingDays = GrowingLength * 10 

    a = xr.DataArray(
        GrowingDays,
        dims=("time", "lat", "lon"),
        coords={
        "time": time,
        "lon": lon,
        "lat": lat,
        },
        name = "GrowingDays",
        attrs={
            "units": "days"
                }
     )
    
    output_nc_file = os.path.join(process_dir, f"{crop}_GrowingDays.nc")    
    a.to_netcdf(output_nc_file)
    print(f"Growing days have been calculated and saved to {output_nc_file}")