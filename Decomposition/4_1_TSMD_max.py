# This code is used to calculate the maximum topsoil soil moisture deficit (TSMD_max) for mositure factor:
# Here we assume that the soil is vegetated and the depth of the topsoil layer is 30 cm

import xarray as xr
import numpy as np
import glob
import os

input_file = '/lustre/nobackup/WUR/ESG/zhou111/Data/Raw/Soil/hwsd_soil_data_on_cropland.nc'
output_dir = '/lustre/nobackup/WUR/ESG/zhou111/Data/Para_N_Cycling'

soil_depth = 30 # [unit: cm]

ds = xr.open_dataset(input_file)

lat = ds["lat"].values
lon = ds["lon"].values
clay = ds["clay"][:] # [unit: %]

TSMD_max = -(20.0 + 1.3 * clay - 0.01 * clay * clay) * soil_depth/23

a = xr.DataArray(
    TSMD_max,
    dims=("lat", "lon"),
    coords={
    "lon": lon,
    "lat": lat,
    },
    name = "TSMD_max",
    attrs={
           "units": "-"
            }
)

output_nc_file = os.path.join(output_dir, f"TSMD_max.nc")    
a.to_netcdf(output_nc_file)
print(f"TSMD_max has been calculated and saved to {output_nc_file}")