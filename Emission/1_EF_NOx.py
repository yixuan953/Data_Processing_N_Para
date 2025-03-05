# This code is used to calculate the emission factor of NOx which depends on annual precipitation

import xarray as xr
import numpy as np
import glob
import os

input_file = '/lustre/nobackup/WUR/ESG/zhou111/Data/Climate_Forcing/WFDE5/Prec_Annual_1981-2019.nc'
output_dir = '/lustre/nobackup/WUR/ESG/zhou111/Data/Para_N_Cycling'

ds = xr.open_dataset(input_file)

time = ds["time"].values
lat = ds["lat"].values
lon = ds["lon"].values
prec = ds["Prec"][:]  # [mm]

# Assign different EF_NOx to differetn precipitation values
EF_NOx = xr.full_like(prec, fill_value=np.nan)  # Create an empty array with the same shape
EF_NOx = xr.where(prec < 400, 0.0019, EF_NOx)
EF_NOx = xr.where((prec >= 400) & (prec < 600), 0.0059, EF_NOx)
EF_NOx = xr.where((prec >= 600) & (prec < 800), 0.0071, EF_NOx)
EF_NOx = xr.where((prec >= 800) & (prec < 1000), 0.0048, EF_NOx)
EF_NOx = xr.where((prec >= 1000) & (prec < 1500), 0.0018, EF_NOx)
EF_NOx = xr.where(prec >= 1500, 0.0024, EF_NOx)

a = xr.DataArray(
    EF_NOx,
    dims=("time","lat", "lon"),
    coords={
    "time": time,
    "lon": lon,
    "lat": lat,
    },
    name = "EF_NOx",
    attrs={
           "units": "-"
            }
)

output_nc_file = os.path.join(output_dir, f"EF_NOx.nc")    
a.to_netcdf(output_nc_file)
print(f"EF_NOx has been calculated and saved to {output_nc_file}")