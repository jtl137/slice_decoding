#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:26:50 2026

@author: jameslim
"""

import tkinter as tk
from tkinter import filedialog
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
import json
import scipy.signal
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300       # for on-screen display
mpl.rcParams['savefig.dpi'] = 300      # for saving figures


# In[]
import numpy as np

# Example: Replace this with your actual path
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250604_TTX/Tissue/stim/SC_DIV1_B2B6/STIM_CC5.0_PC1.0_PW0.1_PositiveFirst_PS1_CS0_IPD0.2/Outputs_LFP_zoomed/extracted_segments_LFP_Ch34.npy"

# Load the specified .npy file
try:
    extracted_segments1 = np.load(file_path)
    print("File loaded successfully.")
    print("Data shape:", extracted_segments1.shape)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"Error loading file: {e}")

# Example: Replace this with your actual path
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250604_TTX/Tissue/stim/SC_DIV1_B2B6/STIM_CC5.0_PC1.0_PW0.1_PositiveFirst_PS1_CS0_IPD0.2/Outputs_LFP_zoomed/extracted_segments_LFP_Ch38.npy"

# Load the specified .npy file
try:
    extracted_segments2 = np.load(file_path)
    print("File loaded successfully.")
    print("Data shape:", extracted_segments2.shape)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"Error loading file: {e}")

# Example: Replace this with your actual path
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250604_TTX/Tissue/stim/SC_DIV1_B2B6_TTX/STIM_CC5.0_PC1.0_PW0.1_PositiveFirst_PS1_CS0_IPD0.2/Outputs_LFP_zoomed/extracted_segments_LFP_Ch34.npy"

# Load the specified .npy file
try:
    extracted_segments_ttx1 = np.load(file_path)
    print("File loaded successfully.")
    print("Data shape:", extracted_segments_ttx1.shape)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"Error loading file: {e}")
    
# Example: Replace this with your actual path
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250604_TTX/Tissue/stim/SC_DIV1_B2B6_TTX/STIM_CC5.0_PC1.0_PW0.1_PositiveFirst_PS1_CS0_IPD0.2/Outputs_LFP_zoomed/extracted_segments_LFP_Ch35.npy"

# Load the specified .npy file
try:
    extracted_segments_ttx2 = np.load(file_path)
    print("File loaded successfully.")
    print("Data shape:", extracted_segments_ttx2.shape)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"Error loading file: {e}")

# media only1
# Example: Replace this with your actual path
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250604_TTX/before/stim/TEMP/STIM_CC5.0_PC1.0_PW0.1_PositiveFirst_PS1_CS0_IPD0.2/Outputs_LFP_zoomed/extracted_segments_LFP_Ch34.npy"
# Load the specified .npy file
try:
    extracted_segments_mediaonly1 = np.load(file_path)
    print("File loaded successfully.")
    print("Data shape:", extracted_segments_mediaonly1.shape)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"Error loading file: {e}")

# media only2
# Example: Replace this with your actual path
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250604_TTX/before/stim/TEMP/STIM_CC5.0_PC1.0_PW0.1_PositiveFirst_PS1_CS0_IPD0.2/Outputs_LFP_zoomed/extracted_segments_LFP_Ch38.npy"
# Load the specified .npy file
try:
    extracted_segments_mediaonly2 = np.load(file_path)
    print("File loaded successfully.")
    print("Data shape:", extracted_segments_mediaonly2.shape)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"Error loading file: {e}")

# Load corresponding baseline recording already concatenated
"""Notch and downsampling to 2kHz has already been done on this array"""
# Example: Replace this with your actual path
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250604_TTX/Tissue/baseline/DIV1_250605_091357/concatenated_signal_low_pass_ds.npy"
# Load the specified .npy file
try:
    baseline_activity = np.load(file_path)
    print("File loaded successfully.")
    print("Data shape:", baseline_activity.shape)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"Error loading file: {e}")
    
# Load impedance info
# Example: Replace this with your actual path
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250604_TTX/Tissue/stim/SC_DIV1_B2B6/impedance.csv"
# Load the specified .npy file
try:
    # Load the CSV file into a NumPy array
    impedance_info = np.genfromtxt(file_path, delimiter=',', skip_header=1)
    print("File loaded successfully.")
    print("Data:", impedance_info)
    print('Channels and Headers: ', impedance_info.shape)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"Error loading file: {e}")
# In[]
# ============================================================
# Supplementary Fig. 4: trial-to-trial variability (SD) across
# Media only / Slice / Slice + TTX, per channel
# ============================================================
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['savefig.dpi'] = 300

fs = 2000
STIM_T = 2.0              # stim onset within the segment (s); segments start 2 s pre-stim
WINDOW = (2.0, 5.0)       # post-stim window in s; use (0.0, 5.0) to reproduce the old figure
CHANNELS = [35, 37]       # one panel per channel
INPUT = 1                 # 1 = input A arrays, 2 = input B arrays

conds = {
    1: {"Media Only": extracted_segments_mediaonly1, "Slice": extracted_segments1, "Slice + TTX": extracted_segments_ttx1},
    2: {"Media Only": extracted_segments_mediaonly2, "Slice": extracted_segments2, "Slice + TTX": extracted_segments_ttx2},
}[INPUT]
colors = {"Media Only": "blue", "Slice": "green", "Slice + TTX": "red"}

def window_idx(win, stim_t=STIM_T, fs=fs):
    return slice(int((stim_t + win[0]) * fs), int((stim_t + win[1]) * fs))

def trial_sd(segs, ch, win):
    """SD across trials at each time point, then summarized over the window.
    segs: (trials, channels, samples). Returns mean and SD over time of the across-trial SD."""
    x = segs[:, ch, window_idx(win)]
    sd_t = x.std(axis=0, ddof=1)          # across-trial SD at each sample
    return sd_t.mean(), sd_t.std(ddof=1), x.shape[0]

fig, axes = plt.subplots(1, len(CHANNELS), figsize=(6 * len(CHANNELS), 4.5), squeeze=False)
summary = []
for k, ch in enumerate(CHANNELS):
    ax = axes[0, k]
    names = list(conds.keys())
    vals, errs, ns = zip(*[trial_sd(conds[n], ch, WINDOW) for n in names])
    ax.bar(names, vals, yerr=errs, capsize=4, color=[colors[n] for n in names],
           edgecolor="black", linewidth=2.5)
    ax.set_title(f"Channel {ch}", fontsize=12, fontweight="bold")
    ax.set_ylabel("Trial-to-trial SD (µV)", fontsize=11, fontweight="bold")
    plt.setp(ax.get_xticklabels(), fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(-0.18, 1.08, "AB"[k], transform=ax.transAxes, fontsize=22, fontweight="bold")
    for n, v, e, nt in zip(names, vals, errs, ns):
        summary.append((ch, n, v, e, nt))

fig.suptitle(f"Post-stimulus variability, Slice 03, Input {'AB'[INPUT-1]} "
             f"({WINDOW[0]:g}–{WINDOW[1]:g} s)", fontsize=13, fontweight="bold", y=1.02)
fig.tight_layout()
tag = f"{WINDOW[0]:g}-{WINDOW[1]:g}s"
fig.savefig(f"SuppFig4_SD_{tag}.png", bbox_inches="tight", facecolor="white")
fig.savefig(f"SuppFig4_SD_{tag}.pdf", bbox_inches="tight", facecolor="white")
plt.show()

for ch, n, v, e, nt in summary:
    print(f"Ch {ch} | {n:<12s} | SD = {v:6.2f} ± {e:5.2f} µV | n trials = {nt}")