#!/usr/bin/env python3
"""Supplementary Fig. 3: Slice 03 spontaneous LFP before and after TTX (0.5 uM).

    python make_supp_fig3.py                     # uses the paths below
    python make_supp_fig3.py --data-root /path/to/copy/of/"Slice - Rat"

Layout (one figure):
    A  Slice:        comb B electrode grid (8 x 4), two outlined channels
    B  Slice:        the two outlined channels overlaid, Pearson r
    C  Slice + TTX:  same grid, same outlined channels
    D  Slice + TTX:  same overlay, Pearson r

Inputs are the continuous recordings saved by baseline_concatenate_1.py,
shape (channels, samples), in uV, already 60-Hz notched, 300-Hz low-passed
and downsampled to 2 kHz. They are plotted exactly as loaded (no filtering).
Pearson r is computed over the entire displayed time series (as in the caption).

Outputs: SuppFig3.png, SuppFig3.pdf and SuppFig3_pearson.csv in OUT_DIR.
Requires Python >= 3.9, numpy, matplotlib.
"""
import argparse
import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # write files; works without a display or Spyder plots pane
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

# ============================== SETTINGS ===================================
DATA_ROOT = Path("/Volumes/PRESTIGE/Slice - Rat")
SLICE_FILE = "Slice_250604_TTX/Tissue/baseline/DIV1_250605_115015/concatenated_signal_low_pass_ds.npy"
TTX_FILE = "Slice_250604_TTX/Tissue/baseline/DIV1_3hoursafterTTX_250605_165418"  # folder or .npy
NPY_NAME = "concatenated_signal_low_pass_ds.npy"  # looked up inside a folder path
OUT_DIR = Path("figures")

FS = 2000                     # Hz
N_CHANNELS = 64
WINDOW_S = {                  # recording time shown (s); same window used for r
    "Slice": (200.0, 220.0),
    "Slice + TTX": (180.0, 200.0),
}
CHANNELS = {"orange": "B3", "blue": "B5"}   # outlined electrodes (ch 35 and 37)
GRID_YLIM_UV = (-500, 500)    # electrode grid (panels A, C)
TRACE_YLIM_UV = (-600, 600)   # overlays (panels B, D)
SCALE_BAR = (20.0, 500.0)     # (s, uV); drawn to the grid's true scale
TTX_LABEL = "Slice +\nTTX\n(0.5µM)"
# ===========================================================================

# Comb B physical layout (rows top to bottom, shanks left to right).
COMB_B = [
    ["B24", "B25", "B17", "B11"],
    ["B31", "B27", "B18", "B9"],
    ["B6", "B30", "B10", "B20"],
    ["B0", "B2", "B19", "B13"],
    ["B3", "B29", "B12", "B16"],
    ["B26", "B4", "B14", "B8"],
    ["B7", "B28", "B21", "B15"],
    ["B5", "B1", "B23", "B22"],
]
COLORS = {"orange": "#ff7f0e", "blue": "#1f77b4"}


def channel_index(label: str) -> int:
    """'A0'-'A31' -> 0-31, 'B0'-'B31' -> 32-63."""
    bank, num = label[0].upper(), int(label[1:])
    return {"A": 0, "B": 32}[bank] + num


def resolve(root: Path, rel: str) -> Path:
    p = Path(rel) if Path(rel).is_absolute() else root / rel
    if p.is_dir():
        p = p / NPY_NAME
    if not p.is_file():
        raise FileNotFoundError(f"Recording not found: {p}")
    return p


def load_window(path: Path, start_s: float, end_s: float) -> np.ndarray:
    """Memory-map a (channels, samples) recording and return the window in float64."""
    x = np.load(path, mmap_mode="r", allow_pickle=False)
    if x.ndim != 2 or x.shape[0] != N_CHANNELS:
        raise ValueError(f"{path.name}: expected ({N_CHANNELS}, samples), got {x.shape}.")
    i0, i1 = int(round(start_s * FS)), int(round(end_s * FS))
    duration = x.shape[1] / FS
    if not 0 <= i0 < i1 <= x.shape[1]:
        raise ValueError(f"{path.name}: window {start_s:g}-{end_s:g} s is outside the "
                         f"{duration:.1f} s recording.")
    w = np.asarray(x[:, i0:i1], dtype=np.float64)
    if not np.isfinite(w).all():
        raise ValueError(f"{path.name}: window contains NaN or infinite values.")
    print(f"  {path.parent.name}: {x.shape}, {duration:.1f} s; showing {start_s:g}-{end_s:g} s")
    return w


def draw_grid(fig, spec, x, t, outlined):
    """8 x 4 comb B grid; outlined = {channel index: color}. Returns axes array."""
    axes = np.empty((8, 4), dtype=object)
    sub = spec.subgridspec(8, 4, wspace=0.04, hspace=0.12)
    for r, row in enumerate(COMB_B):
        for c, lab in enumerate(row):
            ax = fig.add_subplot(sub[r, c])
            idx = channel_index(lab)
            ax.plot(t, x[idx], color="black", lw=0.5)
            ax.set(xlim=(t[0], t[-1]), ylim=GRID_YLIM_UV, xticks=[], yticks=[])
            for sp in ax.spines.values():
                sp.set_visible(idx in outlined)
                sp.set_color(outlined.get(idx, "black"))
                sp.set_linewidth(2.5)
            axes[r, c] = ax
    return axes


def draw_overlay(ax, x, t, pair, r_val):
    """Both outlined channels on one axis (blue drawn first, orange on top)."""
    for name in ("blue", "orange"):
        ax.plot(t, x[pair[name]], color=COLORS[name], lw=1.2,
                label=f"{CHANNELS[name]} (ch {pair[name]})")
    length = len(t) / FS
    ax.set(xlim=(0, length), ylim=TRACE_YLIM_UV, xlabel="Time(s)", ylabel="uV",
           xticks=np.arange(0, length + 1e-9, 2.5))
    ax.text(0.05, 0.92, f"r = {r_val:.2f}", transform=ax.transAxes, fontsize=12)


def scale_bar(fig, ref_ax, t):
    """Red L-shaped bar, to scale, placed left of the grid at the level of ref_ax."""
    pos = ref_ax.get_position()
    sb = fig.add_axes([pos.x0 - 1.15 * pos.width, pos.y0, pos.width, pos.height])
    sb.set(xlim=(t[0], t[-1]), ylim=GRID_YLIM_UV)
    sb.axis("off")
    s, uv = SCALE_BAR
    x1, y0 = t[-1], GRID_YLIM_UV[0]
    sb.plot([x1 - s, x1], [y0, y0], color="#c00000", lw=2.5, clip_on=False)
    sb.plot([x1 - s, x1 - s], [y0, y0 + uv], color="#c00000", lw=2.5, clip_on=False)
    sb.text(x1 - s, y0 + uv / 2, f"{uv:g}µV ", ha="right", va="center", fontsize=13)
    sb.text(x1 - s / 2, y0, f"{s:g}s", ha="center", va="top", fontsize=13)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Make Supplementary Fig. 3.")
    ap.add_argument("--data-root", type=Path, default=DATA_ROOT)
    ap.add_argument("--out", type=Path, default=OUT_DIR)
    args = ap.parse_args(argv)

    pair = {name: channel_index(lab) for name, lab in CHANNELS.items()}
    outlined = {idx: COLORS[name] for name, idx in pair.items()}
    files = {"Slice": resolve(args.data_root, SLICE_FILE),
             "Slice + TTX": resolve(args.data_root, TTX_FILE)}

    fig = plt.figure(figsize=(15, 12))
    outer = fig.add_gridspec(2, 2, left=0.20, right=0.98, top=0.90, bottom=0.06,
                             width_ratios=[1.0, 1.0], wspace=0.14, hspace=0.42)
    rows = []
    for r, (cond, path) in enumerate(files.items()):
        start, end = WINDOW_S[cond]
        x = load_window(path, start, end)
        t = np.arange(x.shape[1]) / FS                      # 0 to window length
        r_val = float(np.corrcoef(x[pair["orange"]], x[pair["blue"]])[0, 1])
        print(f"  {cond}: Pearson r ({CHANNELS['orange']} vs {CHANNELS['blue']}) = {r_val:.3f}")
        rows.append({"condition": cond, "file": str(path), "window_s": f"{start:g}-{end:g}",
                     "channel_orange": CHANNELS["orange"], "channel_blue": CHANNELS["blue"],
                     "n_samples": x.shape[1], "pearson_r": r_val})

        axes = draw_grid(fig, outer[r, 0], x, t, outlined)
        trace_ax = fig.add_subplot(outer[r, 1])
        draw_overlay(trace_ax, x, t, pair, r_val)

        # Row label, panel letters, column titles
        mid = (axes[0, 0].get_position().y1 + axes[7, 0].get_position().y0) / 2
        fig.text(0.115, mid, "Slice" if r == 0 else TTX_LABEL, ha="center", va="center",
                 fontsize=16, fontweight="bold")
        top = axes[0, 0].get_position().y1
        fig.text(0.04, top + 0.01, "AC"[r], fontsize=16, fontweight="bold", va="bottom")
        fig.text(outer[r, 1].get_position(fig).x0 - 0.05, top + 0.01, "BD"[r],
                 fontsize=16, fontweight="bold", va="bottom")
        if r == 0:
            scale_bar(fig, axes[2, 0], t)
            grid_mid = (axes[0, 0].get_position().x0 + axes[0, 3].get_position().x1) / 2
            fig.text(grid_mid, top + 0.025, "Spontaneous Activity", ha="center",
                     fontsize=16, fontweight="bold")
            fig.text(trace_ax.get_position().x0 + trace_ax.get_position().width / 2,
                     top + 0.025, "Time-Series", ha="center", fontsize=16, fontweight="bold")

    # Thick divider between the Slice and Slice + TTX rows
    # Divider halfway between row 1's x-axis label and row 2's panel letters
    y_div = (outer[0, 0].get_position(fig).y0 - 0.035 + outer[1, 0].get_position(fig).y1 + 0.01) / 2
    fig.add_artist(Line2D([0.04, 0.98], [y_div, y_div], color="black", lw=5))

    args.out.mkdir(parents=True, exist_ok=True)
    for ext in ("png", "pdf"):
        fig.savefig(args.out / f"SuppFig3.{ext}", dpi=300, bbox_inches="tight", facecolor="white")
    with open(args.out / "SuppFig3_pearson.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"Saved SuppFig3.png, SuppFig3.pdf and SuppFig3_pearson.csv to {args.out.resolve()}")


if __name__ == "__main__":
    main()
