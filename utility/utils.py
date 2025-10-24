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


# ------------------------------ Plotting Functions ---------------------------------------------------
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


## Polar Plot
def polar_plot(data, category_col, value_col, filename):
    """
    Create a polar plot for the given data.
    Example:
        polar_plot(data=df, category_col="cuisine", value_col="rating", filename="cuisine_rating_polar")
    """
    categories = data[category_col]
    values = data[value_col]

    angles = [n / float(len(categories)) * 2 * 3.14159 for n in range(len(categories))]
    values += values[:1]
    angles += angles[:1]

    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, polar=True)
    plt.xticks(angles[:-1], categories, color='grey', size=8)
    ax.plot(angles, values, linewidth=1, linestyle='solid')
    ax.fill(angles, values, 'b', alpha=0.1)

    plt.title(f'Polar Plot of {value_col} by {category_col}', size=15, y=1.1)
    save_plot(filename)



    ## ----------- -------- -------- Top Rated Cuisines Plot ------- ------------- --------------

def top_rated_cuisines_plot(cuisine_rating_data):
    plt.figure(figsize=(16, 9))
    barplot = sns.barplot(x='Cuisine', y='Rating', data=cuisine_rating_data, palette='coolwarm')    
    # Add value labels on top of bars for clarity
    for p in barplot.patches:
        barplot.annotate(f"{p.get_height():.2f}",
                        (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center',
                        xytext=(0, 5),
                        textcoords='offset points',
                        fontsize=11)

plt.xlabel('Cuisine', fontsize=16)
plt.ylabel('Average Rating', fontsize=16)
plt.title('Top 30 Rated Cuisines on Zomato (Bangalore)', fontsize=22, pad=20)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.ylim(0, 5)  # Ratings are out of 5
plt.tight_layout()
plt.show("top_30_rated_cuisines")