import os
import io
from setuptools import find_packages, setup

# Utility Function to read the README file
# Used for the long_description. It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below

# Read in the README for the long description on PyPI
def long_description():
    with io.open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

setup(
    name='dschloe_dl_framework',
    version="0.0.1",
    author="DSChloe",
    author_email="jhjung@dschloe.com",
    description="Deep Neural Networks built from the book `Deep Learning from Scratch`",
    license='MIT',
    packages=find_packages(),
    keywords="Deep Learning",
    url="https://github.com/dschloe/dl_framework",
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    zip_safe=False
)