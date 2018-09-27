import setuptools

name = "example_pkg",
version = "0.0.1",
author = "Example Author",
author_email = "author@example.com",
description = "A small example package",
long_description_content_type = "text/markdown",
url = "https://github.com/pypa/sampleproject",

classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    url=url,
    packages=setuptools.find_packages(),
    classifiers=classifiers,
)
