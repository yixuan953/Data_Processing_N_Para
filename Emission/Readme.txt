The gaseous emission factors contains three parts: EF_NOx, EF_NH3, and EF_N2O. In which;

1. EF_NOx: [0.0019, 0.0071] based on annual precipitation (mm)
    < 400:       0.0019
    [400,600):   0.0059
    [600,800):   0.0071
    [800,1000):  0.0048
    [1000,1500): 0.0018
    >=1500:      0.0024

2. EF_NH3: 
   In Miterra:
      - Uread-based inorganic fertilisers: 0.15
      - Other inorganic fertilisers: 0.02
      - Manure: 0.20
   The emission factor could be found from IIASA (https://pure.iiasa.ac.at/id/eprint/7400/1/IR-04-048.pdf) 
   
3. EF_N20: 
In the new version of Miterra: It is dependent on climate zone and fertilizer types
Annual mean temperature, precipitation, and evapotranspiration are from ERA5 and available at: https://cds.climate.copernicus.eu/datasets/multi-origin-c3s-atlas?tab=download
                     | Cool Moist | Cool Dry | Warm Moist | Warm Dry |
   Mineral fertiliser|   0.016        0.005      0.016        0.005
   Manure            |   0.006        0.005      0.006        0.005
   Crop residue      |   0.006        0.005      0.006        0.005

Here:
   Cool moist: T <= 10 & P > ET 
   Cool dry:   T <= 10 & P <= ET
   Warm moist: T > 10 & P > ET 
   Warm dry:   T > 10 & P <= ET

In the old version of Miterra:
2019 IPCC guideline (Table 11.1 from Page 8)
Source: https://www.ipcc-nggip.iges.or.jp/public/2019rf/pdf/4_Volume4/19R_V4_Ch11_Soils_N2O_CO2.pdf