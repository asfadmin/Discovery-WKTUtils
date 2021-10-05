# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [PEP 440](https://www.python.org/dev/peps/pep-0440/) 
and uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

------

## [1.1.1](https://github.com/asfadmin/Discovery-WKTUtils/compare/v1.1.0...v1.1.1)

## Added
- Project now declares `__version__`.

## Changed
- Bumped up pytest, pytest-automation, and pluggy to latest versions, for test suite
- Bumped up geopandas, pandas, and regex to latest, to remove warnings
- Updated PyPI publishing pipeline, to version GitHub recommends

------

## [1.1.0](https://github.com/asfadmin/Discovery-WKTUtils/compare/v0.2.1...v1.1.0)

### Added
- Issue templates for GitHub

### Changed
- Switched from using `Discovery-PytestAutomation` repo directly, to `pytest-automation` plugin
- Updated versions in `requirements.txt`
- Cleaned up and refactored test suite

### Removed
- Disabled automatic update pipeline, until a better alternative is found

------

## [0.2.1](https://github.com/asfadmin/Discovery-WKTUtils/compare/v0.2.0...v0.2.1)

### Fixed
- Fixed 3D tags not loading with zipped shapefiles

------

## [0.2.0](https://github.com/asfadmin/Discovery-WKTUtils/compare/v0.1.1...v0.2.0)

### Added
- Dependabot integration into pipeline

### Changed
- `Security updates` in package dependancies

### Fixed
- Removed specific version pins in `setup.py`

------

<!--
TEMPLATE:
## [0.2.0](https://github.com/asfadmin/Discovery-WKTUtils/compare/v0.1.1...v0.2.0)

### Added
- For things that are `created` in this release. (New features!!)

### Changed
- For functionality that's `changed`. (ie. Added default arguments, or breaking changes).

### Fixed
- `Bug fixes` go here.
-->
