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


MAX_POINTS = 200_000      
ROI_START_SEC = 100.0     
ROI_DURATION = 10.0       


with h5py.File("pt_data_128.h5", "r") as f:
    N = f["timestamp"].shape[0]
    step = max(1, N // MAX_POINTS)
    idx = slice(None, None, step)

    ts_ds = f["timestamp"][idx].astype(np.float32)
    rp_ds = f["REAL_P"][idx, :]
    rt_ds = f["REAL_T"][idx, :]
    tp_ds = f["TARGET_P"][idx, :]
    tt_ds = f["TARGET_T"][idx, :]

    ts_full = f["timestamp"][:]     
    t0 = ts_full[0]
    ts1 = f["timestamp"][-1]
    total_seconds = ts1 - t0

    roi_start = t0 + ROI_START_SEC
    roi_end   = roi_start + ROI_DURATION

    mask = (ts_full >= roi_start) & (ts_full <= roi_end)

    ts_roi = ts_full[mask].astype(np.float32)
    rp_roi = f["REAL_P"][mask, :]
    rt_roi = f["REAL_T"][mask, :]
    tp_roi = f["TARGET_P"][mask, :]
    tt_roi = f["TARGET_T"][mask, :]

print(f"Total duration: {total_seconds:.2f} seconds")
print(f"Total duration: {total_seconds/60:.2f} minutes")
print(f"Total duration: {total_seconds/3600:.2f} hours")

t_rel_ds = ts_ds - ts_ds[0]

plt.figure(figsize=(14, 10))


ax1 = plt.subplot(4, 2, 1)
ax1.set_title("ADC P - Overview (downsample)")
for ch in range(32):
    ax1.plot(t_rel_ds, rp_ds[:, ch], linewidth=0.4)
ax1.grid(True)

ax2 = plt.subplot(4, 2, 3)
ax2.set_title("ADC T - Overview (downsample)")
for ch in range(32):
    ax2.plot(t_rel_ds, rt_ds[:, ch], linewidth=0.4)
ax2.grid(True)

ax3 = plt.subplot(4, 2, 5)
ax3.set_title("TARGET P - Overview (downsample)")
for ch in range(32):
    ax3.plot(t_rel_ds, tp_ds[:, ch], linewidth=0.4)
ax3.grid(True)

ax4 = plt.subplot(4, 2, 7)
ax4.set_title("TARGET T - Overview (downsample)")
for ch in range(32):
    ax4.plot(t_rel_ds, tt_ds[:, ch], linewidth=0.4)
ax4.set_xlabel("Time (s)")
ax4.grid(True)


t_rel_roi = ts_roi - ts_roi[0]

ax5 = plt.subplot(4, 2, 2)
ax5.set_title("ADC P - ROI (raw)")
for ch in range(32):
    ax5.plot(t_rel_roi, rp_roi[:, ch], linewidth=0.8)
ax5.grid(True)

ax6 = plt.subplot(4, 2, 4)
ax6.set_title("ADC T - ROI (raw)")
for ch in range(32):
    ax6.plot(t_rel_roi, rt_roi[:, ch], linewidth=0.8)
ax6.grid(True)

ax7 = plt.subplot(4, 2, 6)
ax7.set_title("TARGET P - ROI (raw)")
for ch in range(32):
    ax7.plot(t_rel_roi, tp_roi[:, ch], linewidth=0.8)
ax7.grid(True)

ax8 = plt.subplot(4, 2, 8)
ax8.set_title("TARGET T - ROI (raw)")
for ch in range(32):
    ax8.plot(t_rel_roi, tt_roi[:, ch], linewidth=0.8)
ax8.set_xlabel("Time (s)")
ax8.grid(True)

plt.tight_layout()
plt.show()
