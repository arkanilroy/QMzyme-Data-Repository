import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse

def plot_bars(input_file, colors=None):
    # Read Excel file
    df = pd.read_excel(input_file)

    # Clean column names (important for Excel headers)
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

    fig, ax = plt.subplots(figsize=(12, 6))

    # Default colors
    if colors is None:
        colors = plt.cm.tab10.colors[:n_systems]

    # Plot bars
    for i in range(n_systems):
        offset = (i - n_systems / 2) * width + width / 2

        ax.bar(
            x + offset,
            data.iloc[i].values,
            width,
            label=systems[i],
            color=colors[i]
        )

    # X-axis
    ax.set_xticks(x)
    ax.set_xticklabels(categories, rotation=0, ha='center')

    # Styling
    ax.yaxis.grid(True, linestyle='-', linewidth=0.7, alpha=0.8)
    ax.set_axisbelow(True)

    ax.set_ylabel("EF (MV/cm)")

    # Legend outside
    ax.legend(
        title="System",
        bbox_to_anchor=(1.02, 1),
        loc='upper left'
    )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Grouped bar plot from Excel file")
    parser.add_argument("--input", required=True, help="Input Excel file (.xlsx)")
    parser.add_argument("--colors", nargs='+', help="List of colors")

    args = parser.parse_args()

    plot_bars(args.input, colors=args.colors)

