#!/usr/bin/env python3
"""Fig. 2: spontaneous wide-band activity across the 3D-MEA (A) and one electrode
decomposed into theta and beta (B).

    python make_fig2.py
    python make_fig2.py --recording /path/to/concatenated_signal_low_pass_ds.npy --channel B12

Outputs (PNG + PDF) in OUT_DIR:
    Fig2A_grid                      8 x 8 electrode grid, comb A | comb B, scale bar
    Fig2B_wideband / _theta / _beta  the three Fig. 2B components, separately
    Fig2B_combined                  the three components stacked, as in the figure

Input: the continuous spontaneous recording saved by baseline_concatenate_1.py,
shape (channels, samples), in uV, already 60-Hz notched, 300-Hz low-passed and
downsampled to 2 kHz. Wide-band traces are plotted exactly as loaded.

Theta (4-12 Hz) and beta (12-30 Hz) reproduce the original BP_IIR visualization
filters: fourth-order causal Butterworth (scipy iirfilter + lfilter), applied to the
whole recording of the chosen channel from its first sample, then cropped for
display. These are visualization filters, not the decoding pipeline's filter.

All scale bars are drawn to the true data scale.
Requires Python >= 3.9, numpy, scipy, matplotlib.
"""
import argparse
import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # write files; works without a display
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from scipy.signal import iirfilter, lfilter  # noqa: E402

# ============================== SETTINGS ===================================
RECORDING = "/Volumes/PRESTIGE/Slice - Rat/Slice_250521/1463A/tissue/baseline/DIV1_250522_081314/concatenated_signal_low_pass_ds.npy"           # SET: full path to concatenated_signal_low_pass_ds.npy
CHANNEL_2B = "39"          # SET: electrode shown in Fig. 2B, e.g. "B12" or 44
OUT_DIR = Path("figures")
FS = 2000                # Hz
N_CHANNELS = 64

# Fig. 2A
GRID_WINDOW_S = (200.0, 220.0)          # recording time shown in every grid panel
GRID_YLIM_UV = (-500, 500)
GRID_SCALE_BAR = (5.0, 1000.0)       # (s, uV)
IMPEDANCE_CSV = None                 # optional Intan impedance CSV: blank excluded electrodes
IMPEDANCE_QC_OHMS = (3e3, 2e6)       # keep min <= |Z| <= max
EXCLUDE_CHANNELS = ["A6","A4","A9","A10","A11","A12","A13","A14","A15","A17","A18","A19","A21","A22","A23","A30"]                # optional extra electrodes to blank, e.g. ["A12", "B7"]

# Fig. 2B
WIDE_WINDOW_S = (200.0, 220.0)          # SET to the published wide-band window
BAND_WINDOW_S = (210.0, 212.0)           # SET to the published theta/beta window
WIDE_SCALE_BAR = (5.0, 500.0)       # (s, uV)
BAND_SCALE_BAR = (0.25, 100.0)       # (s, uV) = 250 ms, 100 uV
FILTER_ORDER = 4
BANDS = {"Theta": (4.0, 12.0, "#1f77b4"), "Beta": (12.0, 30.0, "#f5a623")}
# ===========================================================================

LAYOUT = [
    ["A7", "A6", "A14", "A20", "B24", "B25", "B17", "B11"],
    ["A0", "A4", "A13", "A22", "B31", "B27", "B18", "B9"],
    ["A23", "A17", "A27", "A11", "B6", "B30", "B10", "B20"],
    ["A31", "A19", "A12", "A18", "B0", "B2", "B19", "B13"],
    ["A28", "A2", "A29", "A15", "B3", "B29", "B12", "B16"],
    ["A5", "A21", "A1", "A25", "B26", "B4", "B14", "B8"],
    ["A24", "A3", "A10", "A16", "B7", "B28", "B21", "B15"],
    ["A26", "A30", "A8", "A9", "B5", "B1", "B23", "B22"],
]
RED = "#c00000"


def channel_index(ch) -> int:
    """'A0'-'A31' -> 0-31, 'B0'-'B31' -> 32-63; integers pass through."""
    if isinstance(ch, (int, np.integer)):
        return int(ch)
    s = str(ch).strip().upper().replace("-", "")
    if s.isdigit():
        return int(s)
    return {"A": 0, "B": 32}[s[0]] + int(s[1:])


def label(idx: int) -> str:
    return ("A" if idx < 32 else "B") + str(idx % 32)


def load_recording(path: Path) -> np.ndarray:
    if not str(path) or not path.is_file():
        raise FileNotFoundError(f"Set RECORDING (or --recording); not found: '{path}'")
    x = np.load(path, mmap_mode="r", allow_pickle=False)
    if x.ndim != 2 or x.shape[0] != N_CHANNELS:
        raise ValueError(f"{path.name}: expected ({N_CHANNELS}, samples), got {x.shape}.")
    print(f"Recording: {path}\n  {x.shape}, {x.shape[1] / FS:.1f} s at {FS} Hz")
    return x


def crop(x: np.ndarray, window, what: str) -> np.ndarray:
    i0, i1 = int(round(window[0] * FS)), int(round(window[1] * FS))
    if not 0 <= i0 < i1 <= x.shape[-1]:
        raise ValueError(f"{what}: window {window[0]:g}-{window[1]:g} s is outside the "
                         f"{x.shape[-1] / FS:.1f} s recording.")
    out = np.asarray(x[..., i0:i1], dtype=np.float64)
    if not np.isfinite(out).all():
        raise ValueError(f"{what}: window contains NaN or infinite values.")
    return out


def retained_channels():
    """Electrodes shown in Fig. 2A: impedance QC (by channel ID, not row order)
    plus any EXCLUDE_CHANNELS."""
    keep = set(range(N_CHANNELS))
    if IMPEDANCE_CSV is not None:
        path = Path(IMPEDANCE_CSV)
        if path.is_dir():
            path = path / "impedance.csv"
        with open(path, newline="", encoding="utf-8-sig") as fh:
            rows = list(csv.DictReader(fh))
        cols = list(rows[0]) if rows else []
        mag = next((c for c in cols if "impedance magnitude" in c.lower()), None)
        idc = next((c for c in cols if c.lower() in ("channel number", "channel name")), None)
        if mag is None or idc is None:
            raise ValueError(f"{path.name}: need 'Channel Number' and 'Impedance Magnitude' "
                             f"columns; found {cols}")
        z = {}
        for r in rows:
            try:
                z[channel_index(r[idc])] = float(r[mag])
            except (KeyError, ValueError):
                continue
        if len(z) != N_CHANNELS:
            raise ValueError(f"{path.name}: parsed {len(z)} channels, expected {N_CHANNELS}.")
        lo, hi = IMPEDANCE_QC_OHMS
        keep = {i for i, v in z.items() if np.isfinite(v) and lo <= v <= hi}
        print(f"  impedance QC {lo / 1e3:g} kOhm - {hi / 1e6:g} MOhm from {path}")
    keep -= {channel_index(c) for c in EXCLUDE_CHANNELS}
    blank = sorted(set(range(N_CHANNELS)) - keep)
    print(f"  Fig. 2A: {len(keep)}/{N_CHANNELS} electrodes shown; blank: "
          f"{', '.join(label(i) for i in blank) or 'none'}")
    return keep


def scale_bar(ax, s, uv, corner="right", fontsize=12):
    """Red L scale bar in data units: vertical bar on the left of the horizontal bar."""
    (x0, x1), (y0, y1) = ax.get_xlim(), ax.get_ylim()
    xr = x1 if corner == "right" else x0 + s
    yb = y1 - uv
    ax.plot([xr - s, xr - s], [yb, y1], color=RED, lw=2.5, clip_on=False)
    ax.plot([xr - s, xr], [yb, yb], color=RED, lw=2.5, clip_on=False)
    v = f"{uv / 1000:g}mV" if uv >= 1000 else f"{uv:g}µV"
    h = f"{s * 1000:g}ms" if s < 1 else f"{s:g}s"
    ax.text(xr - s, yb + uv / 2, v + " ", ha="right", va="center", fontsize=fontsize)
    ax.text(xr, yb, h, ha="right", va="top", fontsize=fontsize)


def save(fig, out: Path, stem: str):
    out.mkdir(parents=True, exist_ok=True)
    for ext in ("png", "pdf"):
        fig.savefig(out / f"{stem}.{ext}", dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  saved {stem}.png/.pdf")


# --------------------------------------------------------------- Fig. 2A
def fig2a(x, out: Path):
    w = crop(x, GRID_WINDOW_S, "Fig. 2A")
    t = np.arange(w.shape[1]) / FS
    keep = retained_channels()
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(8, 9, width_ratios=[1, 1, 1, 1, 0.12, 1, 1, 1, 1],
                          left=0.10, right=0.98, top=0.92, bottom=0.12, wspace=0.05, hspace=0.15)
    axes = {}
    for r, row in enumerate(LAYOUT):
        for c, lab in enumerate(row):
            ax = fig.add_subplot(gs[r, c if c < 4 else c + 1])
            ax.set(xlim=(0, t[-1]), ylim=GRID_YLIM_UV)
            ax.axis("off")
            idx = channel_index(lab)
            if idx in keep:
                ax.plot(t, w[idx], color="black", lw=0.6)
            axes[r, c] = ax
    # Scale bar left of the grid, same scale as the panels
    p = axes[1, 0].get_position()
    sb = fig.add_axes([p.x0 - 1.1 * p.width, p.y0, p.width, p.height])
    sb.set(xlim=(0, t[-1]), ylim=GRID_YLIM_UV)
    sb.axis("off")
    scale_bar(sb, *GRID_SCALE_BAR, corner="left", fontsize=16)
    # Comb brackets and labels
    for c0, c1, name in ((0, 3, "Comb A"), (4, 7, "Comb B")):
        xa, xb = axes[7, c0].get_position().x0, axes[7, c1].get_position().x1
        y = axes[7, 0].get_position().y0 - 0.02
        xm = (xa + xb) / 2
        for xs, ys in (([xa, xa, xb, xb], [y + 0.012, y, y, y + 0.012]), ([xm, xm], [y, y - 0.015])):
            fig.add_artist(Line2D(xs, ys, color="black", lw=1.5))
        fig.text(xm, y - 0.025, name, ha="center", va="top", fontsize=18, fontweight="bold")
    fig.text(0.54, 0.95, "Wide-band Spontaneous Activity", ha="center", fontsize=30, fontweight="bold")
    save(fig, out, "Fig2A_grid")


# --------------------------------------------------------------- Fig. 2B
def band_filter(trace, lo, hi):
    """Original BP_IIR: 4rd-order causal Butterworth, iirfilter + lfilter."""
    b, a = iirfilter(FILTER_ORDER, [lo / (FS / 2), hi / (FS / 2)], btype="bandpass",
                     analog=False, ftype="butter")
    return lfilter(b, a, trace)


def draw_component(ax, t, y, color, lw, title, bar):
    ax.plot(t, y, color=color, lw=lw)
    pad = 0.08 * np.ptp(y)
    ax.set(xlim=(t[0], t[-1]), ylim=(y.min() - pad, max(y.max(), y.min() + bar[1]) + bar[1] + pad))
    ax.axis("off")
    ax.set_title(title, fontsize=18, fontweight="bold")
    scale_bar(ax, *bar)


def fig2b(x, ch: int, out: Path):
    full = np.asarray(x[ch], dtype=np.float64)       # whole recording, this channel
    if not np.isfinite(full).all():
        raise ValueError(f"channel {ch} contains NaN or infinite values.")
    wide = crop(full, WIDE_WINDOW_S, "Fig. 2B wide-band")
    t_wide = np.arange(wide.size) / FS
    comps = [("wideband", t_wide, wide, "black", 1.2, "Wide-band (0-300Hz)", WIDE_SCALE_BAR)]
    for name, (lo, hi, color) in BANDS.items():
        y = crop(band_filter(full, lo, hi), BAND_WINDOW_S, f"Fig. 2B {name}")
        comps.append((name.lower(), np.arange(y.size) / FS, y, color, 2.0,
                      f"{name} ({lo:g}-{hi:g}Hz)", BAND_SCALE_BAR))
    print(f"  Fig. 2B: {label(ch)} (ch {ch}); wide-band {WIDE_WINDOW_S[0]:g}-{WIDE_WINDOW_S[1]:g} s, "
          f"bands {BAND_WINDOW_S[0]:g}-{BAND_WINDOW_S[1]:g} s")

    for key, t, y, color, lw, title, bar in comps:            # separate components
        fig, ax = plt.subplots(figsize=(9, 2.6))
        draw_component(ax, t, y, color, lw, title, bar)
        save(fig, out, f"Fig2B_{key}")

    fig, axes = plt.subplots(3, 1, figsize=(9, 8.5), gridspec_kw={"hspace": 0.45})
    for ax, (key, t, y, color, lw, title, bar) in zip(axes, comps):
        draw_component(ax, t, y, color, lw, title, bar)
    save(fig, out, "Fig2B_combined")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Make Fig. 2A and Fig. 2B components.")
    ap.add_argument("--recording", type=Path, default=Path(RECORDING))
    ap.add_argument("--channel", default=CHANNEL_2B, help="Fig. 2B electrode, e.g. B12 or 44")
    ap.add_argument("--out", type=Path, default=OUT_DIR)
    ap.add_argument("--only", choices=("2A", "2B"))
    args = ap.parse_args(argv)

    x = load_recording(args.recording)
    if args.only in (None, "2A"):
        fig2a(x, args.out)
    if args.only in (None, "2B"):
        if str(args.channel).strip() == "":
            raise ValueError("Set CHANNEL_2B (or --channel) to the electrode shown in Fig. 2B.")
        ch = channel_index(args.channel)
        if not 0 <= ch < N_CHANNELS:
            raise ValueError(f"channel {args.channel} is outside 0-{N_CHANNELS - 1}.")
        fig2b(x, ch, args.out)
    print(f"Done: {args.out.resolve()}")


if __name__ == "__main__":
    main()
