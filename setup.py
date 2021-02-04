import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WKTUtils",
    version="0.0.4",
    author="ASF Discovery Team",
    author_email="uaf-asf-discovery@alaska.edu",
    description="A few WKT utilities for use elsewhere",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asfadmin/Discovery-WKTUtils.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "GeologyUtils==0.0.1",
        'dateparser==1.0.0',
        'defusedxml==0.6.0',
        'Fiona==1.8.18',
        'geomet==0.2.1.post1',
        'kml2geojson==4.0.2',
        'pyshp==2.1.0',
        'PyYAML==5.3.1',
        'regex==2020.11.13',
        'requests==2.22.0',
        'Shapely==1.6.4.post2',
        'sklearn==0.0'
    ]
)
