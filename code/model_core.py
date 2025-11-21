from __future__ import annotations
import numpy as np
import xarray as xr
import gsw


# --- Function to compute potential density σ0 using TEOS-10 ---
def pot_density(SP, T, p_local, lon, lat):
    SA = gsw.SA_from_SP(SP, p_local, lon, lat) # Absolute Salinity [g/kg] from Practical Salinity.
    CT = gsw.CT_from_t(SA, T, p_local)         # Conservative Temp [°C]
    return gsw.sigma0(SA, CT) + 1000.0         # potential density σ0 [kg m^-3]


def schmidt_number_CO2_W14(temp_C):
    # Jähne et al. (1987) as listed in Wanninkhof (2014); dimensionless
    T = temp_C
    a, b, c, d, e = 2116.8, -136.25, 4.7353, -0.092307, 0.0007555
    return a + b*T + c*T**2 + d*T**3 + e*T**4

def k_W14_from_U2(U2, temp_C):
    """
    U2: <U^2> (m^2 s^-2) for the averaging window
    temp_C: temperature (°C) for Schmidt correction (scalar or array matching U2)
    Returns: k (in-situ) in cm hr^-1
    """
    Sc = schmidt_number_CO2_W14(temp_C)
    k = 0.251 * U2 * np.sqrt(660.0 / Sc)  # cm/hr
    return k

def K0_weiss74_CO2(temp_C, sal):
    """Weiss (1974) CO2 solubility: returns K0 in mol kg^-1 atm^-1."""
    T = temp_C + 273.15  # K
    A1, A2, A3 = -58.0931, 90.5069, 22.2940
    B1, B2, B3 = 0.027766, -0.025888, 0.0050578
    lnK0 = A1 + A2 * (100.0 / T) + A3 * np.log(T / 100.0) \
           + sal * (B1 + B2 * (T / 100.0) + B3 * (T / 100.0) ** 2)
    return np.exp(lnK0)  # mol kg^-1 atm^-1

def subset_box_0360(ds, lon_min, lon_max, lat_min, lat_max, lon_name="longitude", lat_name="latitude"):
    """Subset a 0–360° longitude grid to the desired box, 
    handling wrap-around across 0° if needed."""
    L0 = (np.asarray(lon_min) % 360 + 360) % 360
    L1 = (np.asarray(lon_max) % 360 + 360) % 360

    if L0 <= L1:
        return ds.sel({lon_name: slice(L0, L1), lat_name: slice(lat_min, lat_max)})
    else:
        # Box crosses 0° meridian: stitch two slices
        left  = ds.sel({lon_name: slice(L0, 360), lat_name: slice(lat_min, lat_max)})
        right = ds.sel({lon_name: slice(0,  L1), lat_name: slice(lat_min, lat_max)})
        return xr.concat([left, right], dim=lon_name)