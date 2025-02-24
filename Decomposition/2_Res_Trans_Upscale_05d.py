# This code is used to upscale C and N content to 0.5 degree and calculate the C:N ratio

import os
import glob
import rasterio
import numpy as np
import xarray as xr
from scipy.interpolate import griddata


# import xesmf as xe

input_dir = '/lustre/nobackup/WUR/ESG/zhou111/Data/Processed/Soil'
process_dir = '/lustre/nobackup/WUR/ESG/zhou111/Data/Processed/Soil'
output_dir = '/lustre/nobackup/WUR/ESG/zhou111/Data/Para_N_Cycling' # For the final C:N ratio .nc files

# Create latitude and longitude arrays
lat = np.linspace(90 - 0.25, -90 + 0.25, 360, dtype=np.float64)
lon = np.linspace(-180 + 0.25, 180 - 0.25, 720, dtype=np.float64)
target_grid = xr.Dataset(
    {
        "lat": (["lat"], lat),  # Global latitudes
        "lon": (["lon"], lon),  # Global longitudes
    }
)

vars = ["SOC", "N"]

for var in vars:
    f1 = os.path.join(process_dir, f"{var}_amount_0-5cm_5km.nc")
    ly1 = xr.open_dataset(f1)

    f2 = os.path.join(process_dir, f"{var}_amount_5-15cm_5km.nc")
    ly2 = xr.open_dataset(f2)

    f3 = os.path.join(process_dir, f"{var}_amount_15-30cm_5km.nc")
    ly3 = xr.open_dataset(f3)

    lat_orig = ly1.lat.values
    lon_orig = ly1.lon.values

    if var == "SOC":
       var_name = "SOC"
    
    if var == "N":
       var_name = "Soil N"
    
    data_ly1 = ly1[var_name][:]
    data_ly2 = ly2[var_name][:]
    data_ly3 = ly3[var_name][:]

    sum_all_ly = data_ly1 + data_ly2 + data_ly3

    # Create a meshgrid for interpolation
    lon_orig_mesh, lat_orig_mesh = np.meshgrid(lon_orig, lat_orig)
    lon_new_mesh, lat_new_mesh = np.meshgrid(lon, lat)

    # If xesmf module is available
    # regridder = xe.Regridder(sum_all_ly, target_grid, "bilinear")
    # ds_upscaled = regridder(sum_all_ly)

    ds_upscaled = griddata(
        (lon_orig_mesh.ravel(), lat_orig_mesh.ravel()),
         sum_all_ly.values.ravel(),
        (lon_new_mesh, lat_new_mesh),
         method="linear"  # or "nearest", "cubic"
    )

    ds_new = xr.Dataset(
    {var: (["lat", "lon"], ds_upscaled)},
     coords={"lat": lat, "lon": lon}
    )

    output_file = os.path.join(process_dir, f"{var}_top30cm_05d.nc")
    ds_new.to_netcdf(output_file)