''' this will contain utility functions '''

# util functions for auto saving plots

import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

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
# setup_autosave()


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

## ------------------------------ Correlation Analysis ------------------------------------------------


def analyze_corr(df, col, filename):
    # fig
    fig = plt.figure(figsize=(12, 12))
    
    # mask
    mask = np.triu(df.corr()) #Because correlation matrices are symmetric (the same above & below the diagonal).
    
    # axes 
    axes = fig.add_axes([0, 0, 1, 1]) #Manually adds an axis taking the full figure area (0,0) to (1,1)
    sns.heatmap(df.dropna().corr(), annot=True, mask=mask, square=True, fmt='.2g', #show correlation values inside cells
                vmin=-1, vmax=1, center=0, cmap='viridis', linecolor='white', linewidths=0.5, #fmt='.2g'rounds numbers 
                cbar_kws= {'orientation': 'vertical'}, ax=axes) 
    
    # title
    axes.text(-1, -1.5, 'Correlation', color='black', fontsize=24, fontweight='bold')

    plt.show(filename)

    # Printing correlations
    corr_matrix = df.corr()


## ------------------------------ Categorical Conversion ------------------------------------------------

def convert_cat(df, col_list): 
    df_temp = pd.DataFrame() 
    df_temp = df
    col_list = col_list
    
    for col in col_list:
        df_temp[col] = df_temp[col].astype('category')
        df_temp[col] = df_temp[col].cat.codes
    return df_temp

## ------------------------------ Outlier Detection ------------------------------------------------

def detect_outliers(df, columns): # using IQR method
    outliers = pd.DataFrame(False, index=df.index, columns=columns)
    
    for col in columns:
        Q1 = df[col].quantile(0.25) #first quartile
        Q3 = df[col].quantile(0.75) #third quartile
        IQR = Q3 - Q1               #interquartile range
        lower_bound = Q1 - 1.5 * IQR 
        upper_bound = Q3 + 1.5 * IQR
        outliers[col] = (df[col] < lower_bound) | (df[col] > upper_bound)
    
    return outliers


