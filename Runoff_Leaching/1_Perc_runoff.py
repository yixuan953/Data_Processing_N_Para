# This code is used to calculate the runoff fraction (L_runoff)
# Lrunoff = Lmax_runoff * fpre_surplus * ftexture * frock

import xarray as xr
import numpy as np
import glob
import os

# 1. Calculate Lmax_runoff that is dependent on slope percentage (%)
input_slope = "/lustre/nobackup/WUR/ESG/zhou111/Data/Raw/Slope/ddm30_slopes_cru_neva.nc"
ds_slope = xr.open_dataset(input_slope)
lat = ds_slope["lat"].values
lon = ds_slope["lon"].values
slope_degree = ds_slope["slope"][:]  # [-]
slope = slope_degree * 100  # [%] so that the classification matches with MITERRA

Lmax_runoff = xr.full_like(slope, fill_value=np.nan) 
Lmax_runoff = xr.where((slope >= 0) & (slope < 8), 0.10, Lmax_runoff)
Lmax_runoff = xr.where((slope >= 8) & (slope < 15), 0.20, Lmax_runoff)
Lmax_runoff = xr.where((slope >= 15) & (slope < 25), 0.35, Lmax_runoff)
Lmax_runoff = xr.where((slope >= 25), 0.50, Lmax_runoff)

# 2. Calculate ftexture that is dependent on clay content (%)
input_soil = "/lustre/nobackup/WUR/ESG/zhou111/Data/Raw/Soil/hwsd_soil_data_on_cropland.nc"
ds_soil = xr.open_dataset(input_soil)
lat = ds_slope["lat"].values
lon = ds_slope["lon"].values
clay = ds_soil["clay"][:]  # [%]

ftexture= xr.full_like(clay, fill_value=np.nan) 
ftexture = xr.where((clay < 18), 0.25, ftexture)
ftexture = xr.where((clay >= 18) & (clay < 34), 0.75, ftexture)
ftexture = xr.where((clay >= 34) & (clay < 60), 0.90, ftexture)
ftexture = xr.where((clay >= 60), 1.0, ftexture)