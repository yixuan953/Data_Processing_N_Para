The gaseous emission factors contains three parts: EF_NOx, EF_NH3, and EF_N2O. In which;

1. EF_N2O: [0.0019, 0.0071] based on annual precipitation (mm)
    < 400:       0.0019
    [400,600):   0.0059
    [600,800):   0.0071
    [800,1000):  0.0048
    [1000,1500): 0.0018
    >=1500:      0.0024

2. EF_NH3: 
   Uread-based inorganic fertilisers: Emission factor for each country (NUTS0)
   Other inorganic fertilisers: Emission factor for each country (NUTS0)
   Livestock slurry: Estimated using the ALFAM2 model
Problems:
   How to prepare the global data? 
   For N fertilizer types, we only have manure, urea-based inorganic fertiliser, and other inorganic fertiliser.

3. EF_N20: 2019 IPCC guideline (Table 11.1 from Page 8)
Source: https://www.ipcc-nggip.iges.or.jp/public/2019rf/pdf/4_Volume4/19R_V4_Ch11_Soils_N2O_CO2.pdf
Question:
- As I do not know if the rice field is continuous flooding or single and multiple drainage, can I use the value 0.004?