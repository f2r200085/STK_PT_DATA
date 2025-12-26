import h5py
import matplotlib.pyplot as plt
import numpy as np

"""
Datasets:
REAL_P     (N, 32) float32
REAL_T     (N, 32) float32
TARGET_P   (N, 32) float32
TARGET_T   (N, 32) float32
timestamp  (N,)    float64
"""

MAX_PLOT_POINTS = 200_000   


with h5py.File("pt_data_128.h5", "r") as f:

    N = f["timestamp"].shape[0]
    step = max(1, N // MAX_PLOT_POINTS)
    idx = slice(None, None, step)

    print("Total samples :", N)
    print("Downsample step:", step)
    print("Plot points   :", (N + step - 1) // step)

    ts = f["timestamp"][idx]                        # (N_ds,)
    rp = f["REAL_P"][idx, :]                        # (N_ds, 32)
    rt = f["REAL_T"][idx, :]
    tp = f["TARGET_P"][idx, :]
    tt = f["TARGET_T"][idx, :]


t0 = ts[0]
ts -= t0
t_rel = ts   

plt.figure(figsize=(14, 10))

# ---------- REAL P ----------
ax1 = plt.subplot(2, 2, 1)
ax1.set_title("ADC P (all data, downsampled)")
for ch in range(32):
    ax1.plot(t_rel, rp[:, ch], linewidth=0.4)
ax1.set_ylabel("Code")
ax1.grid(True)

# ---------- REAL T ----------
ax2 = plt.subplot(2, 2, 2)
ax2.set_title("ADC T (all data, downsampled)")
for ch in range(32):
    ax2.plot(t_rel, rt[:, ch], linewidth=0.4)
ax2.set_ylabel("Code")
ax2.set_xlabel("Time (s)")
ax2.grid(True)

# ---------- TARGET P ----------
ax3 = plt.subplot(2, 2, 3)
ax3.set_title("TARGET P (all data, downsampled)")
for ch in range(32):
    ax3.plot(t_rel, tp[:, ch], linewidth=0.4)
ax3.set_ylabel("Pa")
ax3.set_xlabel("Time (s)")
ax3.grid(True)

# ---------- TARGET T ----------
ax4 = plt.subplot(2, 2, 4)
ax4.set_title("TARGET T (all data, downsampled)")
for ch in range(32):
    ax4.plot(t_rel, tt[:, ch], linewidth=0.4)
ax4.set_ylabel("°C")
ax4.set_xlabel("Time (s)")
ax4.grid(True)

plt.tight_layout()
plt.show()
