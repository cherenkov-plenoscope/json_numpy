import setuptools
import os


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


with open(os.path.join("json_numpy", "version.py")) as f:
    txt = f.read()
    last_line = txt.splitlines()[-1]
    version_string = last_line.split()[-1]
    version = version_string.strip("\"'")


setuptools.setup(
    name="json_numpy_sebastian-achim-mueller",
    version=version,
    author="Sebastian Achim Mueller",
    author_email="sebastian-achim.mueller@mpi-hd.mpg.de",
    description="Dumps and loads numpy-arrays into or from json",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/cherenkov-plenoscope/json_numpy",
    packages=["json_numpy",],
    package_data={"json_numpy": []},
    install_requires=[],
    python_requires=">=3.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
