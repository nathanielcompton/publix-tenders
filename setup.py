from setuptools import setup, find_packages

# read the contents of README
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="publix-tendies",
    version="0.0.1",
    author="Nathaniel Compton",
    author_email="nathanielcompton@gmail.com",
    description="Determines whether chicken tender 'Pub subs' are on sale.",
    long_description=long_description,
    long_description_content_type="text/restructuredtext",
    url="https://github.com/nathanielcompton/publix-tendies",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
