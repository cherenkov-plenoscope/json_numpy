import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="json_numpy_sebastian-achim-mueller",
    version="0.1.1",
    author="Sebastian Achim Mueller",
    author_email="sebastian-achim.mueller@mpi-hd.mpg.de",
    description="Dumps and loads numpy-arrays into or from json",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cherenkov-plenoscope/json_numpy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["json_numpy",],
    python_requires=">=3.0",
)
