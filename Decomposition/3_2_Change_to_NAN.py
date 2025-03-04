import xarray as xr
import numpy as np

file_path = '/lustre/nobackup/WUR/ESG/zhou111/Data/Processed/Climate/WFDE5/Monthly/m_temp.nc'  
output_path = '/lustre/nobackup/WUR/ESG/zhou111/Data/Para_N_Cycling/m_temp.nc'  
ds = xr.open_dataset(file_path)
var_name = "Tair"

# Replace value larger than 10 (temp lower than about -20 celsuis degree) to NAN
ds[var_name] = ds[var_name].where(ds[var_name] <= 10, np.nan)
ds = ds.rename({var_name: "m_temp"}) 

# Update the unit attribute
ds["m_temp"].attrs["units"] = "-" 
ds["m_temp"].attrs["long_name"] = "Temperature modification factor calculated basing on monthly mean temperature (celsuis degree)" 

# Save the results
ds.to_netcdf(output_path)
ds.close()
print(f"FillValue has been changed to NAN and saved to {output_path}")