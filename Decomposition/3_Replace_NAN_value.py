import xarray as xr
import numpy as np

# Open the NetCDF file
file_path = '/lustre/nobackup/WUR/ESG/zhou111/Data/Processed/Climate/WFDE5/Monthly/T_div.nc'  
output_path = '/lustre/nobackup/WUR/ESG/zhou111/Data/Processed/Climate/WFDE5/Monthly/T_div_no_nan.nc'  

# Open the dataset
ds = xr.open_dataset(file_path)

for var in ds.data_vars:
    if np.issubdtype(ds[var].dtype, np.floating):  # Only process floating-point variables
        ds[var] = ds[var].fillna(-2.0)
        # Which means that 106.6/(T+18.27) = -1

# Save the modified dataset to a new NetCDF file
ds.to_netcdf(output_path)

print(f"NaN values replaced and saved to {output_path}")