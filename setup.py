import setuptools
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reproducible_figures",
    version="0.1",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://github.com/prajayshah/reproducible_figures',
    author="Prajay Shah",
    author_email="prajay.shah@mail.utoronto.ca",
    description="Functions to help implement a reproducible figure making process in Python",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6',
    zip_safe=False
)