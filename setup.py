from setuptools import find_packages, setup
from typing import List

Hyphen_e_dot = '-e .'
## Creating a function that will print the requirements list
def get_requirements(file_path:str)-> List[str]:

    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if Hyphen_e_dot in requirements:
            requirements.remove(Hyphen_e_dot)
    
    return requirements

setup(
    name="Zomato Restaurant Rating Prediction",
    version="0.0.1",
    author="Bhavesh",
    author_email="bhaveshkumar3832@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)
