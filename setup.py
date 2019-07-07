import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="git_test_pkg",
    version="0.0.1",
    author="Laura McLoughlin",
    author_email="b00092153@student.itb.ie",
    description="A text misclassification analysis package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lauramcloughlin/git_test_pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)