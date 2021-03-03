import os

from setuptools import setup


# Utility Function to read the README file
# Used for the long_description. It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='dschloe_dl_framework',
    version="0.0.1",
    author="DSChloe",
    author_email="jhjung@dschloe.com",
    description="Deep Neural Networks built from the book `Deep Learning from Scratch`",
    license="APACHE",
    keywords="Deep Learning",
    url="https://github.com/dschloe/dl_framework",
    packages=["dschloe_dl_framework"],
    classifiers=[
       "Development Status :: 1 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)