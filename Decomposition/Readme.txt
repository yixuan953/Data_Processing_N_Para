Soil N supply through SOM decomposition at annual scale is calculated using the following function:
Soil_N_decomp = (SOC * SOC_decomposition_rate * CorrectionFactor_temp * CorrectionFactor_moisture * GrowingDays/365) / soil CN ratio

In which:
1 - SOC data is available from the HSWD at: https://www.hydroshare.org/resource/1361509511e44adfba814f6950c6e742/
2 - Soil decomposition rate = 0.05/yr (Reference?)
3 - CorrectionFactor_temp: m_temp, the reasonable range should be (0, 6)
4 - CorrectionFactor_moisture: 
5 - GrowingDays: "mat_a1 - sow_a1" - average matuarity date - sowing date (Crop calendar from Sacks et al., 2010. DOI: 10.1111/j.1466-8238.2010.00551.x) 
6 - Soil CN ratio is available from SoilGrids at: https://files.isric.org/soilgrids/latest/.
Here:
    6-1 Soil organic carbon (dg/kg) is available for 3 layers (0-5, 5-15, 15-30 cm) at 5 km 
    6-2 Soil bulk density (cg/cm3) is available for 3 layers (0-5, 5-15, 15-30 cm) at 5 km
    6-3 Soil nitrogen content (cg/kg) is available for 3 layers (0-5, 5-15, 15-30 cm) at 5 km
The data is upscaled to 0-30 cm at 0.5 degree, by aggregating the total SOC and soil N amount [kg] (SOC_content or Soil_N_content * BulkDensity * LayerDepth * 5km * 5km)

The scripts used to calculate 