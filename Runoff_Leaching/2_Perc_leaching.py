# This code is used to calculate the leaching fraction (L_runoff)
# Lleaching = Lmax_leaching × flanduse × fprecip × ftemp × froot × fsoc

import xarray as xr
import numpy as np
import glob
import os

# 1. Calculate the soil related reduction factors
input_soil = "/lustre/nobackup/WUR/ESG/zhou111/Data/Raw/Soil/hwsd_soil_data_on_cropland.nc"
ds_soil = xr.open_dataset(input_soil)
lat = ds_soil["lat"].values
lon = ds_soil["lon"].values

texture_class = ds_soil["texture_class"][:] # 1-2: Sand; 3-9: Loam; 10-12: Clay.  
soc = ds_soil["oc"][:] # Unit: %

# Lmax_leaching is related to texture class
Lmax_leaching = xr.full_like(texture_class, fill_value=np.nan) 
Lmax_leaching = xr.where((texture_class <= 2), 1.0, Lmax_leaching)
Lmax_leaching = xr.where((texture_class > 2) & (texture_class <= 9), 0.75, Lmax_leaching)
Lmax_leaching = xr.where((texture_class > 9) & (texture_class <= 12), 0.50, Lmax_leaching)

# fsoc is related to soc
fsoc = xr.full_like(soc, fill_value=np.nan) 
fsoc = xr.where((soc > 6), 0.5, fsoc)
fsoc = xr.where((soc > 2) & (soc <= 6), 0.75, fsoc)
fsoc = xr.where((soc > 1) & (soc <= 2), 0.90, fsoc)
fsoc = xr.where((soc <= 1), 1.0, fsoc)

# 2. Calculate the temperature related reduction factors
input_temp = "/lustre/nobackup/WUR/ESG/zhou111/Data/Climate_Forcing/WFDE5/Tair_Annual_1981-2019.nc"
ds_temp = xr.open_dataset(input_temp)
temp = ds_temp["Tair"][:]

ftemp = xr.full_like(temp, fill_value=np.nan) 
ftemp = xr.where((temp < 5), 1.0, ftemp)
ftemp = xr.where((temp < 15) & (temp >= 5), 0.75, ftemp)
ftemp = xr.where((temp >= 15), 0.5, ftemp)