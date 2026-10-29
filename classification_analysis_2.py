#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 08:55:37 2026

@author: jameslim
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300       # for on-screen display
mpl.rcParams['savefig.dpi'] = 300      # for saving figures

# In[]
import numpy as np

# Example: Replace this with your actual path
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250409/1463A/tissue/stim/SC_5uA_DIV3/STIM_CC5.0_PC1.0_PW0.1_PositiveFirst_PS1_CS0_IPD0.2/Outputs_LFP_zoomed/extracted_segments_LFP_Ch2.npy"

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
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250409/1463A/tissue/stim/SC_5uA_DIV3/STIM_CC5.0_PC1.0_PW0.1_PositiveFirst_PS1_CS0_IPD0.2/Outputs_LFP_zoomed/extracted_segments_LFP_Ch21.npy"
# Load the specified .npy file
try:
    extracted_segments2 = np.load(file_path)
    print("File loaded successfully.")
    print("Data shape:", extracted_segments2.shape)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"Error loading file: {e}")
# Load corresponding baseline recording already concatenated
"""Notch and downsampling to 2kHz has already been done on this array"""
# Example: Replace this with your actual path
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250409/1463A/tissue/baseline/1463A_baseline_DIV3_250412_095705/concatenated_signal_low_pass_ds.npy"
# Load the specified .npy file
try:
    baseline_activity1 = np.load(file_path)
    print("File loaded successfully.")
    print("Data shape:", baseline_activity1.shape)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"Error loading file: {e}")
    
# Load impedance info
# Example: Replace this with your actual path
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250409/1463A/tissue/stim/SC_5uA_DIV3/impedance.csv"
# file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250409/1463A/notissue/SCS_ch2-21_removetissue/impedance.csv"
# Load the specified .npy file
try:
    # Load the CSV file into a NumPy array
    impedance_1 = np.genfromtxt(file_path, delimiter=',', skip_header=1)
    print("File loaded successfully.")
    print("Data:", impedance_1)
    print('Channels and Headers: ', impedance_1.shape)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"Error loading file: {e}")
# In[]
# Example: Replace this with your actual path
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250521/1463A/tissue/stim/SC_B5-B6_DIV2/STIM_CC5.0_PC1.0_PW0.1_PositiveFirst_PS1_CS0_IPD0.2/Outputs_LFP_zoomed/extracted_segments_LFP_Ch37.npy"

# Load the specified .npy file
try:
    extracted_segments3 = np.load(file_path)
    print("File loaded successfully.")
    print("Data shape:", extracted_segments3.shape)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"Error loading file: {e}")

# Example: Replace this with your actual path
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250521/1463A/tissue/stim/SC_B5-B6_DIV2/STIM_CC5.0_PC1.0_PW0.1_PositiveFirst_PS1_CS0_IPD0.2/Outputs_LFP_zoomed/extracted_segments_LFP_Ch38.npy"
# Load the specified .npy file
try:
    extracted_segments4 = np.load(file_path)
    print("File loaded successfully.")
    print("Data shape:", extracted_segments4.shape)
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
    baseline_activity2 = np.load(file_path)
    print("File loaded successfully.")
    print("Data shape:", baseline_activity2.shape)
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
    impedance_2 = np.genfromtxt(file_path, delimiter=',', skip_header=1)
    print("File loaded successfully.")
    print("Data:", impedance_2)
    print('Channels and Headers: ', impedance_2.shape)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"Error loading file: {e}")
# In[]
# Example: Replace this with your actual path
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250604_TTX/Tissue/stim/SC_DIV1_B2B6/STIM_CC5.0_PC1.0_PW0.1_PositiveFirst_PS1_CS0_IPD0.2/Outputs_LFP_zoomed/extracted_segments_LFP_Ch34.npy"

# Load the specified .npy file
try:
    extracted_segments5 = np.load(file_path)
    print("File loaded successfully.")
    print("Data shape:", extracted_segments5.shape)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"Error loading file: {e}")

# Example: Replace this with your actual path
file_path = r"/Volumes/PRESTIGE/Slice - Rat/Slice_250604_TTX/Tissue/stim/SC_DIV1_B2B6/STIM_CC5.0_PC1.0_PW0.1_PositiveFirst_PS1_CS0_IPD0.2/Outputs_LFP_zoomed/extracted_segments_LFP_Ch38.npy"

# Load the specified .npy file
try:
    extracted_segments6 = np.load(file_path)
    print("File loaded successfully.")
    print("Data shape:", extracted_segments6.shape)
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
    baseline_activity3 = np.load(file_path)
    print("File loaded successfully.")
    print("Data shape:", baseline_activity3.shape)
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
    impedance_3 = np.genfromtxt(file_path, delimiter=',', skip_header=1)
    print("File loaded successfully.")
    print("Data:", impedance_3)
    print('Channels and Headers: ', impedance_3.shape)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"Error loading file: {e}")


# In[] Exclude channels with impedance > 2 MOhm (open) or < 10 kOhm (shorted)
import numpy as np

IMPEDANCE_THRESH = 2e6   # upper cutoff: 2 MOhm
SHORT_THRESH = 1e4       # lower cutoff: 10 kOhm

def get_good_impedance_channels(impedances, phases=None,
                                hi=IMPEDANCE_THRESH, lo=SHORT_THRESH,
                                channel_names=None, verbose=True):
    """
    Return indices of channels with lo <= impedance <= hi.
    If phases are given, also flag channels with positive phase (a short signature).
    """
    z = np.asarray(impedances, dtype=float)
    too_high = z > hi
    too_low = z < lo

    if phases is not None:
        ph = np.asarray(phases, dtype=float)
        pos_phase = ph > 0
        mismatch = pos_phase & ~too_low
        if mismatch.any():
            print(f"WARNING: {mismatch.sum()} channel(s) have positive phase but |Z| >= {lo:g} Ω: "
                  f"{np.where(mismatch)[0].tolist()}")

    keep = np.where(~too_high & ~too_low)[0]

    if verbose:
        names = np.asarray(channel_names) if channel_names is not None else np.arange(len(z))
        print(f"{len(z)} channels total")
        print(f"  {too_high.sum()} excluded (> {hi/1e6:g} MΩ): {names[too_high].tolist()}")
        print(f"  {too_low.sum()} excluded as shorted (< {lo/1e3:g} kΩ): {names[too_low].tolist()}")
        print(f"  {len(keep)} channels retained")
    return keep

low_imp_chs1 = get_good_impedance_channels(
    impedance_1[:, 4],                 # magnitude at 1 kHz
    phases=impedance_1[:, 5],          # phase at 1 kHz (sanity check)
    channel_names=impedance_1[:, 1],   # channel names, for the printout
)
low_imp_chs2 = get_good_impedance_channels(
    impedance_2[:, 4],                 # magnitude at 1 kHz
    phases=impedance_2[:, 5],          # phase at 1 kHz (sanity check)
    channel_names=impedance_2[:, 1],   # channel names, for the printout
)
low_imp_chs3 = get_good_impedance_channels(
    impedance_3[:, 4],                 # magnitude at 1 kHz
    phases=impedance_3[:, 5],          # phase at 1 kHz (sanity check)
    channel_names=impedance_3[:, 1],   # channel names, for the printout
)

extracted_segments1_imp = extracted_segments1[:, low_imp_chs1, :]
extracted_segments2_imp = extracted_segments2[:, low_imp_chs1, :]
extracted_segments3_imp = extracted_segments3[:, low_imp_chs2, :]
extracted_segments4_imp = extracted_segments4[:, low_imp_chs2, :]
extracted_segments5_imp = extracted_segments5[:, low_imp_chs3, :]
extracted_segments6_imp = extracted_segments6[:, low_imp_chs3, :]
# In[]
import scipy.signal
from scipy import signal
# ========== APPLY NOTCH FILTER ==========
def apply_notch_filter(data, notch_freq, sampling_rate, quality_factor=30):
    """
    Applies a notch filter to each channel in the data array.

    Parameters:
    - data: numpy array with shape (channels, samples)
    - notch_freq: float, frequency to remove (e.g., 60 Hz)
    - sampling_rate: int, samples per second
    - quality_factor: float, controls notch width (higher = narrower)

    Returns:
    - filtered_data: numpy array with the same shape as input
    """
    b, a = signal.iirnotch(notch_freq, quality_factor, sampling_rate)
    filtered_data = np.zeros_like(data)

    for channel in range(data.shape[0]):
        signal_data = data[channel, :]
        if len(signal_data) < 3 * max(len(a), len(b)):
            raise ValueError("Signal too short for filtfilt.")
        filtered_data[channel, :] = signal.filtfilt(b, a, signal_data)

    return filtered_data

fs = 2000  # Hz

extracted_segments1_imp = apply_notch_filter(extracted_segments1_imp, 60, fs)
extracted_segments2_imp = apply_notch_filter(extracted_segments2_imp, 60, fs)
extracted_segments3_imp = apply_notch_filter(extracted_segments3_imp, 60, fs)
extracted_segments4_imp = apply_notch_filter(extracted_segments4_imp, 60, fs)
extracted_segments5_imp = apply_notch_filter(extracted_segments5_imp, 60, fs)
extracted_segments6_imp = apply_notch_filter(extracted_segments6_imp, 60, fs)
# In[]
from scipy.signal import butter, filtfilt

# Bandpass filter function
def bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype="band")
    return filtfilt(b, a, data)

lowcut=4
highcut=30
extracted_segments1_lowband = bandpass_filter(extracted_segments1_imp, lowcut, highcut, fs)
extracted_segments2_lowband = bandpass_filter(extracted_segments2_imp, lowcut, highcut, fs)
extracted_segments3_lowband = bandpass_filter(extracted_segments3_imp, lowcut, highcut, fs)
extracted_segments4_lowband = bandpass_filter(extracted_segments4_imp, lowcut, highcut, fs)
extracted_segments5_lowband = bandpass_filter(extracted_segments5_imp, lowcut, highcut, fs)
extracted_segments6_lowband = bandpass_filter(extracted_segments6_imp, lowcut, highcut, fs)
# In[] correct way to split theta and beta bins
import numpy as np
from scipy.signal import welch, butter, filtfilt

def bandpass_filter(data, lowcut, highcut, fs, order=4):
    """
    Applies a zero-phase Butterworth bandpass filter.
    Applies filter along the last axis (time).
    """
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, data, axis=-1)

def compute_psd_bins_theta_beta(signal, bin_size, start_time=2, end_time=7, fs=2000, nperseg=256):
    """
    Compute PSD features for theta (4-12 Hz) and beta (12-30 Hz) bands
    per bin, per channel, for each trial.
    
    Returns:
        psd_bins: np.array, shape [trials, bins, channels, 2] (theta, beta)
    """
    trials, channels, num_samples = signal.shape

    # Compute start and end indices
    start_idx = int(start_time * fs)
    end_idx   = int(end_time * fs)

    num_bins = (end_idx - start_idx) // bin_size

    # Output array: trials x bins x channels x 2 (theta, beta)
    psd_bins = np.zeros((trials, num_bins, channels, 2))

    for i in range(num_bins):
        start = start_idx + i * bin_size
        stop  = start_idx + (i + 1) * bin_size

        for trial in range(trials):
            for channel in range(channels):
                segment = signal[trial, channel, start:stop]

                if len(segment) == 0:
                    continue

                # Compute PSD
                freqs, psd = welch(segment, fs=fs, nperseg=nperseg)

                # Band masks
                theta_mask = (freqs >= 4) & (freqs <= 12)
                beta_mask  = (freqs > 12) & (freqs <= 30)

                # Integrate power in each band
                theta_power = np.trapz(psd[theta_mask], freqs[theta_mask])
                beta_power  = np.trapz(psd[beta_mask],  freqs[beta_mask])

                psd_bins[trial, i, channel, 0] = theta_power
                psd_bins[trial, i, channel, 1] = beta_power

    # Log-transform for stability
    psd_bins = np.log10(psd_bins + 1e-12)

    return psd_bins

# ==========================================
# Application Pipeline
# ==========================================
fs = 2000
lowcut = 4
highcut = 30

# Assuming extracted_segments1_imp ... extracted_segments8_imp are already loaded
segments_imp = {
    1: extracted_segments1_imp,
    2: extracted_segments2_imp,
    3: extracted_segments3_imp,
    4: extracted_segments4_imp,
    5: extracted_segments5_imp,
    6: extracted_segments6_imp,
}

# Dictionaries to store our final outputs
X_tb = {}
theta_psd_bins = {}
beta_psd_bins = {}
thetabeta = {}

for i in range(1, 7):
    print(f"Processing segment {i}...")
    
    # 1. Bandpass filter
    extracted_lowband = bandpass_filter(segments_imp[i], lowcut, highcut, fs)
    
    # 2. Extract unflattened PSD bins
    # (Excludes last 32 and ch13 and 15 depending on your slicing before this function)
    X_tb_unflattened = compute_psd_bins_theta_beta(
        extracted_lowband, 
        bin_size=1000, 
        start_time=4, 
        end_time=7, 
        nperseg=1000,
        fs=fs
    )
    
    X_tb[i] = X_tb_unflattened
    
    # 3. Separate Theta and Beta
    theta_unflattened = X_tb_unflattened[..., 0]
    beta_unflattened  = X_tb_unflattened[..., 1]
    
    # 4. Reshape/flatten for classifiers
    thetabeta[i]      = X_tb_unflattened.reshape(X_tb_unflattened.shape[0], -1)
    theta_psd_bins[i] = theta_unflattened.reshape(theta_unflattened.shape[0], -1)
    beta_psd_bins[i]  = beta_unflattened.reshape(beta_unflattened.shape[0], -1)

print("Feature extraction complete!")

# You can now access your flattened classifier inputs like this:
# thetabeta[1]       (equivalent to your old thetabeta1)
# theta_psd_bins[1]  (equivalent to your old theta_psd_bins1)
# beta_psd_bins[8]   (equivalent to your old beta_psd_bins8)

# In[] z-score to baseline activity recorded before experiment
import numpy as np

def make_pseudo_trials(
    baseline_activity,
    fs=2000,
    trial_duration_sec=3.0,
    drop_remainder=True
):
    """
    baseline_activity: (channels, samples)
    returns: (trials, channels, samples_per_trial)
    """
    channels, total_samples = baseline_activity.shape
    samples_per_trial = int(trial_duration_sec * fs)

    n_trials = total_samples // samples_per_trial

    if drop_remainder:
        baseline_activity = baseline_activity[:, :n_trials * samples_per_trial]

    # reshape
    baseline_trials = baseline_activity.reshape(
        channels,
        n_trials,
        samples_per_trial
    ).transpose(1, 0, 2)

    return baseline_trials

# 1. Collect your baseline activities into a dictionary
baselines = {
    1: baseline_activity1,
    2: baseline_activity2,
    3: baseline_activity3,
}

# 2. Map which extracted segment uses which baseline
segment_to_baseline_map = {
    1: 1, 2: 1,
    3: 2, 4: 2,
    5: 3, 6: 3,
}

# 3. Map each baseline to its specific low impedance channel list
impedance_channels = {
    1: low_imp_chs1,  # Applies to baseline 1 (segments 1 & 2)
    2: low_imp_chs2,  # Applies to baseline 2 (segments 3 & 4)
    3: low_imp_chs3,  # Applies to baseline 3 (segments 5 & 6)
}

# Dictionaries to store your final z-scored, flattened matrices
thetabeta_z = {}
theta_psd_bins_z = {}
beta_psd_bins_z = {}

# 4. Process each of the 4 baselines
for baseline_id in range(1, 4):
    print(f"Processing baseline {baseline_id}...")
    
    # Omit high impedance channels using the specific list for this pair
    baseline_imp = baselines[baseline_id][impedance_channels[baseline_id], :]
    
    # Make pseudo trials
    baseline_trials = make_pseudo_trials(
        baseline_imp,
        fs=2000,
        trial_duration_sec=3.0
    )
    
    # Compute baseline PSD bins
    X_baseline = compute_psd_bins_theta_beta(
        baseline_trials,
        bin_size=1000,     
        start_time=0,      # baseline starts at beginning of pseudo-trial
        end_time=3.0,      
        fs=2000,
        nperseg=1000
    )
    
    # Collapse baseline across trials to get mean and std
    baseline_mean = X_baseline.mean(axis=0)  # (bins, channels, 2)
    baseline_std  = X_baseline.std(axis=0)   # (bins, channels, 2)
    
    # 5. Apply feature-wise normalization to the corresponding segments
    # Find which segments correspond to this baseline
    segments_for_this_baseline = [seg for seg, b_id in segment_to_baseline_map.items() if b_id == baseline_id]
    
    for seg_id in segments_for_this_baseline:
        # X_tb dictionary comes from the script provided in the previous turn
        X_tb_z = (X_tb[seg_id] - baseline_mean) / baseline_std
        
        # Flatten for classifiers
        thetabeta_z[seg_id]      = X_tb_z.reshape(X_tb_z.shape[0], -1)
        theta_psd_bins_z[seg_id] = X_tb_z[..., 0].reshape(X_tb_z.shape[0], -1)
        beta_psd_bins_z[seg_id]  = X_tb_z[..., 1].reshape(X_tb_z.shape[0], -1)

print("Z-scoring complete!")

# In[]

# TEMPORAL WINDOW COMPARISON: Spontaneous vs 0-2s vs 2-5s
# Per-Slice Supplementary Grid Figure
#
# Append this to your existing pipeline AFTER z-scoring is complete.
# Requires: segments_imp, baselines, impedance_channels,
#           compute_psd_bins_theta_beta, bandpass_filter,
#           make_pseudo_trials,
#           thetabeta_z, theta_psd_bins_z, beta_psd_bins_z,
#           low_imp_chs1/2/3, segment_to_baseline_map
# ============================================================


# ---- Slice configuration ----
# UPDATE the inter-site distances with your actual values from Table 1
slice_config = [
    {
        'name': 'Slice 01',   # <-- UPDATE distance
        'seg_A': 1, 'seg_B': 2,
        'baseline_id': 1,
        'imp_channels': low_imp_chs1,
    },
    {
        'name': 'Slice 02',   # <-- UPDATE distance
        'seg_A': 3, 'seg_B': 4,
        'baseline_id': 2,
        'imp_channels': low_imp_chs2,
    },
    {
        'name': 'Slice 03',   # <-- UPDATE distance
        'seg_A': 5, 'seg_B': 6,
        'baseline_id': 3,
        'imp_channels': low_imp_chs3,
    },
]

# ============================================================
# STEP 1: Extract 0-2s post-stimulus features
# ============================================================
# Your existing pipeline extracts 2-5s (start_time=4, end_time=7).
# Stim onset is at t=2s in segment coordinates, so:
#   0-2s post-stim = segment t=2 to t=4
#   2-5s post-stim = segment t=4 to t=7 (already done)

print("=" * 60)
print("STEP 1: Extracting 0-2s post-stimulus features")
print("=" * 60)

X_tb_0to2 = {}
for i in range(1, 7):
    print(f"  Segment {i}...")
    extracted_lowband = bandpass_filter(segments_imp[i], lowcut, highcut, fs)
    X_tb_0to2[i] = compute_psd_bins_theta_beta(
        extracted_lowband,
        bin_size=1000,
        start_time=2,      # stim onset in segment coordinates
        end_time=4,         # = 0-2s post-stimulus
        nperseg=1000,
        fs=fs
    )
print("  Done.\n")

# ============================================================
# STEP 2: Z-score 0-2s features to baseline
# ============================================================
# Baseline pseudo-trials must match the 0-2s window duration (2s)
# so the bin count aligns for z-scoring.

print("=" * 60)
print("STEP 2: Z-scoring 0-2s features to baseline")
print("=" * 60)

thetabeta_0to2_z = {}
theta_0to2_z = {}
beta_0to2_z = {}

for baseline_id in range(1, 4):
    print(f"  Baseline {baseline_id}...")
    baseline_imp = baselines[baseline_id][impedance_channels[baseline_id], :]

    # 2-second pseudo-trials to match 0-2s bin structure
    baseline_trials_2s = make_pseudo_trials(
        baseline_imp, fs=2000, trial_duration_sec=2.0
    )

    X_baseline_2s = compute_psd_bins_theta_beta(
        baseline_trials_2s,
        bin_size=1000,
        start_time=0,
        end_time=2.0,
        fs=2000,
        nperseg=1000
    )

    baseline_mean_2s = X_baseline_2s.mean(axis=0)   # (bins, channels, 2)
    baseline_std_2s  = X_baseline_2s.std(axis=0)

    # Apply to corresponding segments
    segs_for_bl = [s for s, b in segment_to_baseline_map.items() if b == baseline_id]
    for seg_id in segs_for_bl:
        X_z = (X_tb_0to2[seg_id] - baseline_mean_2s) / baseline_std_2s
        thetabeta_0to2_z[seg_id] = X_z.reshape(X_z.shape[0], -1)
        theta_0to2_z[seg_id]     = X_z[..., 0].reshape(X_z.shape[0], -1)
        beta_0to2_z[seg_id]      = X_z[..., 1].reshape(X_z.shape[0], -1)

print("  Done.\n")

FS = 2000
NOTCH_FREQ = 60
NOTCH_Q = 30
LOWCUT = 4
HIGHCUT = 30
FILTER_ORDER = 4

BIN_SIZE = 1000
NPERSEG = 1000
BASELINE_DURATION = 3.0
def preprocess_baseline(data):
    """
    data: continuous baseline, shape (channels, samples)
    returns: floating-point data with the same shape

    Uses the same filter designs as the experimental pipeline.
    """
    data = np.asarray(data, dtype=np.float64)

    if data.ndim != 2:
        raise ValueError("Baseline must have shape (channels, samples).")
    if not np.isfinite(data).all():
        raise ValueError("Baseline contains NaN or infinite values.")

    # 1. Same notch filter as experimental recordings.
    b_notch, a_notch = signal.iirnotch(
        NOTCH_FREQ, NOTCH_Q, fs=FS
    )

    # 2. Same bandpass filter as experimental recordings.
    b_band, a_band = signal.butter(
        FILTER_ORDER,
        [LOWCUT, HIGHCUT],
        btype="bandpass",
        fs=FS,
    )

    required_padlen = max(
        3 * max(len(a_notch), len(b_notch)),
        3 * max(len(a_band), len(b_band)),
    )
    if data.shape[-1] <= required_padlen:
        raise ValueError("Baseline is too short for filtering.")

    filtered = signal.filtfilt(
        b_notch, a_notch, data, axis=-1
    )
    filtered = signal.filtfilt(
        b_band, a_band, filtered, axis=-1
    )

    if not np.isfinite(filtered).all():
        raise ValueError("Filtering produced nonfinite values.")

    return filtered
# ============================================================
# STEP 3: Spontaneous baseline control (fake A/B)
# ============================================================
# 3-second pseudo-trials to match the 2-5s feature dimension
# (6 bins of 1000 samples each).
# Z-scored to own stats (same normalization as real data).
# Fake A/B labels assigned by alternating index.

print("=" * 60)
print("STEP 3: Building spontaneous baseline control")
print("=" * 60)

spontaneous_features = {}

for baseline_id in range(1, 4):
    print(f"  Baseline {baseline_id}...")
    baseline_imp = preprocess_baseline(baselines[baseline_id][impedance_channels[baseline_id], :])    
    baseline_trials = make_pseudo_trials(
        baseline_imp, fs=2000, trial_duration_sec=3.0
    )

    X_baseline = compute_psd_bins_theta_beta(
        baseline_trials,
        bin_size=1000,
        start_time=0,
        end_time=3.0,
        fs=2000,
        nperseg=1000
    )

    # Z-score to own stats
    bl_mean = X_baseline.mean(axis=0)
    bl_std  = X_baseline.std(axis=0)
    X_baseline_z = (X_baseline - bl_mean) / bl_std

    # Ensure even trial count for equal A/B split
    n_bt = X_baseline_z.shape[0]
    if n_bt % 2 != 0:
        X_baseline_z = X_baseline_z[:-1]
        n_bt -= 1

    # Alternating fake A/B: even indices = A, odd = B
    idx_A = np.arange(0, n_bt, 2)
    idx_B = np.arange(1, n_bt, 2)
    spont_A = X_baseline_z[idx_A]
    spont_B = X_baseline_z[idx_B]

    spontaneous_features[baseline_id] = {
        'thetabeta_A': spont_A.reshape(spont_A.shape[0], -1),
        'thetabeta_B': spont_B.reshape(spont_B.shape[0], -1),
        'theta_A':     spont_A[..., 0].reshape(spont_A.shape[0], -1),
        'theta_B':     spont_B[..., 0].reshape(spont_B.shape[0], -1),
        'beta_A':      spont_A[..., 1].reshape(spont_A.shape[0], -1),
        'beta_B':      spont_B[..., 1].reshape(spont_B.shape[0], -1),
    }

    print(f"    {len(idx_A)} pseudo-trials per class "
          f"(from {n_bt} total baseline trials)")

print("  Done.\n")

# In[]
# ============================================================
# SUPPLEMENTARY: Effective feature count + permutation testing
# per slice. Uses the same AB-pair grouping
# and the same LR
# ============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.base import clone
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import GroupKFold, permutation_test_score

N_PERM   = 1000
SCORING  = "accuracy"          # matches "CV Mean Accuracy" in your grid; "roc_auc" also works
RS       = 42
N_SPLITS = 5
PERM_WINDOWS = ['Spontaneous', '0-2 s', '2-5 s']   # trim to ['2-5 s'] for a fast run
FIG_FEAT, FIG_WIN = 'Theta + Beta', '2-5 s'          # what goes in the figure
C_REPORT = 0.01   # strongest C in the regularization supp figure, where accuracy is unchanged
# ---------- helpers ----------
def build_ab_dataset(X1, X2, block_size=2):
    
    n = min(len(X1), len(X2))
    X = np.vstack((X1[:n], X2[:n]))
    y = np.r_[np.zeros(n, int), np.ones(n, int)]
    b = np.arange(n) // (block_size // 2)
    return X, y, np.r_[b, b]

def get_features(slc, feat, win):
    """Same selection logic as STEP 4."""
    a, b, bl = slc['seg_A'], slc['seg_B'], slc['baseline_id']
    key = {'Theta': 'theta', 'Beta': 'beta', 'Theta + Beta': 'thetabeta'}[feat]
    if win == 'Spontaneous':
        sf = spontaneous_features[bl]
        return sf[f'{key}_A'], sf[f'{key}_B']
    src = {
        '0-2 s': {'Theta': theta_0to2_z, 'Beta': beta_0to2_z, 'Theta + Beta': thetabeta_0to2_z},
        '2-5 s': {'Theta': theta_psd_bins_z, 'Beta': beta_psd_bins_z, 'Theta + Beta': thetabeta_z},
    }[win][feat]
    return src[a], src[b]

def logistic_effective_df(Xs, y, C):
    """
    Effective degrees of freedom of L2 logistic regression.
    sklearn objective: C*sum(loss) + 0.5*||w||^2  ->  penalty lambda = 1/C.
      upper : uses max logistic weight p(1-p)=0.25 -> conservative upper bound
      fitted: uses fitted weights (can understate df if data are near-separable)
    """
    d = np.linalg.svd(Xs, compute_uv=False)
    df_upper = np.sum(0.25 * d**2 / (0.25 * d**2 + 1.0 / C))

    lr = LogisticRegression(C=C, max_iter=5000).fit(Xs, y)
    p = lr.predict_proba(Xs)[:, 1]
    s = np.linalg.svd(Xs * np.sqrt(np.clip(p * (1 - p), 1e-10, None))[:, None], compute_uv=False)
    df_fitted = np.sum(s**2 / (s**2 + 1.0 / C))
    return float(df_upper), float(df_fitted)

def effective_dimensionality(X, y, groups):
    Xs = StandardScaler().fit_transform(X)
    splits = list(GroupKFold(n_splits=N_SPLITS).split(Xs, y, groups))

    # PCA-based
    pca = PCA().fit(Xs)
    cum = np.cumsum(pca.explained_variance_ratio_)
    ev = pca.explained_variance_
    out = {
        'n_trials': X.shape[0], 'n_features': X.shape[1],
        'PCA_n90': int(np.searchsorted(cum, 0.90) + 1),
        'PCA_n95': int(np.searchsorted(cum, 0.95) + 1),
        'Participation_ratio': float(ev.sum()**2 / (ev**2).sum()),
    }

    # Effective df at the C actually used in the main figure
    out['C_report'] = C_REPORT
    out['df_upper'], out['df_fitted'] = logistic_effective_df(Xs, y, C_REPORT)


    return out
# In[]
# ============================================================
# UNIFIED RUN: single source of truth for Tables 2-4 + Supp 5-7
# One config, one fold set per condition, one null per condition.
# Resumable: nulls are cached to disk; rerunning skips finished ones.
# ============================================================
import os, json, numpy as np, pandas as pd, sklearn
from sklearn.base import clone
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import GroupKFold, cross_validate, cross_val_predict, cross_val_score, permutation_test_score
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# ---------- the ONE config ----------
SEED, N_SPLITS, N_PERM, BLOCK = 42, 5, 1000, 2
C_MAIN = 0.01          # used for LR + linear SVM everywhere, incl. effective df
C_SWEEP = [0.01, 0.1, 1, 10, 100]
C_REPORT = C_MAIN      # so effective_dimensionality() reports df for the model you actually report
OUT = "/Volumes/PRESTIGE/Slice - Rat/manuscript_BMES/unified_run_261015"
os.makedirs(f"{OUT}/nulls", exist_ok=True)
json.dump(dict(seed=SEED, n_splits=N_SPLITS, n_perm=N_PERM, block_size=BLOCK, C_main=C_MAIN,
               cv="GroupKFold (AB pairs, no shuffle)", permutation="within-pair label swap",
               svm_kernel="linear", sklearn=sklearn.__version__),
          open(f"{OUT}/config.json", "w"), indent=2)

def make_pipe(clf):
    return Pipeline([("vt", VarianceThreshold(1e-12)), ("sc", StandardScaler()), ("clf", clf)])

CLASSIFIERS = {
    "LR":  LogisticRegression(C=C_MAIN, max_iter=5000, random_state=SEED),
    "SVM": SVC(kernel="linear", C=C_MAIN),
    "LDA": LinearDiscriminantAnalysis(),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "RF":  RandomForestClassifier(n_estimators=100, random_state=SEED, n_jobs=1),
}

feature_set_names = ['Theta', 'Beta', 'Theta + Beta']
window_names      = ['Spontaneous', '0-2 s', '2-5 s']

# Nested dict: results[slice][feature_set][window] = {clf: (mean, std)}

rows, cms, eff_rows, sweep_rows = [], [], [], []
for slc in slice_config:
    for feat in feature_set_names:
        for win in window_names:
            X1, X2 = get_features(slc, feat, win)
            X, y, g = build_ab_dataset(X1, X2, BLOCK)
            assert np.isfinite(X).all(), f"NaN/inf: {slc['name']} {feat} {win}"
            splits = list(GroupKFold(n_splits=N_SPLITS).split(X, y, g))   # ONE fold set for this condition

            # effective dimensionality (descriptive, at C_MAIN)
            eff_rows.append({"Slice": slc["name"], "Features": feat, "Window": win,
                             **effective_dimensionality(X, y, g)})

            for name, clf in CLASSIFIERS.items():
                pipe = make_pipe(clone(clf))
                cv = cross_validate(pipe, X, y, cv=splits, scoring=["accuracy", "roc_auc"])
                yhat = cross_val_predict(pipe, X, y, cv=splits)            # out-of-fold, all trials
                obs = cv["test_accuracy"].mean()

                tag = f"{slc['name']}_{feat}_{win}_{name}".replace(" ", "").replace("+", "")
                null_path = f"{OUT}/nulls/{tag}.npy"
                if os.path.exists(null_path):
                    null = np.load(null_path)
                else:
                    score, null, _ = permutation_test_score(
                        pipe, X, y, groups=g, cv=splits, scoring="accuracy",
                        n_permutations=N_PERM, random_state=SEED, n_jobs=-1)
                    assert np.isclose(score, obs), f"observed mismatch {tag}: {score} vs {obs}"
                    np.save(null_path, null)
                p = (np.sum(null >= obs) + 1) / (N_PERM + 1)

                rep = classification_report(y, yhat, output_dict=True, zero_division=0)
                cm = confusion_matrix(y, yhat, normalize="true")
                rows.append(dict(Slice=slc["name"], Features=feat, Window=win, Classifier=name,
                                 n_trials=len(y), n_features=X.shape[1],
                                 CV_Acc=obs, CV_Acc_SD=cv["test_accuracy"].std(ddof=1),
                                 CV_AUC=cv["test_roc_auc"].mean(), CV_AUC_SD=cv["test_roc_auc"].std(ddof=1),
                                 Recall_A=rep["0"]["recall"], Recall_B=rep["1"]["recall"],
                                 Macro_F1=rep["macro avg"]["f1-score"],
                                 Null_Mean=null.mean(), Null_SD=null.std(ddof=1),
                                 Null_95th=np.percentile(null, 95), p=p, N_perm=N_PERM))
                cms.append(dict(Slice=slc["name"], Features=feat, Window=win, Classifier=name,
                                TN=cm[0, 0], FP=cm[0, 1], FN=cm[1, 0], TP=cm[1, 1]))

            # Supp 5: regularization sweep on the SAME folds (2-5 s only)
            if win == "2-5 s":
                for C in C_SWEEP:
                    for name, est in {"LR": LogisticRegression(C=C, max_iter=5000, random_state=SEED),
                                      "SVM": SVC(kernel="linear", C=C)}.items():
                        s = cross_val_score(make_pipe(est), X, y, cv=splits)
                        sweep_rows.append(dict(Slice=slc["name"], Features=feat, Classifier=name,
                                               C=C, CV_Acc=s.mean(), CV_Acc_SD=s.std(ddof=1)))
            print(f"{slc['name']:>9s} | {feat:>12s} | {win:>11s} | done")

res   = pd.DataFrame(rows);       res.to_csv(f"{OUT}/results_all.csv", index=False)
cm_df = pd.DataFrame(cms);        cm_df.to_csv(f"{OUT}/confusion_oof.csv", index=False)
eff   = pd.DataFrame(eff_rows);   eff.to_csv(f"{OUT}/effective_dim.csv", index=False)
sweep = pd.DataFrame(sweep_rows); sweep.to_csv(f"{OUT}/C_sweep.csv", index=False)

# ---------- manuscript tables, all sliced from the same CSV ----------
main = res[res.Window == "2-5 s"]
main[["Slice","Features","Classifier","CV_Acc","CV_Acc_SD","CV_AUC","CV_AUC_SD","Recall_A","Recall_B","Macro_F1"]] \
    .to_csv(f"{OUT}/Table2_CV_performance.csv", index=False)
cm_df[cm_df.Window == "2-5 s"].to_csv(f"{OUT}/Table3_confusion_OOF.csv", index=False)
main[["Slice","Features","Classifier","CV_Acc","Null_Mean","Null_SD","p","N_perm"]] \
    .to_csv(f"{OUT}/Table4_permutation.csv", index=False)
print(main.pivot_table(index=["Slice","Classifier"], columns="Features", values="CV_Acc").round(3))

# Supp 7 grid: rebuild the dict your STEP 5 plotting code expects, then run STEP 5 unchanged
results = {}
for r in res.itertuples():
    results.setdefault(r.Slice, {}).setdefault(r.Features, {}).setdefault(r.Window, {})[r.Classifier] = (r.CV_Acc, r.CV_Acc_SD)
classifiers = CLASSIFIERS   # STEP 5 reads clf names from here

# Supp 6B: load the cached nulls instead of re-permuting
perm_results = {}
for slc in slice_config:
    tag = f"{slc['name']}_ThetaBeta_2-5s_LR".replace(" ", "")
    r = res[(res.Slice == slc["name"]) & (res.Features == "Theta + Beta") & (res.Window == "2-5 s") & (res.Classifier == "LR")].iloc[0]
    perm_results[(slc["name"], "Theta + Beta", "2-5 s")] = {"score": r.CV_Acc, "null": np.load(f"{OUT}/nulls/{tag}.npy"), "p": r.p}
eff_df = eff   # Supp 6A plotting code reads eff_df
# In[]# In[]
import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['savefig.dpi'] = 300

# --- point at the unified run (same OUT as the analysis cell) ---
OUT = "/Volumes/PRESTIGE/Slice - Rat/manuscript_BMES/unified_run_261015"
out_dir = os.path.join(OUT, "per_slice_plots")
os.makedirs(out_dir, exist_ok=True)

res = pd.read_csv(os.path.join(OUT, "results_all.csv"))
main = res[res["Window"] == "2-5 s"].copy()          # analysis window only

# --- fixed orders so every figure matches the tables ---
conditions  = ["Theta", "Beta", "Theta + Beta"]
classifiers = ["LR", "SVM", "LDA", "KNN", "RF"]
slices      = ["Slice 01", "Slice 02", "Slice 03"]
colors = dict(zip(classifiers, sns.color_palette("Set2", len(classifiers))))
ALPHA = 0.05

# sanity: exactly one row per slice x feature x classifier
dup = main.groupby(["Slice", "Features", "Classifier"]).size()
assert (dup == 1).all(), f"Duplicate rows:\n{dup[dup != 1]}"

def stars(p):
    return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < ALPHA else ""

def plot_panel(ax, sdf, metric, err_col, title, mark_sig=False):
    n = len(classifiers)
    width = 0.8 / n
    x = np.arange(len(conditions))
    for i, clf in enumerate(classifiers):
        vals, errs, ps = [], [], []
        for cond in conditions:
            row = sdf[(sdf["Features"] == cond) & (sdf["Classifier"] == clf)]
            vals.append(row[metric].iloc[0] if len(row) else np.nan)
            errs.append(row[err_col].iloc[0] if len(row) else 0)
            ps.append(row["p"].iloc[0] if len(row) else np.nan)
        xpos = x + i * width
        ax.bar(xpos, vals, width, yerr=errs, capsize=3, label=clf,
               color=colors[clf], edgecolor="white", linewidth=0.5)
        if mark_sig:   # permutation p from the same run (accuracy only)
            for xp, v, e, p in zip(xpos, vals, errs, ps):
                if np.isfinite(p) and stars(p):
                    ax.text(xp, v + e + 0.01, stars(p), ha="center", va="bottom", fontsize=9)
    ax.set_xticks(x + width * (n - 1) / 2)
    ax.set_xticklabels(conditions, fontsize=12, fontweight="bold")
    ax.set_ylim(0, 1.08)
    ax.axhline(0.5, color="k", linestyle="--", linewidth=1, label="Chance")
    ax.tick_params(axis="y", labelsize=12)
    plt.setp(ax.get_yticklabels(), fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(title, fontsize=15, fontweight="bold")

# --- one figure per slice: CV accuracy (with permutation stars) + CV AUC ---
for s in slices:
    sdf = main[main["Slice"] == s]
    fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)
    plot_panel(axes[0], sdf, "CV_Acc", "CV_Acc_SD", "CV Accuracy", mark_sig=True)
    plot_panel(axes[1], sdf, "CV_AUC", "CV_AUC_SD", "CV AUC")
    axes[0].set_ylabel("Score", fontsize=14, fontweight="bold")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="center right", frameon=False, fontsize=11)
    fig.suptitle(f"{s}: Classifier Performance (2–5 s)", fontsize=18, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 0.87, 0.95])
    fig.savefig(os.path.join(out_dir, f"{s.replace(' ', '')}_classifier_performance.png"), dpi=300)
    fig.savefig(os.path.join(out_dir, f"{s.replace(' ', '')}_classifier_performance.pdf"))
    plt.show()

# --- overview grid (candidate Fig. 4A/C): one row per slice, no pooling ---
fig, axes = plt.subplots(len(slices), 2, figsize=(14, 4 * len(slices)), sharey=True, squeeze=False)
for r, s in enumerate(slices):
    sdf = main[main["Slice"] == s]
    plot_panel(axes[r, 0], sdf, "CV_Acc", "CV_Acc_SD", f"{s}: CV Accuracy", mark_sig=True)
    plot_panel(axes[r, 1], sdf, "CV_AUC", "CV_AUC_SD", f"{s}: CV AUC")
    axes[r, 0].set_ylabel("Score", fontsize=13, fontweight="bold")
handles, labels = axes[0, 0].get_legend_handles_labels()
fig.legend(handles, labels, loc="center right", frameon=False, fontsize=11)
fig.tight_layout(rect=[0, 0, 0.87, 1])
fig.savefig(os.path.join(out_dir, "all_slices_grid.png"), dpi=300)
fig.savefig(os.path.join(out_dir, "all_slices_grid.pdf"))
plt.show()

# In[]
import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['savefig.dpi'] = 300

OUT = "/Volumes/PRESTIGE/Slice - Rat/manuscript_BMES/unified_run_261015"
out_dir = os.path.join(OUT, "per_slice_plots")
os.makedirs(out_dir, exist_ok=True)

cm_df = pd.read_csv(os.path.join(OUT, "confusion_oof.csv"))
res   = pd.read_csv(os.path.join(OUT, "results_all.csv"))
cm_df = cm_df[cm_df["Window"] == "2-5 s"]
res   = res[res["Window"] == "2-5 s"]

slices      = ["Slice 01", "Slice 02", "Slice 03"]
classifiers = ["LR", "SVM", "LDA", "KNN", "RF"]
labels      = ["Input A", "Input B"]

def get_cm(slc, feat, clf):
    r = cm_df[(cm_df.Slice == slc) & (cm_df.Features == feat) & (cm_df.Classifier == clf)]
    assert len(r) == 1, f"expected 1 row for {slc}/{feat}/{clf}, got {len(r)}"
    r = r.iloc[0]
    return np.array([[r.TN, r.FP], [r.FN, r.TP]])   # rows = true A/B, cols = predicted A/B

def get_meta(slc, feat, clf):
    r = res[(res.Slice == slc) & (res.Features == feat) & (res.Classifier == clf)].iloc[0]
    return int(r.n_trials // 2), r.CV_Acc

def draw_cm(
    ax, cm, title,
    show_ylabel=True,
    show_xlabel=True,
    cbar=False,
    cbar_ax=None,
    class_labels=("Class 0", "Class 1"),  # replace with actual class names
):
    cm = np.asarray(cm, dtype=float)

    if cm.shape != (2, 2):
        raise ValueError(f"Expected a 2×2 confusion matrix, got {cm.shape}")

    if not np.isfinite(cm).all() or (cm < 0).any():
        raise ValueError("Confusion matrix must contain finite, nonnegative values")

    # Assumes rows = true classes, columns = predicted classes.
    # Works for counts or an already row-normalized matrix.
    row_totals = cm.sum(axis=1, keepdims=True)
    if (row_totals == 0).any():
        raise ValueError("Cannot normalize a class with no observations")

    proportions = cm / row_totals

    sns.heatmap(
        proportions,
        ax=ax,
        annot=True,
        fmt=".2f",
        cmap="Blues",
        vmin=0,
        vmax=1,
        square=True,
        linewidths=0.5,
        linecolor="white",
        xticklabels=class_labels,
        yticklabels=class_labels,
        cbar=cbar,
        cbar_ax=cbar_ax,
        annot_kws={"fontsize": 12, "fontweight": "bold"},
    )

    # Prevent stray ticks from expanding the matrix's visible bounds.
    ax.set_xlim(0, 2)
    ax.set_ylim(2, 0)
    ax.tick_params(axis="both", length=0)
    ax.set_xticklabels(class_labels, rotation=0)
    ax.set_yticklabels(class_labels, rotation=0)

    ax.set_title(title, fontweight="bold")
    ax.set_ylabel("True" if show_ylabel else "")
    ax.set_xlabel("Predicted" if show_xlabel else "")

# ============================================================
# Fig. 4B: one model, one matrix per slice (no pooling)
# ============================================================
FEAT, CLF = "Theta + Beta", "LR"   # must match the caption

fig = plt.figure(figsize=(4.8, 11))
gs = fig.add_gridspec(3, 2, width_ratios=[1, 0.06], hspace=0.45, wspace=0.15)
axes = [fig.add_subplot(gs[i, 0]) for i in range(3)]
cax = fig.add_subplot(gs[:, 1])          # one colorbar spanning all three rows

for i, s in enumerate(slices):
    n_per, acc = get_meta(s, FEAT, CLF)
    draw_cm(axes[i], get_cm(s, FEAT, CLF),
            f"{s} (acc = {acc:.2f}, n = {n_per}/class)",
            show_ylabel=True,
            show_xlabel=(i == len(slices) - 1),   # "Predicted" only on the bottom panel
            cbar=(i == 0), cbar_ax=cax if i == 0 else None)

cax.set_ylabel("Proportion of true class", fontsize=10)
fig.suptitle(f"{CLF}, {FEAT}\n(2–5 s, out-of-fold)", fontsize=13, fontweight="bold", y=0.95)
fig.savefig(os.path.join(out_dir, f"Fig4B_confusion_{CLF}_{FEAT.replace(' + ', '')}_vertical.png"), bbox_inches="tight")
fig.savefig(os.path.join(out_dir, f"Fig4B_confusion_{CLF}_{FEAT.replace(' + ', '')}_vertical.pdf"), bbox_inches="tight")
plt.show()
# ============================================================
# Supplementary: all classifiers x slices for one feature set
# (makes class bias visible, as the reviewer asked)
# ============================================================
for FEAT in ["Theta", "Beta", "Theta + Beta"]:
    fig, axes = plt.subplots(len(slices), len(classifiers),
                             figsize=(3.0 * len(classifiers), 3.0 * len(slices)))
    for r, s in enumerate(slices):
        for c, clf in enumerate(classifiers):
            n_per, acc = get_meta(s, FEAT, clf)
            draw_cm(axes[r, c], get_cm(s, FEAT, clf),
                    f"{s} | {clf}\nacc = {acc:.2f}",
                    show_ylabel=(c == 0), show_xlabel=(r == len(slices) - 1))
    fig.suptitle(f"Out-of-fold confusion matrices: {FEAT} (2–5 s)", fontsize=15, fontweight="bold", y=1.01)
    fig.tight_layout()
    fig.savefig(os.path.join(out_dir, f"Supp_confusion_grid_{FEAT.replace(' + ', '')}.png"), bbox_inches="tight")
    plt.show()

# ============================================================
# Quick class-bias table for the Results sentence
# ============================================================
bias = cm_df.assign(Recall_A=cm_df.TN, Recall_B=cm_df.TP,
                    Bias=(cm_df.TP - cm_df.TN).round(2))
print(bias.loc[bias.Bias.abs() >= 0.20,
               ["Slice", "Features", "Classifier", "Recall_A", "Recall_B", "Bias"]]
      .sort_values("Bias", key=abs, ascending=False).to_string(index=False))

# In[] Manuscript Figure 4
# ============================================================
# Fig. 4: (A) per-slice CV accuracy + AUC, (B) per-slice LR confusion matrix
# One row per slice, three independent preparations, no pooling
# ============================================================
FEAT, CLF = "Theta + Beta", "LR"   # confusion-matrix model; must match the caption

fig = plt.figure(figsize=(18, 4.3 * len(slices)))
gs = fig.add_gridspec(len(slices), 4, width_ratios=[1.6, 1.6, 0.95, 0.05],
                      wspace=0.32, hspace=0.55)

bar_axes = []
for r, s in enumerate(slices):
    sdf = main[main["Slice"] == s]

    # --- A: accuracy + AUC bars ---
    ax_acc = fig.add_subplot(gs[r, 0])
    ax_auc = fig.add_subplot(gs[r, 1], sharey=ax_acc)
    plot_panel(ax_acc, sdf, "CV_Acc", "CV_Acc_SD", f"{s}: CV Accuracy", mark_sig=True)
    plot_panel(ax_auc, sdf, "CV_AUC", "CV_AUC_SD", f"{s}: CV AUC")
    ax_acc.set_ylabel("Score", fontsize=13, fontweight="bold")
    plt.setp(ax_auc.get_yticklabels(), visible=False)
    bar_axes.append(ax_acc)

    # --- B: confusion matrix for the primary model ---
    ax_cm = fig.add_subplot(gs[r, 2])
    n_per, acc = get_meta(s, FEAT, CLF)
    draw_cm(ax_cm, get_cm(s, FEAT, CLF),
            f"{s}: {CLF}\n(acc = {acc:.2f}, n = {n_per}/class)",
            show_ylabel=True, show_xlabel=(r == len(slices) - 1),
            cbar=(r == 0), cbar_ax=fig.add_subplot(gs[:, 3]) if r == 0 else None)

# colorbar label (the spanning cbar axis is the last one added in row 0)
cbar_ax = [a for a in fig.axes if a.get_subplotspec().colspan.start == 3][0]
cbar_ax.set_ylabel("Proportion of true class", fontsize=11)

# panel letters
fig.text(0.075, 0.965, "A", fontsize=22, fontweight="bold")
fig.text(0.665, 0.965, "B", fontsize=22, fontweight="bold")

# one shared legend for the bar panels
handles, labels = bar_axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc="upper center", ncol=len(labels),
           frameon=False, fontsize=11, bbox_to_anchor=(0.4, 1.0))

fig.subplots_adjust(top=0.92, bottom=0.07, left=0.08, right=0.95)
fig.savefig(os.path.join(out_dir, "Fig4_per_slice_A_bars_B_confusion.png"), dpi=300, bbox_inches="tight")
fig.savefig(os.path.join(out_dir, "Fig4_per_slice_A_bars_B_confusion.pdf"), bbox_inches="tight")
plt.show()

# In[] Supplementary Fig 6

import os, json
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['savefig.dpi'] = 300

OUT = "/Volumes/PRESTIGE/Slice - Rat/manuscript_BMES/unified_run_261015"
out_dir = os.path.join(OUT, "per_slice_plots")
os.makedirs(out_dir, exist_ok=True)

cfg  = json.load(open(os.path.join(OUT, "config.json")))
eff  = pd.read_csv(os.path.join(OUT, "effective_dim.csv"))
res  = pd.read_csv(os.path.join(OUT, "results_all.csv"))
N_PERM, C_MAIN = cfg["n_perm"], cfg["C_main"]

slices   = ["Slice 01", "Slice 02", "Slice 03"]
features = ["Theta", "Beta", "Theta + Beta"]
WIN, FIG_FEAT, FIG_CLF = "2-5 s", "Theta + Beta", "LR"

def null_tag(slc, feat, win, clf):   # same tag format as the unified run
    return f"{slc}_{feat}_{win}_{clf}".replace(" ", "").replace("+", "")

# sanity: effective df was computed at the reported C
assert np.allclose(eff["C_report"], C_MAIN), "effective df not computed at C_MAIN; rerun with C_REPORT = C_MAIN"

fig, axes = plt.subplots(2, 3, figsize=(15, 9), gridspec_kw={"hspace": 0.45})

# ================= A: effective dimensionality =================
metrics = [("n_features", "Raw features",            "#bdbdbd"),
           ("PCA_n95",    "PCs (95% variance)",      "#92c5de"),
           ("df_upper",   f"LR effective df (C = {C_MAIN:g})", "#2166ac")]
w = 0.25
for c, feat in enumerate(features):
    ax = axes[0, c]
    sub = eff[(eff.Features == feat) & (eff.Window == WIN)].set_index("Slice").loc[slices].reset_index()
    x = np.arange(len(sub))
    for j, (col, lab, colr) in enumerate(metrics):
        ax.bar(x + (j - 1) * w, sub[col], w, color=colr, label=lab if c == 0 else None)
    for xi, n in zip(x, sub.n_trials):
        ax.hlines(n, xi - 1.6 * w, xi + 1.6 * w, colors="k", linestyles="--", lw=1.3,
                  label="Trials per slice" if (c == 0 and xi == 0) else None)
    ax.set_xticks(x); ax.set_xticklabels(sub.Slice, fontsize=10)
    ax.set_ylim(0,800)
    ax.set_title(f"{feat} ({WIN})", fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
axes[0, 0].set_ylabel("Dimensionality", fontsize=11)
axes[0, 0].legend(frameon=False, fontsize=8, loc="upper left")
axes[0, 0].text(-0.2, 1.1, "A", transform=axes[0, 0].transAxes, fontsize=18, fontweight="bold")

# ================= B: permutation nulls (same run as Table 4) =================
p_floor = 1 / (N_PERM + 1)
for c, s in enumerate(slices):
    ax = axes[1, c]
    row  = res[(res.Slice == s) & (res.Features == FIG_FEAT) & (res.Window == WIN) & (res.Classifier == FIG_CLF)].iloc[0]
    null = np.load(os.path.join(OUT, "nulls", null_tag(s, FIG_FEAT, WIN, FIG_CLF) + ".npy"))
    assert len(null) == N_PERM

    ax.hist(null, bins=40, color="#bdbdbd", edgecolor="white", label="Permutation null" if c == 0 else None)
    ax.axvline(row.Null_95th, color="k", ls="--", lw=1, label="Null 95th pct" if c == 0 else None)
    ax.axvline(row.CV_Acc, color="#d6604d", lw=2.5, label="Observed" if c == 0 else None)
    ptxt = f"p ≤ {p_floor:.3f}" if row.p <= p_floor + 1e-12 else f"p = {row.p:.3f}"
    ax.annotate(f"Observed = {row.CV_Acc:.2f}\n{ptxt}", xy=(row.CV_Acc, 0.95),
                xycoords=("data", "axes fraction"), xytext=(-6, 0), textcoords="offset points",
                ha="right", va="top", fontsize=10)
    ax.set_xlim(min(null.min(), 0.35) - 0.02, max(row.CV_Acc, null.max()) + 0.04)
    ax.set_ylim(0,100)
    ax.set_title(s, fontweight="bold")
    ax.set_xlabel(f"CV accuracy ({FIG_CLF}, {FIG_FEAT}, {WIN})", fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)
axes[1, 0].set_ylabel("Count", fontsize=11)
axes[1, 0].legend(frameon=False, fontsize=8, loc="upper left")
axes[1, 0].text(-0.2, 1.1, "B", transform=axes[1, 0].transAxes, fontsize=18, fontweight="bold")

fig.savefig(os.path.join(out_dir, "SuppFig6_effective_dim_permutation.png"), bbox_inches="tight", facecolor="white")
fig.savefig(os.path.join(out_dir, "SuppFig6_effective_dim_permutation.pdf"), bbox_inches="tight", facecolor="white")
plt.show()

# numbers for the caption
print(eff[eff.Window == WIN][["Slice", "Features", "n_features", "PCA_n95", "df_upper"]].round(1).to_string(index=False))

# In[] Supplementary Fig. 7
import os, json
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['savefig.dpi'] = 300

OUT = "/Volumes/PRESTIGE/Slice - Rat/manuscript_BMES/unified_run_261015"
out_dir = os.path.join(OUT, "per_slice_plots")
os.makedirs(out_dir, exist_ok=True)

res = pd.read_csv(os.path.join(OUT, "results_all.csv"))
cfg = json.load(open(os.path.join(OUT, "config.json")))

slices      = ["Slice 01", "Slice 02", "Slice 03"]
features    = ["Theta", "Beta", "Theta + Beta"]
windows     = ["Spontaneous", "0-2 s", "2-5 s"]
win_labels  = {"Spontaneous": "Spontaneous\n(pseudo A/B)", "0-2 s": "0–2 s\n(artifact)", "2-5 s": "2–5 s\n(analysis)"}
classifiers = ["LR", "SVM", "LDA", "KNN", "RF"]
colors = dict(zip(classifiers, sns.color_palette("Set2", len(classifiers))))   # same colors as Fig. 4

# sanity: one row per slice x feature x window x classifier
dup = res.groupby(["Slice", "Features", "Window", "Classifier"]).size()
assert (dup == 1).all(), f"Duplicates:\n{dup[dup != 1]}"
missing = set(windows) - set(res.Window)
assert not missing, f"Windows missing from results_all.csv: {missing}"

def stars(p):
    return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""

n_clf = len(classifiers)
bw = 0.14
gap = 0.25
group_w = n_clf * bw

fig, axes = plt.subplots(len(slices), len(features), figsize=(16, 13), sharey=True)

for r, s in enumerate(slices):
    for c, feat in enumerate(features):
        ax = axes[r, c]
        sub = res[(res.Slice == s) & (res.Features == feat)]
        for j, clf in enumerate(classifiers):
            for i, win in enumerate(windows):
                row = sub[(sub.Window == win) & (sub.Classifier == clf)].iloc[0]
                x = i * (group_w + gap) + j * bw
                ax.bar(x, row.CV_Acc, bw, yerr=row.CV_Acc_SD, color=colors[clf],
                       edgecolor="white", linewidth=0.5, capsize=2, error_kw={"linewidth": 0.8},
                       label=clf if (r == 0 and c == 0 and i == 0) else None)
                st = stars(row.p)
                if st:
                    ax.text(x, row.CV_Acc + row.CV_Acc_SD + 0.01, st, ha="center", va="bottom",
                            fontsize=12, rotation=90)
        ax.axhline(0.5, color="#333333", ls="--", lw=1, alpha=0.7, zorder=0)
        centers = [i * (group_w + gap) + group_w / 2 - bw / 2 for i in range(len(windows))]
        ax.set_xticks(centers)
        ax.set_xticklabels([win_labels[w] for w in windows], fontsize=9)
        ax.set_ylim(0.3, 1.12)
        ax.spines[["top", "right"]].set_visible(False)
        if r == 0:
            ax.set_title(feat, fontsize=13, fontweight="bold", pad=10)
        if c == 0:
            ax.set_ylabel("CV accuracy", fontsize=11)
            n_sp = int(sub[sub.Window == "Spontaneous"].n_trials.iloc[0])
            n_st = int(sub[sub.Window == "2-5 s"].n_trials.iloc[0])
            ax.annotate(f"{s}\n(n = {n_st} stim / {n_sp} spont.)", xy=(-0.32, 0.5),
                        xycoords="axes fraction", fontsize=11, fontweight="bold",
                        rotation=90, ha="center", va="center")

fig.legend(loc="upper center", ncol=n_clf, frameon=False, fontsize=11,
           bbox_to_anchor=(0.5, 1.0), title="Classifier",
           title_fontproperties={"weight": "bold", "size": 11})
fig.tight_layout(rect=[0.03, 0, 1, 0.95], h_pad=3, w_pad=2)
fig.savefig(os.path.join(out_dir, "SuppFig7_temporal_windows.png"), bbox_inches="tight", facecolor="white")
fig.savefig(os.path.join(out_dir, "SuppFig7_temporal_windows.pdf"), bbox_inches="tight", facecolor="white")
plt.show()

# numbers for the caption / Results sentence
print(res.pivot_table(index=["Slice", "Window"], columns="Classifier", values="CV_Acc")
         .loc[:, classifiers].round(2))
print("\nSignificant (p<0.05) per slice x window:")
print(res.assign(sig=res.p < 0.05).groupby(["Slice", "Window"]).sig.sum().unstack())
# In[]
# ============================================================
# Supp. Fig. 5 (C sweep) and Supp. Fig. 8 (inter-site distance)
# Source: unified run outputs only (C_sweep.csv, results_all.csv)
# ============================================================
import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['savefig.dpi'] = 300

OUT = "/Volumes/PRESTIGE/Slice - Rat/manuscript_BMES/unified_run_261015"
out_dir = os.path.join(OUT, "per_slice_plots")
os.makedirs(out_dir, exist_ok=True)

sweep = pd.read_csv(os.path.join(OUT, "C_sweep.csv"))
res   = pd.read_csv(os.path.join(OUT, "results_all.csv"))
main  = res[res.Window == "2-5 s"]

slices      = ["Slice 01", "Slice 02", "Slice 03"]
features    = ["Theta", "Beta", "Theta + Beta"]
classifiers = ["LR", "SVM", "LDA", "KNN", "RF"]
slice_colors = dict(zip(slices, sns.color_palette("tab10", 3)))
feat_style = {"Theta": ("#ff7f0e", "s"), "Beta": ("#1f77b4", "o"), "Theta + Beta": ("#2ca02c", "D")}
C_MAIN = 0.01

# ---------- sanity: sweep at C_MAIN must equal the reported model ----------
for s in slices:
    for f in features:
        for clf in ["LR", "SVM"]:
            sw = sweep[(sweep.Slice == s) & (sweep.Features == f) & (sweep.Classifier == clf) & np.isclose(sweep.C, C_MAIN)]
            rp = main[(main.Slice == s) & (main.Features == f) & (main.Classifier == clf)]
            assert len(sw) == 1 and len(rp) == 1, f"missing row {s}/{f}/{clf}"
            assert np.isclose(sw.CV_Acc.iloc[0], rp.CV_Acc.iloc[0]), \
                f"C sweep at C={C_MAIN} ({sw.CV_Acc.iloc[0]:.3f}) != reported ({rp.CV_Acc.iloc[0]:.3f}) for {s}/{f}/{clf}"
print("C sweep matches reported model at C = 0.01")

# ============================================================
# Supp. Fig. 5: accuracy vs C, one panel per feature set
# ============================================================
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5), sharey=True)
for ax, f in zip(axes, features):
    for s in slices:
        for clf, ls, mk in [("LR", "-", "o"), ("SVM", "--", "x")]:
            d = sweep[(sweep.Slice == s) & (sweep.Features == f) & (sweep.Classifier == clf)].sort_values("C")
            ax.errorbar(d.C, d.CV_Acc, yerr=d.CV_Acc_SD, color=slice_colors[s], ls=ls, marker=mk,
                        capsize=2, lw=1.5, ms=5, label=f"{s}, {clf}")
    ax.axvline(C_MAIN, color="grey", ls=":", lw=1)
    ax.axhline(0.5, color="k", ls="--", lw=0.8)
    ax.set_xscale("log")
    ax.set_xticks(sorted(sweep.C.unique()))
    ax.set_title(f"{f} (2–5 s)", fontweight="bold")
    ax.set_xlabel("Regularization strength C", fontweight="bold")
    ax.set_ylim(0.4, 1.0)
    ax.spines[["top", "right"]].set_visible(False)
axes[0].set_ylabel("CV accuracy", fontweight="bold")
axes[0].text(C_MAIN * 1.15, 0.42, "reported\nC = 0.01", fontsize=8, color="grey")
h, l = axes[0].get_legend_handles_labels()
fig.legend(h, l, loc="center right", frameon=False, fontsize=9)
fig.tight_layout(rect=[0, 0, 0.86, 1])
fig.savefig(os.path.join(out_dir, "SuppFig5_C_sweep.png"), bbox_inches="tight", facecolor="white")
fig.savefig(os.path.join(out_dir, "SuppFig5_C_sweep.pdf"), bbox_inches="tight", facecolor="white")
plt.show()

# ============================================================
# Supp. Fig. 8: accuracy vs inter-stimulation-site distance (exploratory, n = 3)
# ============================================================
DIST = {"Slice 01": 150, "Slice 02": 750, "Slice 03": 427}   # Table 1, in-plane stim-to-stim (µm)
fig, axes = plt.subplots(1, 5, figsize=(20, 4.3), sharey=True)
stats_rows = []
for ax, clf in zip(axes, classifiers):
    txt = []
    for f in features:
        d = main[(main.Classifier == clf) & (main.Features == f)].copy()
        d["dist"] = d.Slice.map(DIST)
        d = d.sort_values("dist")
        col, mk = feat_style[f]
        ax.errorbar(d.dist, d.CV_Acc, yerr=d.CV_Acc_SD, color=col, marker=mk, ls="none",
                    capsize=3, ms=7, mec="k", label=f)
        r, p = pearsonr(d.dist, d.CV_Acc)
        stats_rows.append(dict(Classifier=clf, Features=f, r=r, p=p))
        txt.append(f"{f}: r = {r:.2f}, p = {p:.2f}")
    ax.axhline(0.5, color="red", ls="--", lw=1)
    ax.set_xticks([150, 427, 750])
    ax.set_xticklabels(["150\n(S01)", "427\n(S03)", "750\n(S02)"], fontsize=9)
    ax.set_xlim(80, 820)
    ax.set_ylim(0.3, 1.05)
    ax.set_title(clf, fontweight="bold")
    ax.set_xlabel("Inter-stimulation-site distance (µm)", fontsize=10)
    ax.text(0.03, 0.97, "\n".join(txt), transform=ax.transAxes, fontsize=7, va="top",
            bbox=dict(boxstyle="round", fc="white", alpha=0.85))
    ax.spines[["top", "right"]].set_visible(False)
axes[0].set_ylabel("CV accuracy (2–5 s)", fontweight="bold")
axes[0].legend(loc="lower right", frameon=False, fontsize=8)
fig.suptitle("Exploratory: decoding accuracy vs inter-stimulation-site distance (n = 3 slices)",
             fontsize=16, fontweight="bold", y=1.03)
fig.tight_layout()
fig.savefig(os.path.join(out_dir, "SuppFig8_intersite_distance.png"), bbox_inches="tight", facecolor="white")
fig.savefig(os.path.join(out_dir, "SuppFig8_intersite_distance.pdf"), bbox_inches="tight", facecolor="white")
plt.show()

stats = pd.DataFrame(stats_rows)
stats.to_csv(os.path.join(OUT, "SuppFig8_pearson.csv"), index=False)
print(stats.round(3).to_string(index=False))

# In[] FIGURE 5 SHAP Feature Importance
import numpy as np
from scipy import signal

# Match the existing experimental preprocessing exactly.
FS = 2000
NOTCH_FREQ = 60
NOTCH_Q = 30
LOWCUT = 4
HIGHCUT = 30
FILTER_ORDER = 4

BIN_SIZE = 1000
NPERSEG = 1000
BASELINE_DURATION = 3.0





# Outputs used by your existing classifier and SHAP code.
thetabeta_z = {}
theta_psd_bins_z = {}
beta_psd_bins_z = {}
X_tb_unflattened_z = {}

# Retain these for inspection or later reuse.
baseline_features = {}
baseline_stats = {}

for baseline_id, raw_baseline in baselines.items():
    print(f"Processing baseline {baseline_id}...")

    # Must match experimental channel selection AND ordering.
    baseline_imp = np.asarray(raw_baseline)[
        impedance_channels[baseline_id], :
    ]

    # Filter continuous baseline once, before making pseudo-trials.
    baseline_filtered = preprocess_baseline(baseline_imp)

    samples_per_trial = int(BASELINE_DURATION * FS)
    n_trials = baseline_filtered.shape[-1] // samples_per_trial

    if n_trials < 2:
        raise ValueError(
            f"Baseline {baseline_id}: need at least two complete "
            f"{BASELINE_DURATION}-second pseudo-trials."
        )

    baseline_trials = make_pseudo_trials(
        baseline_filtered,
        fs=FS,
        trial_duration_sec=BASELINE_DURATION,
        drop_remainder=True,
    )

    # Same PSD settings and log transform as experimental features.
    # The existing function already performs log10(power + 1e-12).
    X_baseline = compute_psd_bins_theta_beta(
        baseline_trials,
        bin_size=BIN_SIZE,
        start_time=0,
        end_time=BASELINE_DURATION,
        fs=FS,
        nperseg=NPERSEG,
    )

    baseline_mean = X_baseline.mean(axis=0)
    baseline_std = X_baseline.std(axis=0, ddof=0)

    # Fail explicitly rather than silently creating invalid z-scores.
    if (
        not np.isfinite(X_baseline).all()
        or np.any(baseline_std <= 1e-12)
    ):
        raise ValueError(
            f"Baseline {baseline_id}: nonfinite features or "
            "zero/near-zero feature variance. Inspect the baseline."
        )

    baseline_features[baseline_id] = X_baseline
    baseline_stats[baseline_id] = {
        "mean": baseline_mean,
        "std": baseline_std,
    }

    paired_segments = [
        seg_id
        for seg_id, b_id in segment_to_baseline_map.items()
        if b_id == baseline_id
    ]

    for seg_id in paired_segments:
        X = np.asarray(X_tb[seg_id], dtype=np.float64)

        if X.shape[1:] != baseline_mean.shape:
            raise ValueError(
                f"Segment {seg_id}: feature shape {X.shape[1:]} "
                f"does not match baseline {baseline_mean.shape}."
            )
        if not np.isfinite(X).all():
            raise ValueError(
                f"Segment {seg_id}: nonfinite experimental features."
            )

        X_z = (X - baseline_mean) / baseline_std

        X_tb_unflattened_z[seg_id] = X_z
        thetabeta_z[seg_id] = X_z.reshape(X_z.shape[0], -1)
        theta_psd_bins_z[seg_id] = X_z[..., 0].reshape(
            X_z.shape[0], -1
        )
        beta_psd_bins_z[seg_id] = X_z[..., 1].reshape(
            X_z.shape[0], -1
        )

print("Baseline preprocessing and z-scoring complete.")

# ==========================================
# COMPUTE SHAP IMPORTANCE FOR ALL DATASETS
# ==========================================
import shap
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

def flatten_features(X):
    """
    X: (trials, bins, channels, bands)
    Returns: X_flat, shape
    """
    shape = X.shape[1:]
    X_flat = X.reshape(X.shape[0], -1)
    return X_flat, shape

def shap_feature_importance(X, y, background_size=100):
    X_flat, shape = flatten_features(X)

    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000, C=0.01))
    model.fit(X_flat, y)

    # Background samples for SHAP
    background = shap.sample(X_flat, background_size)
    explainer = shap.KernelExplainer(model.predict_proba, background)

    shap_values = explainer.shap_values(X_flat, silent=True)
    if shap_values.ndim == 3:
        shap_vals = shap_values[:, :, 1]   # select class 1
    else:
        shap_vals = shap_values

    importance_flat = np.mean(np.abs(shap_vals), axis=0)
    importance = importance_flat.reshape(shape)

    return importance

# Group unflattened datasets into your 3 experiments
pairs_for_shap = {
    1: (X_tb_unflattened_z[1], X_tb_unflattened_z[2]), # Slice 1 (A2 vs A21)
    2: (X_tb_unflattened_z[3], X_tb_unflattened_z[4]), # Slice 2 (B5 vs B6)
    3: (X_tb_unflattened_z[5], X_tb_unflattened_z[6])  # Slice 3 (B2 vs B6)
}

datasets_shap = []

for pair_idx, (X_A, X_B) in pairs_for_shap.items():
    print(f"\nComputing SHAP for Dataset {pair_idx}...")
    
    # Combine Stim A and Stim B trials for this dataset
    X_combined = np.concatenate([X_A, X_B], axis=0)
    y_combined = np.concatenate([np.zeros(X_A.shape[0]), np.ones(X_B.shape[0])])
    
    # Generate SHAP array of shape (bins, channels, bands)
    shap_imp = shap_feature_importance(X_combined, y_combined, background_size=100)
    datasets_shap.append(shap_imp)

print("\nSHAP extraction complete for all datasets!")

# ==========================================
# 1. SETUP REAL GEOMETRY
# ==========================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

layout = [
    ['A7', 'A6', 'A14', 'A20', 'B24', 'B25', 'B17', 'B11'],
    ['A0', 'A4', 'A13', 'A22', 'B31', 'B27', 'B18', 'B9'],
    ['A23', 'A17', 'A27', 'A11', 'B6', 'B30', 'B10', 'B20'],
    ['A31', 'A19', 'A12', 'A18', 'B0', 'B2', 'B19', 'B13'],
    ['A28', 'A2', 'A29', 'A15', 'B3', 'B29', 'B12', 'B16'],
    ['A5', 'A21', 'A1', 'A25', 'B26', 'B4', 'B14', 'B8'],
    ['A24', 'A3', 'A10', 'A16', 'B7', 'B28', 'B21', 'B15'],
    ['A26', 'A30', 'A8', 'A9', 'B5', 'B1', 'B23', 'B22']
]

# Map the layout labels to the 0-63 hardware indices
channel_map = {}
for r in range(8):
    for c in range(8):
        lbl = layout[r][c]
        if lbl.startswith('A'):
            channel_map[lbl] = int(lbl[1:])
        elif lbl.startswith('B'):
            channel_map[lbl] = 32 + int(lbl[1:])

def build_physical_coords_3d(layout):
    coords = {}
    for r in range(8):
        for c in range(8):
            label = layout[r][c]
            z_pos = r * 150
            x_pos = c * 400 if c <= 3 else (c - 4) * 400
            y_pos = 0 if c <= 3 else 400
            coords[label] = (x_pos, y_pos, z_pos)
    return coords

coords = build_physical_coords_3d(layout)

# ==========================================
# PREPARE POOLED DATA WITH IMPEDANCE MASKS
# ==========================================
experiment_stims = [['A2', 'A21'], ['B5', 'B6'], ['B2', 'B6']]
impedance_masks = [low_imp_chs1, low_imp_chs2, low_imp_chs3]

distances, peak_shaps_theta, peak_shaps_beta, dataset_ids = [], [], [], []

for i, (shap_matrix, stim_lbls, good_chs) in enumerate(zip(datasets_shap, experiment_stims, impedance_masks)):
    good_chs_list = list(good_chs)
    
    ds_distances = []
    ds_peak_shaps_theta = []
    ds_peak_shaps_beta = []
    
    for ch_lbl, hw_idx in channel_map.items():
        if hw_idx not in good_chs_list:
            continue
            
        shap_ch_idx = good_chs_list.index(hw_idx)
        curr_x, curr_y, curr_z = coords[ch_lbl]
        
        dists = []
        for s in stim_lbls:
            sx, sy, sz = coords[s]
            dists.append(np.linalg.norm(np.array([curr_x, curr_y, curr_z]) - np.array([sx, sy, sz])))
        
        ds_distances.append(np.min(dists))
        
        # Extract both Theta (0) and Beta (1) peaks independently
        ds_peak_shaps_theta.append(np.max(shap_matrix[:, shap_ch_idx, 0])) 
        ds_peak_shaps_beta.append(np.max(shap_matrix[:, shap_ch_idx, 1])) 

    # Normalize Theta and Beta independently within this dataset
    ds_peak_shaps_theta_norm = np.array(ds_peak_shaps_theta) / np.max(ds_peak_shaps_theta)
    ds_peak_shaps_beta_norm = np.array(ds_peak_shaps_beta) / np.max(ds_peak_shaps_beta)
    
    distances.extend(ds_distances)
    peak_shaps_theta.extend(ds_peak_shaps_theta_norm)
    peak_shaps_beta.extend(ds_peak_shaps_beta_norm)
    dataset_ids.extend([f"Slice 0{i+1}"] * len(ds_distances))

df_spatial = pd.DataFrame({
    'Distance': distances, 
    'Theta Peak SHAP': peak_shaps_theta, 
    'Beta Peak SHAP': peak_shaps_beta, 
    'Dataset': dataset_ids
})

# ==========================================
# 3. PLOT THE 3-PANEL REBUTTAL FIGURE
# ==========================================
# Increased width from 11 to 15 to comfortably fit 3 columns
fig = plt.figure(figsize=(15, 6))
# 3 rows, 3 columns
gs = fig.add_gridspec(3, 3, width_ratios=[1, 1.2, 1.2], hspace=0.4, wspace=0.25)

# --- PANEL A: 3x1 Vertical Heatmaps ---
axes_A = [fig.add_subplot(gs[i, 0]) for i in range(3)]

for i, ds_shap in enumerate(datasets_shap):
    time_band_data = np.mean(ds_shap, axis=1) 
    time_band_data_norm = time_band_data / np.max(time_band_data)
    
    imA = axes_A[i].imshow(time_band_data_norm.T, aspect='auto', origin='lower', 
                           cmap='viridis', vmin=0, vmax=1)
    
    if i == 1:
        axes_A[i].set_ylabel("Freq Band (0=Theta, 1=Beta)", fontweight='bold')
        
    axes_A[i].set_yticks([0, 1])
    axes_A[i].set_title(f"Slice 0{i+1}", fontweight='bold', fontsize=10)
    
    if i == 2:
        axes_A[i].set_xlabel("Time Bins", fontweight='bold')
    else:
        axes_A[i].set_xticks([])

axes_A[0].text(0.5, 1.35, "A. Temporal Dynamics", transform=axes_A[0].transAxes, 
               ha='center', va='bottom', fontweight='bold', fontsize=12)

fig.colorbar(imA, ax=axes_A, orientation='horizontal', label='Normalized Mean SHAP', 
             shrink=0.8, pad=0.12, aspect=30)

# --- PANEL B: Spatial Feature Decay (Theta) ---
ax_B = fig.add_subplot(gs[:, 1]) 
sns.regplot(data=df_spatial, x='Distance', y='Theta Peak SHAP', ax=ax_B,
            scatter=False, line_kws={'color': 'black', 'linewidth': 3}, lowess=True)
sns.scatterplot(data=df_spatial, x='Distance', y='Theta Peak SHAP', hue='Dataset', 
                ax=ax_B, alpha=0.7, s=50, palette='Set1', legend=False)

ax_B.set_title("B. Spatial Feature Decay (Theta)", fontweight='bold', fontsize=12)
ax_B.set_xlabel("3D Distance from Stimulus ($\mu$m)", fontweight='bold')
ax_B.set_ylabel("Normalized Peak SHAP", fontweight='bold')
ax_B.grid(True, linestyle='--', alpha=0.5)

# --- PANEL C: Spatial Feature Decay (Beta) ---
ax_C = fig.add_subplot(gs[:, 2]) 
sns.regplot(data=df_spatial, x='Distance', y='Beta Peak SHAP', ax=ax_C,
            scatter=False, line_kws={'color': 'black', 'linewidth': 3}, lowess=True)
sns.scatterplot(data=df_spatial, x='Distance', y='Beta Peak SHAP', hue='Dataset', 
                ax=ax_C, alpha=0.7, s=50, palette='Set1')

ax_C.set_title("C. Spatial Feature Decay (Beta)", fontweight='bold', fontsize=12)
ax_C.set_xlabel("3D Distance from Stimulus ($\mu$m)", fontweight='bold')
ax_C.set_ylabel("Normalized Peak SHAP", fontweight='bold')
ax_C.grid(True, linestyle='--', alpha=0.5)

# Move legend outside the plot for Panel C
ax_C.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()