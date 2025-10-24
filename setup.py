from setuptools import setup, find_packages

setup(
    name="Zomato Restaurant Rating Prediction",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "folium",
        "geopy",
        "plotly",
        "joblib"
    ],
)