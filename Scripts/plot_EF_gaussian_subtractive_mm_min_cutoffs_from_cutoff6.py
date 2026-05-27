#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
import argparse

# ==========================================
# GLOBAL PLOT SETTINGS
# ==========================================
plt.rc("figure", autolayout=True)

ONE_MM = 1 / 25.4  # Convert mm to inches

plt.rc("legend", fontsize=13)
plt.rc("font", size=16)

#plt.rcParams.update({
#    'font.size': 14,
#    'axes.titlesize': 14,
#    'axes.labelsize': 14,
#    'xtick.labelsize': 14,
#    'ytick.labelsize': 14,
#    'legend.fontsize': 18
#})

# =========================
# Arguments
# =========================
parser = argparse.ArgumentParser()

parser.add_argument(
    "--input",
    required=True,
    help="Input .dat file"
)

parser.add_argument(
    "--colors",
    nargs="+",
    required=True,
    help="Colors for cutoffs in order, e.g. '#8dd3c7 #fb8072 #bebada #80b1d3'"
)

args = parser.parse_args()

# =========================
# Load data
# =========================
df = pd.read_csv(args.input, sep=r"\s+")

cutoffs = [c for c in df.columns if c != "System"]

if len(args.colors) != len(cutoffs):
    raise ValueError("Number of colors must match number of cutoff columns")

cutoff_colors = dict(zip(cutoffs, args.colors))

# =========================
# Plot settings
# =========================
x = np.arange(len(cutoffs))
bar_width = 0.35

# Figure size: 85 mm x 70 mm
fig, ax = plt.subplots(figsize=(180 * ONE_MM, 120 * ONE_MM))

systems = df["System"].values

# assume exactly two systems
if len(systems) != 2:
    raise ValueError("This script expects exactly 2 systems")

sys1, sys2 = systems

# =========================
# Plot bars
# =========================
for i, cutoff in enumerate(cutoffs):

    color = cutoff_colors[cutoff]

    # System 1 (solid)
    ax.bar(
        x[i] - bar_width / 2,
        df.loc[df["System"] == sys1, cutoff].values[0],
        width=bar_width,
        color=color,
        edgecolor='black',
        linewidth=0.6
    )

    # System 2 (hatched)
    ax.bar(
        x[i] + bar_width / 2,
        df.loc[df["System"] == sys2, cutoff].values[0],
        width=bar_width,
        color=color,
        edgecolor='black',
        hatch='///',
        linewidth=0.6
    )

# =========================
# Axis formatting
# =========================
ax.set_xticks(x)
ax.set_xticklabels(cutoffs)

#ax.set_title("Gaussian subtractive approach")
ax.set_ylabel("EF (MV/cm)")

ax.grid(
    axis='y',
    linestyle='--',
    linewidth=0.5,
    alpha=0.5
)

# =========================
# Clean legend
# =========================
legend_elements = [
    Patch(
        facecolor='white',
        edgecolor='black',
        label=sys1
    ),
    Patch(
        facecolor='white',
        edgecolor='black',
        hatch='///',
        label=sys2
    )
]

ax.legend(
    handles=legend_elements,
    loc='upper left',
    framealpha=1,
    facecolor='white',
    edgecolor='black'
)

plt.savefig('EF_gaussian_subtractive_mm_min_cutoffs_from_cutoff6.eps', format='eps')
plt.savefig('EF_gaussian_subtractive_mm_min_cutoffs_from_cutoff6.png', format='png', dpi=300)
plt.show()
