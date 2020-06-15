import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WKTUtils",
    version="0.0.1",
    author="ASF Discovery Team",
    author_email="uaf-asf-discovery@alaska.edu",
    description="A few WKT utilities for use elsewhere",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="git@github.com/asfadmin/Discovery-WKTUtils.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)