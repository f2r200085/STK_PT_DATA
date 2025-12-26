# STK_PT_DATA
HDF5 measurement data and a simple Python script for visualizing multi-channel time-series data (plotting only, no analysis).

# PT Data Viewer

This repository contains:

- HDF5 measurement data
- A simple Python script for visualizing the data

The script is for **plotting only** (visual inspection).  
No analysis, filtering, or data modification is performed.

---

## Data Format (HDF5)

```text
REAL_P     : (N, 32), float32
REAL_T     : (N, 32), float32
TARGET_P   : (N, 32), float32
TARGET_T   : (N, 32), float32
timestamp  : (N,),    float64   # seconds

