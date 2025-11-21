# ---- Suppress tqdm IProgress warnings globally ----
import warnings
warnings.filterwarnings("ignore", message=".*IProgress.*ipywidgets.*")
# --------------------------------------------------------


from pathlib import Path
import os
import glob
import time
import math
import sys
from datetime import datetime

import numpy as np
from numpy import nanmedian
import pandas as pd
import xarray as xr

import gsw
import PyCO2SYS as pyco2
import copernicusmarine
import earthaccess as ea

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.ticker as mticker
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.geoaxes import GeoAxes
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER

from scipy.optimize import minimize

# ------------------------------------------------------------------
# Paths (relative to project_root/)
# ------------------------------------------------------------------
ROOT = Path("..").resolve()

DATA_DIR       = ROOT / "data"
DATA_RAW       = DATA_DIR / "raw"
DATA_INTERIM   = DATA_DIR / "interim"
DATA_PROCESSED = DATA_DIR / "processed"

WIND_DIR = DATA_RAW / "wind"
NPP_DIR  = DATA_RAW / "NPP"
SST_DIR  = DATA_RAW / "SST"

IMG_DIR = ROOT / "img"

#SRC_DIR = ROOT / "src"
#if str(SRC_DIR) not in sys.path:
#    sys.path.append(str(SRC_DIR))

# ------------------------------------------------------------------
# Atomic weights in g/mol (IUPAC standard values)
# ------------------------------------------------------------------
M_Ca = 40.078     # calcium g/mol
M_O  = 15.999     # oxygen g/mol
M_H  = 1.008      # hydrogen g/mol
M_C  = 12.011     # carbon g/mol

# ------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------
rho = 1025.0                 # kg/m3, surface density 
KD = 1.5e-5                 # m^2/s   
f_remin_POC = 0.99          # frac of POC export remin in box 2
# use 365.2425 d/yr (or set to 365.0 to match your conventions)
DAYS_PER_YEAR = 365.2425
SECONDS_PER_YEAR = DAYS_PER_YEAR * 86400.0
