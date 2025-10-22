''' this will contain utility functions '''

# util functions for auto saving plots

import os
import matplotlib.pyplot as plt

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
setup_auto_save_show()



## wordcloud 

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Generate word cloud from restaurant names
wordcloud = WordCloud(
    width=1600,
    height=800,
    background_color='white',
    colormap='viridis',
    max_words=200,
    relative_scaling=0.5
).generate_from_frequencies(rest_df['name'].value_counts())

# Display the word cloud
plt.figure(figsize=(15, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Most Frequent Restaurant Names", fontsize=18, pad=20)
plt.show(plt.title)
