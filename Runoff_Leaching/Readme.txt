In order to calculate the N losses through surface runoff and leaching, we need to calculate the fraction of N losses through runoff (Lrunoff) and leaching (Lleaching)
In which: 
Lrunoff = Lmax_runoff × flanduse × fprecip × ftexture × froc
Lleaching = Lmax_leaching × flanduse × fprecip × ftemp × froot × fsoc

1. Lrunoff calculation contains elements as follows:
   1) Lmax_runoff depends on slope percentage (= slope degree * 100)
   2) flanduse = 0.25 for grassland, = 1.0 for others
   3) fprecip depends on precipitation surplus (mm): Annaul precipitation - annual evapotranspiration
   4) ftexture depends on the clay content (%)
   5) frock is a reduction factor for the depth to rock: Soil Depth from ISRIC (https://data.isric.org/geonetwork/srv/api/records/f36117ea-9be5-4afd-bb7d-7a3e77bf392a)
   Questions: here I do not have the data, but can I assume it is larger than 25 cm as my topsoil depth is assumed to be 30 cm, and the rooting depth of all of my crops are larger than 40cm

2. Lleaching calculation contains elements as follows:
   1) Lmax_leaching depends on texture class, the value
            = 1.00, if the texture class = Sand (coding number in HWSD: 1, 2)
            = 0.75, if the texture class = Loam (coding number in HWSD: 3-9)
            = 0.50, if the texture class = Clay, heavy clay or peat (coding number in HWSD: 10-12)
   2) flanduse = 0.36 for grassland, = 1.0 for others
   3) fprecip depends on 
        - Precipitation surplus (mm): Annaul precipitation - annual evapotranspiration [mm]
        - Soil texture class (same classification as step 2-1)
   4) ftemp depends on average annual temperature [celsuis degree], the value
            = 1.00, if Ave_temp < 5
            = 0.75, if Ave_temp >=5, <15
            = 0.50, if Ave_temp =>15
   5) froot depends on rooting depth class, the value (Question: only Europe has this data) 
            = 1.00, if the obastacle to roots between 20–60 cm depth
            = 0.75, if the obastacle to roots between 60-80 cm depth, or no obastacle to roots
          We could make assumptions using the rooting depth data of main crops from FAO (https://www.fao.org/4/y5749e/y5749e0j.htm):
            - Maize: 0.9 m (froot = 0.75)
            - Wheat: 1.0 m (froot = 0.75)
            - Rice: 0.5 m
            - Soybean: 0.6 m
   6) fsoc depends on soil organic carbon content, the value
            = 0.50, if SOC > 6%
            = 0.75, if 2% < SOC <= 6% 
            = 0.90, if 1% < SOC <= 2% 
            = 1.00, if SOC <= 1% 