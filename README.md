# local IAM 

This repository contains the data and model for the paper:  
**_“A Regional Integrated Assessment of Ocean Alkalinity Enhancement: Linking Biogeochemistry, Ecology, and Economics”_** 
<!-- The paper is published in [journal] and is available [here](link). -->

## Authors

- Lotta Siebert¹\*  
- Patricia Grasse² ³
- Wilfried Rickels¹ ⁴  

<details>
<summary>Affiliations (click to expand)</summary>

- **\*** Corresponding author: [lotta.siebert@ifw-kiel.de](mailto:lotta.siebert@ifw-kiel.de)  
- ¹ Global Commons and Climate Policy, Kiel Institute for the World Economy, Germany  
- ² German Centre for Integrative Biodiversity Research (iDiv), Leipzig, Germany  
- ³ GEOMAR Helmholtz Centre for Ocean Research Kiel, Kiel, Germany  
- ⁴ Department of Economics, Kiel University, Germany  

</details>


## Abstract


## Requirements

This project uses **Python 3.12.7** and requires the following Python packages:


```
import numpy as np
from numpy import nanmedian
import pandas as pd
import os, glob
from pathlib import Path
import gsw
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.geoaxes import GeoAxes
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER
import PyCO2SYS as pyco2
import xarray as xr
from datetime import datetime
from scipy.optimize import minimize
import matplotlib.ticker as mticker
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import earthaccess as ea
import time

```


## Data


| Dataset | File Name | Source |
|---------|-----------|--------|
| RSS CCMP Monthly 10 Meter Surface Winds | 188 nc files `CCMP_Wind_Analysis_201001_monthly_mean_V03.1_L4.nc` | [EarthData](https://podaac.jpl.nasa.gov/dataset/CCMP_WINDS_10MMONTHLY_L4_V3.1) |

| NPP Data | `cmems_nwshelf_npp_2000_2024` | [Copernicus Marine Service](https://data.marine.copernicus.eu/product/NWSHELF_MULTIYEAR_BGC_004_011/services) | 

SST and mixed layer  and bathymetry depth: https://data.marine.copernicus.eu/product/NWSHELF_MULTIYEAR_PHY_004_009/services

compare to measurments: https://www.imr.no/forskning/forskningsdata/stasjoner/index.html?utm_source=chatgpt.com
https://www.imr.no/forskning/forskningsdata/stasjoner/view/initdownload
https://www.imr.no/forskning/forskningsdata/stasjoner/view?station=Ytre+Utsira&utm_source=chatgpt.com


https://www.ncei.noaa.gov/access/ocean-carbon-acidification-data-system/oceans/Moorings/Station_M.html

## Repository Structure

```
├── code/                         
│   └── main.ipynb          
├── data/                 
│   ├── raw/
│   ├── interim/
│   └── processed/
├── img/    
└── README.md
```
## Processed Data Naming Convention


  
## License

<!-- This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. -->

