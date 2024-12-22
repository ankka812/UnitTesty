import os

from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = os.getenv(
    "VERSION", "0.0.0"
)

setup(
    name="student management",
    version="0.1.0",  
    author="ankka812", 
    author_email="anka.w812@gmail.com", 
    description="Project to manage students and their attendance.",
    url="https://github.com/ankka812/UnitTesty.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.6",
)
