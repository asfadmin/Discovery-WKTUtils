import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

extra_requirements = [
    'requests',
    'scikit-learn',
]

test_requirements = [
    'pytest',
    'pytest-xdist',
    'pytest-automation',
]

setuptools.setup(
    name="WKTUtils",
    # version= Moved to pyproject.toml,
    author="ASF Discovery Team",
    author_email="uaf-asf-discovery@alaska.edu",
    description="A few WKT utilities for use elsewhere",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asfadmin/Discovery-WKTUtils.git",
    extras_require={"extras": extra_requirements, "test": test_requirements},
    packages=setuptools.find_packages(),
    # package_data= {'WKTUtils': ['VERSION']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'dateparser',
        'defusedxml',
        'geomet',
        'geopandas',
        'kml2geojson',
        'pyshp',
        'PyYAML',
        'Shapely'
    ],
)
