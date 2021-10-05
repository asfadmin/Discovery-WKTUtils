import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WKTUtils",
    # version= Moved to pyproject.toml,
    author="ASF Discovery Team",
    author_email="uaf-asf-discovery@alaska.edu",
    description="A few WKT utilities for use elsewhere",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asfadmin/Discovery-WKTUtils.git",
    packages=setuptools.find_packages(),
    # package_data= {'WKTUtils': ['VERSION']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'dateparser',
        'defusedxml',
        'Fiona',
        'geomet',
        'geopandas',
        'kml2geojson',
        'pyshp',
        'PyYAML',
        'regex',
        'requests',
        'Shapely',
        'sklearn'
    ]
)
