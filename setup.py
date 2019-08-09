import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="publix-tendies",
    version="0.0.1",
    author="Nathaniel Compton",
    author_email="nathanielcompton@gmail.com",
    description="Determines whether chicken tender 'Pub subs' are on sale.",
    long_description=long_description,
    long_description_content_type="text/reStructuredText",
    url="https://github.com/nathanielcompton/publix-tendies",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
