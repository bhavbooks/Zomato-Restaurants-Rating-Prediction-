''' this will contain utility functions '''

# util functions for auto saving plots

import os
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure folder exists
os.makedirs('visualizations', exist_ok=True)

def save_plot(filename, folder='visualizations', dpi=300, show=True):
    """
    Save the current matplotlib plot automatically.
    Example:
        save_plot('price_distribution')
    """
    path = os.path.join(folder, f"{filename}.png")
    plt.savefig(path, bbox_inches='tight', dpi=dpi)
    if show:
        plt.show()
    print(f"✅ Plot saved at: {path}")


def setup_autosave():
    """
    Replaces plt.show() with a version that auto-saves when a filename is passed.
    Example:
        plt.show("my_plot")
    """
    _old_show = plt.show

    def auto_save_show(filename=None):
        if filename:
            os.makedirs('visualizations', exist_ok=True)
            plt.savefig(f'visualizations/{filename}.png', bbox_inches='tight', dpi=300)
            print(f"✅ Auto-saved: visualizations/{filename}.png")
        _old_show()

    plt.show = auto_save_show
    print("✅ Auto-save mode activated. Use plt.show('filename') to save automatically.")

# Activate auto-save by default
setup_autosave()

def box_plot(data, x, y):
    """
    Create a box plot for the given data.
    Example:
        box_plot(data=df, x="city", y="rating")
    """
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=data, x=x, y=y)
    plt.title(f'Box Plot of {y} by {x}')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.xticks(rotation=45)
    plt.tight_layout()
