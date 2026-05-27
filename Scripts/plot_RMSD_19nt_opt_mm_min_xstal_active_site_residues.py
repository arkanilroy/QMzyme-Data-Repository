import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# ==========================================
# GLOBAL PLOT SETTINGS
# ==========================================
plt.rc("figure", autolayout=True)

ONE_MM = 1 / 25.4  # Convert mm to inches

plt.rc("legend", fontsize=18)
plt.rc("font", size=16)

#plt.rcParams.update({
#    'font.size': 8,
#    'axes.titlesize': 8,
#    'axes.labelsize': 8,
#    'xtick.labelsize': 8,
#    'ytick.labelsize': 8,
#    'legend.fontsize': 6,
#    'legend.title_fontsize': 6,
#})

# ==========================================
# LOAD DATA
# ==========================================
df = pd.read_excel("RMSD_19nt_opt_mm_min_xstal_active_site_residues.xlsx", index_col=0)

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
    "Ash103": "o",     # circle
}

# ==========================================
# GROUP DEFINITIONS
# ==========================================
groups = {
    "M#_xTB": [
        "mm_min_cutoff3xtb",
        "mm_min_cutoff4xtb",
        "mm_min_cutoff5xtb",
        "mm_min_cutoff6xtb",
        "mm_min_cutoff7xtb",
        "mm_min_cutoff8xtb"
    ],

    "M#_DFT": [
        "mm_min_cutoff3dft",
        "mm_min_cutoff4dft",
        "mm_min_cutoff5dft",
        "mm_min_cutoff6dft",
        "mm_min_cutoff7dft",
        "mm_min_cutoff8dft"
    ],

    "M#_xTB_nowat": [
        "mm_min_cutoff3_nowat_xtb",
        "mm_min_cutoff4_nowat_xtb",
        "mm_min_cutoff5_nowat_xtb",
        "mm_min_cutoff6_nowat_xtb",
        "mm_min_cutoff7_nowat_xtb",
        "mm_min_cutoff8_nowat_xtb"
    ],

    "M#_DFT_nowat": [
        "mm_min_cutoff3_nowat_dft",
        "mm_min_cutoff4_nowat_dft",
        "mm_min_cutoff5_nowat_dft",
        "mm_min_cutoff6_nowat_dft",
        "mm_min_cutoff7_nowat_dft",
        "mm_min_cutoff8_nowat_dft",
    ],
   
    "C#_xTB": [
        "xstal_cutoff3_xtb",
        "xstal_cutoff4_xtb",
        "xstal_cutoff5_xtb",
        "xstal_cutoff6_xtb",
        "xstal_cutoff7_xtb",
        "xstal_cutoff8_xtb",
    ],

    "C#_DFT": [
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

#SIZE BASED ON DIGITAL DISCOVERY GUIDELINES (Double column)
#"Images should fit within either single column (8.3 cm) or double column (17.1 cm) width, and must be no longer than 23.3 cm. They should be prepared to make best use of the space available and must not be larger than a single page."
fig, ax = plt.subplots(figsize=(250 * ONE_MM, 120 * ONE_MM))

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
                s=40,
                color=color,
                edgecolors='black',
                linewidths=0.6,
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
    rotation=0
)

ax.set_ylabel("RMSD ($\AA$)")

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
        markersize=5,
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
        markersize=5
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

# ==========================================
# GRID
# ==========================================
ax.grid(
    True,
    linestyle='--',
    linewidth=0.5,
    alpha=0.6
)

plt.savefig('RMSD_19nt_opt_mm_min_xstal_active_site_residues.eps', format='eps')
plt.savefig('RMSD_19nt_opt_mm_min_xstal_active_site_residues.png', format='png', dpi=300)
plt.show()
