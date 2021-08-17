import setuptools
import os

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="json_numpy_relleums",
    version="0.0.2",
    author="Sebastian Achim Mueller",
    author_email="sebastian-achim.mueller@mpi-hd.mpg.de",
    description="Dump/load numpy arrays into/from json",
    long_description=long_description,
    long_description_content_type="text/md",
    url="https://github.com/cherenkov-plenoscope/json_numpy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["json_numpy",],
    python_requires=">=3.0",
)
