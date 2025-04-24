Soil N supply through SOM decomposition at annual scale is calculated using the following function:
Soil_N_decomp = (SOC * SOC_decomposition_rate * CorrectionFactor_temp * CorrectionFactor_moisture * GrowingDays/365) / soil CN ratio


In which:
1 - SOC data is available from the HSWD at: https://www.hydroshare.org/resource/1361509511e44adfba814f6950c6e742/
    - Variable name: oc [percent weight, 0-1]
    - Long name: Topsoil Organic Carbon 
2 - Soil decomposition rate = 0.05/yr (Reference?)
3 - CorrectionFactor_temp: m_temp. The temperature [celsuis degree] (-10, 40) --> m_temp (0, 6.5)
    m_temp = 47.91 / (1 + e^(106.6 / (T + 18.27))) 
    Here, T is the monthly mean temperature calculated basing on the daily mean temperature.
4 - CorrectionFactor_moisture: m_moist
    4-1 Calculate the maximum topsoil moisture deficit (TSMD_max) = -(20.0 + 1.3K - 0.01K^2) * D/23 if soil is vegetated
        Here K is the clay content [%], D is the depth of topsoil depth [cm]?
    4-2 Calculate the precipitation surplus = Monthly precipitation - Monthly Evapotranspiration [mm] Can I use the output of VIC here?
    4-3 Calculate the TSMD = TSMD_acc + precipitation surplus 
        Here, TSMDacc = max(TSMD, TSMD_max) if TSMD <0 OR 0.0 if TSMD>=0
    4.4 m_moist = 1.0 if TSDM_acc < 0.444 TSMD OR 0.2 + 0.8 * (TSMD_max - TSMD_acc) /(TSMD_max - 0.444 * TSMD_max)
5 - GrowingDays: The data source is from the crop calendar of Sacks et al. (2010) (DOI: 10.1111/j.1466-8238.2010.00551.x)
Here:
    For regions where maturity and sowing happen in the same year: GrowingDays =  (mat_a1 - sow_a1)  (average matuarity date - average sowing date) * 10 (in order to transform dekad to days) 
    For regions where maturity and sowing happen in different years: GrowingDays =  (36 - sow_a1 + mat_a1) * 10
6 - Soil CN ratio is available from SoilGrids at: https://files.isric.org/soilgrids/latest/.
Here:
    6-1 Soil organic carbon (dg/kg) is available for 3 layers (0-5, 5-15, 15-30 cm) at 5 km 
    6-2 Soil bulk density (cg/cm3) is available for 3 layers (0-5, 5-15, 15-30 cm) at 5 km
    6-3 Soil nitrogen content (cg/kg) is available for 3 layers (0-5, 5-15, 15-30 cm) at 5 km
The data is upscaled to 0-30 cm at 0.5 degree, by aggregating the total SOC and soil N amount [kg] (SOC_content or Soil_N_content * BulkDensity * LayerDepth * 5km * 5km)