import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse


def plot_bars(input_file, colors=None):
    # -------------------------
    # Global plotting settings
    # -------------------------
    plt.rc("figure", autolayout=True)

    ONE_MM = 1 / 25.4  # Convert mm to inches

    plt.rc("legend", fontsize=18)
    plt.rc("font", size=14)

    # -------------------------
    # Read Excel file
    # -------------------------
    df = pd.read_excel(input_file)

    # Clean column names
    df.columns = df.columns.str.strip()

    # First column = system names
    systems = df.iloc[:, 0]

    # Remaining columns = categories
    data = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
    categories = data.columns

    n_systems = len(systems)
    n_categories = len(categories)

    x = np.arange(n_categories)
    width = 0.8 / n_systems

    # SIZE BASED ON DIGITAL DISCOVERY GUIDELINES (Double column)
    # "Images should fit within either single column (8.3 cm)
    # or double column (17.1 cm) width, and must be no longer
    # than 23.3 cm."
    fig, ax = plt.subplots(figsize=(230 * ONE_MM, 120 * ONE_MM))

    # Default colors
    if colors is None:
        colors = plt.cm.tab10.colors[:n_systems]

    # -------------------------
    # Plot bars
    # -------------------------
    for i in range(n_systems):
        offset = (i - n_systems / 2) * width + width / 2

        ax.bar(
            x + offset,
            data.iloc[i].values,
            width,
            label=systems[i],
            color=colors[i],
            edgecolor='black',   # Border color
            linewidth=0.8        # Border thickness
        )

    # -------------------------
    # X-axis
    # -------------------------
    ax.set_xticks(x)
    ax.set_xticklabels(categories, rotation=0, ha='center')

    # -------------------------
    # Styling
    # -------------------------
    ax.yaxis.grid(True, linestyle='-', linewidth=0.7, alpha=0.8)
    ax.set_axisbelow(True)

    ax.set_ylabel("EF (MV/cm)")

    # Legend outside
    ax.legend(
        title="System",
        bbox_to_anchor=(1.02, 1),
        loc='upper left'
    )

    # Optional: cleaner borders around axes
    for spine in ax.spines.values():
        spine.set_linewidth(1.0)

    # Save figures
    plt.savefig(
        'EF_gaussian_subtractive_mm_min_xstal.eps',
        format='eps',
        bbox_inches='tight'
    )

    plt.savefig(
        'EF_gaussian_subtractive_mm_min_xstal.png',
        format='png',
        dpi=300,
        bbox_inches='tight'
    )

    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Grouped bar plot from Excel file"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Input Excel file (.xlsx)"
    )

    parser.add_argument(
        "--colors",
        nargs='+',
        help="List of colors"
    )

    args = parser.parse_args()

    plot_bars(args.input, colors=args.colors)
