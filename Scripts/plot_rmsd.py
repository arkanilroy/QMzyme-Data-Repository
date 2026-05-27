import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

plt.rcParams.update({
    'font.size': 16,
    'axes.titlesize': 16,
    'axes.labelsize': 16,
    'xtick.labelsize': 16,
    'ytick.labelsize': 16,
    'legend.fontsize': 16,
    'legend.title_fontsize': 16,
})
# ==========================================
# LOAD DATA
# ==========================================
# If using Excel:
df = pd.read_excel("mm_min_xstal_rmsd.xlsx", index_col=0)

# ==========================================
# CUTOFF COLORS
# ==========================================
cutoff_colors = {
    "cutoff3": "#8dd3c7",
    "cutoff4": "#fb8072",
    "cutoff5": "#bebada",
    "cutoff6": "#80b1d3",
    "cutoff7": "#ffffb3",
    "cutoff8": "#fdb462",
}

# ==========================================
# RESIDUE SHAPES
# ==========================================
marker_styles = {
    "Y16": "p",        # pentagon
    "D40": "s",        # square
    "Ash103": "o",     # o
}

# ==========================================
# GROUP DEFINITIONS
# ==========================================
groups = {
    "mm_min_xtb": [
        "mm_min_cutoff3xtb",
        "mm_min_cutoff4xtb",
        "mm_min_cutoff5xtb",
        "mm_min_cutoff6xtb",
    ],

    "mm_min_dft": [
        "mm_min_cutoff3dft",
        "mm_min_cutoff4dft",
        "mm_min_cutoff5dft",
    ],

    "mm_min_nowat_xtb": [
        "mm_min_cutoff3_nowat_xtb",
        "mm_min_cutoff4_nowat_xtb",
        "mm_min_cutoff5_nowat_xtb",
        "mm_min_cutoff6_nowat_xtb",
    ],

    "mm_min_nowat_dft": [
        "mm_min_cutoff3_nowat_dft",
        "mm_min_cutoff4_nowat_dft",
        "mm_min_cutoff5_nowat_dft",
        "mm_min_cutoff6_nowat_dft",
    ],

    "xstal_xtb": [
        "xstal_cutoff3_xtb",
        "xstal_cutoff4_xtb",
        "xstal_cutoff5_xtb",
        "xstal_cutoff6_xtb",
        "xstal_cutoff7_xtb",
        "xstal_cutoff8_xtb",
    ],

    "xstal_dft": [
        "xstal_cutoff3_dft",
        "xstal_cutoff4_dft",
        "xstal_cutoff5_dft",
        "xstal_cutoff6_dft",
        "xstal_cutoff7_dft",
        "xstal_cutoff8_dft",
    ],
}

# ==========================================
# RESIDUES TO PLOT
# ==========================================
residues = ["Y16", "D40", "Ash103"]

# ==========================================
# PLOT
# ==========================================
fig, ax = plt.subplots(figsize=(18, 8))

group_spacing = 2.5
point_spacing = 0.25

x_ticks = []
x_labels = []

current_x = 0

# ==========================================
# LOOP OVER GROUPS
# ==========================================
for group_name, columns in groups.items():

    ncols = len(columns)

    offsets = np.linspace(
        -point_spacing * (ncols - 1) / 2,
        point_spacing * (ncols - 1) / 2,
        ncols
    )

    for i, col in enumerate(columns):

        if col not in df.columns:
            print(f"Missing column: {col}")
            continue

        xpos = current_x + offsets[i]

        # determine cutoff
        cutoff = None
        for c in cutoff_colors.keys():
            if c in col:
                cutoff = c
                break

        color = cutoff_colors[cutoff]

        # plot each residue
        for residue in residues:

            yval = df.loc[residue, col]

            ax.scatter(
                xpos,
                yval,
                marker=marker_styles[residue],
                s=180,
                color=color,
                edgecolors='black',
                linewidths=1.2,
                zorder=5
            )

    x_ticks.append(current_x)
    x_labels.append(group_name)

    current_x += group_spacing

# ==========================================
# AXIS FORMATTING
# ==========================================
ax.set_xticks(x_ticks)
ax.set_xticklabels(
    x_labels,
    rotation=0,
    fontsize=16
)

ax.set_ylabel("RMSD ($\AA$)", fontsize=16)
#ax.set_title("Residue RMSD Comparison", fontsize=16)

# ==========================================
# CUTOFF LEGEND
# ==========================================
cutoff_handles = []

for cutoff, color in cutoff_colors.items():

    handle = Line2D(
        [0],
        [0],
        marker='o',
        color='w',
        markerfacecolor=color,
        markeredgecolor='black',
        markersize=10,
        linestyle=''
    )

    cutoff_handles.append(handle)

legend1 = ax.legend(
    cutoff_handles,
    cutoff_colors.keys(),
    title="Cutoffs",
    loc='upper left',
    bbox_to_anchor=(1.02, 1.0),
    borderaxespad=0
)

ax.add_artist(legend1)

# ==========================================
# RESIDUE LEGEND
# ==========================================
residue_handles = []

for residue, marker in marker_styles.items():

    handle = Line2D(
        [0],
        [0],
        marker=marker,
        color='black',
        linestyle='',
        markersize=10
    )

    residue_handles.append(handle)

legend2 = ax.legend(
    residue_handles,
    marker_styles.keys(),
    title="Residues",
    loc='upper left',
    bbox_to_anchor=(1.02, 0.35),
    borderaxespad=0
)
ax.grid(
    True,
    linestyle='--',
    linewidth=0.7,
    alpha=0.6
)
plt.tight_layout()
plt.show()
