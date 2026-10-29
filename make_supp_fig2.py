#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 13:20:53 2026

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
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250521/1463A/tissue/stim/SC_B5-B6_DIV2/STIM_CC5.0_PC1.0_PW0.1_PositiveFirst_PS1_CS0_IPD0.2/Outputs_LFP_zoomed/extracted_segments_LFP_Ch37.npy"

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
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250521/1463A/tissue/stim/SC_B5-B6_DIV2/STIM_CC5.0_PC1.0_PW0.1_PositiveFirst_PS1_CS0_IPD0.2/Outputs_LFP_zoomed/extracted_segments_LFP_Ch38.npy"
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
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250521/1463A/notissue/CW/TEMP/STIM_CC5.0_PC1.0_PW0.1_PositiveFirst_PS1_CS0_IPD0.2/Outputs_LFP_zoomed/extracted_segments_LFP_Ch37.npy"

# Load the specified .npy file
try:
    extracted_segments_mediaonly1 = np.load(file_path)
    print("File loaded successfully.")
    print("Data shape:", extracted_segments_mediaonly1.shape)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"Error loading file: {e}")

# Example: Replace this with your actual path
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250521/1463A/notissue/CW/TEMP/STIM_CC5.0_PC1.0_PW0.1_PositiveFirst_PS1_CS0_IPD0.2/Outputs_LFP_zoomed/extracted_segments_LFP_Ch38.npy"

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
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250521/1463A/tissue/baseline/DIV1_250522_081314/concatenated_signal_low_pass_ds.npy"
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
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250521/1463A/tissue/stim/SC_B5-B6_DIV2/impedance.csv"
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
# ============================================================
# RAW ARTIFACT TRACE + 0-2 s EXCLUSION WINDOW (Fig. 3D / Supp)
#
# Complements plot_f_segments(). Uses the same arrays:
#   extracted_segments*  -> raw wideband (0-300 Hz), [trials, channels, samples]
#   f_segments_theta*/beta* -> optional band-limited overlays
#   notissue segments    -> optional media-only overlay (same stim protocol)
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


def plot_artifact_trace(
    raw_segments,               # [trials, channels, samples], wideband 0-300 Hz
    ch,                         # channel index (same index you use in plot_f_segments)
    trial,                      # trial index (0-based)
    fs=2000,
    stim_time=2.0,              # stim onset in SEGMENT time (s) -- match plot_f_segments
    pre=2,                    # seconds shown before stim
    post=5,                   # seconds shown after stim
    excl_end=2.0,               # end of artifact exclusion window (s post-stim)
    win_end=5.0,                # end of analysis window (s post-stim)
    ylim=(-200, 200),           # main-axis y-limits (artifact will be clipped; see inset)
    relative_time=True,         # True: x-axis = time re: stim (0 = stim). False: segment time
    theta=None,                 # optional [trials, channels, samples] theta-filtered array
    beta=None,                  # optional [trials, channels, samples] beta-filtered array
    notissue_segments=None,     # optional media-only raw array [trials, channels, samples]
    notissue_trial=0,
    notissue_ch=None,           # defaults to ch
    inset=True,
    inset_ms=(-20, 5000),        # artifact zoom window in ms re: stim
    title=None,
    save_path=None,
):
    n_samples = raw_segments.shape[2]
    t_seg = np.arange(n_samples) / fs
    t_plot = t_seg - stim_time if relative_time else t_seg
    offset = 0.0 if relative_time else stim_time   # where "stim" sits on the x-axis

    # Display window
    x0, x1 = offset - pre, offset + post
    mask = (t_plot >= x0) & (t_plot <= x1)

    raw = raw_segments[trial, ch, :]
    SLICE_COLOR = 'blue'   # slice, raw
    MEDIA_COLOR = '#222222'   # media only (purple)
    fig, ax = plt.subplots(figsize=(12, 3.5))

    # ---- Shaded windows ----
    ax.axvspan(offset, offset + excl_end, color='red', alpha=0.15, zorder=0,
               label='_nolegend_')
    ax.axvspan(offset + excl_end, offset + win_end, color='#2ca02c', alpha=0.08,
               zorder=0, label='_nolegend_')

    # ---- Optional media-only overlay (plotted first, underneath) ----
    if notissue_segments is not None:
        nch = ch if notissue_ch is None else notissue_ch
        nt = notissue_segments.shape[2]
        t_nt = np.arange(nt) / fs
        t_nt_plot = t_nt - stim_time if relative_time else t_nt
        m_nt = (t_nt_plot >= x0) & (t_nt_plot <= x1)
        ax.plot(t_nt_plot[m_nt], notissue_segments[notissue_trial, nch, m_nt],
                color=MEDIA_COLOR, lw=0.5, alpha=0.9, label='Media only (no tissue)')

    # ---- Raw slice trace ----
    ax.plot(t_plot[mask], raw[mask], color=SLICE_COLOR, lw=0.4,
            label='Slice, raw (0-300 Hz)', alpha=0.8)

    # ---- Optional band overlays (same colors as Fig. 3C) ----
    if theta is not None:
        ax.plot(t_plot[mask], theta[trial, ch, mask], color='#1f77b4', lw=0.9,
                alpha=0.9, label='theta (4-12 Hz)')
    if beta is not None:
        ax.plot(t_plot[mask], beta[trial, ch, mask], color='#ff7f0e', lw=0.9,
                alpha=0.7, label='beta (12-30 Hz)')

    # ---- Stim + boundary lines ----
    ax.axvline(offset, color='black', ls='--', lw=1.5, label='STIM')
    ax.axvline(offset + excl_end, color='#cc0000', ls='--', lw=1, alpha=0.7,
               label='_nolegend_')

    # ---- Zone labels ----
    box = dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.85)
    ylo = ylim[0] + 0.1 * (ylim[1] - ylim[0])
    ax.text(offset + excl_end / 2, ylo, f'0-{excl_end:g} s excluded\n(artifact-dominated)',
            ha='center', va='bottom', fontsize=9, fontweight='bold',
            color='#cc0000', bbox=box)
    ax.text(offset + (excl_end + win_end) / 2, ylo,
            f'{excl_end:g}-{win_end:g} s analysis window',
            ha='center', va='bottom', fontsize=9, fontweight='bold',
            color='#1a7a1a', bbox=box)

    # ---- Axes formatting ----
    ax.set_xlim(x0, x1)
    ax.set_ylim(*ylim)
    ax.set_xlabel('Time relative to stimulus onset (s)' if relative_time else 'Time (s)',
                  fontsize=11)
    ax.set_ylabel('uV', fontsize=11)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend(loc='upper right', fontsize='x-small', ncol=2, frameon=False)
    ax.set_title(title or f'Raw trace, channel {ch}, trial {trial + 1}',
                 fontsize=11, fontweight='bold')


  # ---- Inset: full-scale artifact zoom (trace + scale bar only) ----
    if inset:
        axi = inset_axes(ax, width='22%', height='55%', loc='upper left',
                         bbox_to_anchor=(0.045, -0.6, 0.75, 1), bbox_transform=ax.transAxes)
        t_ms = (t_seg - stim_time) * 1000
        zm = (t_ms >= inset_ms[0]) & (t_ms <= inset_ms[1])

        if notissue_segments is not None:
            t_nt_ms = (np.arange(notissue_segments.shape[2]) / fs - stim_time) * 1000
            zn = (t_nt_ms >= inset_ms[0]) & (t_nt_ms <= inset_ms[1])
            axi.plot(t_nt_ms[zn], notissue_segments[notissue_trial, nch, zn],
                     color=MEDIA_COLOR, lw=0.6)

        axi.plot(t_ms[zm], raw[zm], color=SLICE_COLOR, lw=0.6)
        axi.axvline(0, color='black', ls='--', lw=0.8)
        axi.set_title('Artifact + Trace (full scale)', fontsize=7, fontweight='bold')

        inset_ylim = (-5000, 5000)
        axi.set_xlim(*inset_ms)
        axi.set_ylim(*inset_ylim)
        axi.axis('off')                      # no ticks, labels, or spines

        # ---- L-shaped scale bar (bottom-right corner) ----
        sb_ms = 1000                           # horizontal bar length (ms)
        sb_uv = 2000                         # vertical bar length (uV)
        x_end = inset_ms[1] - 0.05 * (inset_ms[1] - inset_ms[0])
        y_bot = inset_ylim[0] + 0.08 * (inset_ylim[1] - inset_ylim[0])

        axi.plot([x_end - sb_ms, x_end], [y_bot, y_bot], color='black', lw=1.2)   # time
        axi.plot([x_end, x_end], [y_bot, y_bot + sb_uv], color='black', lw=1.2)  # amplitude
        axi.text(x_end - sb_ms / 2, y_bot - 0.03 * (inset_ylim[1] - inset_ylim[0]),
                 f'{sb_ms} ms', ha='center', va='top', fontsize=6)
        axi.text(x_end + 0.02 * (inset_ms[1] - inset_ms[0]), y_bot + sb_uv / 2,
                 f'{sb_uv / 1000:g} mV', ha='left', va='center', fontsize=6)

    if save_path:
        fig.savefig(f'{save_path}.png', dpi=300, bbox_inches='tight', facecolor='white')
        fig.savefig(f'{save_path}.pdf', bbox_inches='tight', facecolor='white')
    plt.show()
    return fig, ax    


# ============================================================
# Example usage (run AFTER bandpass_extracted_segments cells)
# ============================================================

# In[]
if __name__ == '__main__':
    fs = 2000
    stim_time = 2          # <-- must match plot_f_segments (see note in chat)
    ch =39                 # <-- pick a representative channel near the stim site
    trial = 59             # <-- match a trial shown in Fig. 3C (e.g., Trial 35 -> index 34)

    # 3) With media-only overlay (load your notissue/removetissue segments first)
    notissue_segments = extracted_segments_mediaonly2
    plot_artifact_trace(
        extracted_segments2, ch=ch, trial=trial, fs=fs, stim_time=stim_time,
        notissue_segments=notissue_segments, notissue_trial=0,
        save_path='fig3D_artifact_trace_slice_vs_media',
    )