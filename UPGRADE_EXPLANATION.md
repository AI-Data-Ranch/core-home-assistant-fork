# Python Upgrade Decision and Process Log

## Decision Summary
- **Language**: Python
- **Current Version**: 3.13
- **Target Version**: 3.14
- **Decision**: Upgrade
- **Decision Date**: 2026-03-05

## Rationale

### Support Timeline Analysis
- Python 3.13 was released October 2024 and is actively supported.
- Python 3.14 was released October 2025 and is the latest stable release with active support through ~2030.
- The CI already tests against Python 3.14.2, indicating readiness for the upgrade.

### Version Selection Logic
- The user explicitly requested upgrading from Python 3.13 to Python 3.14.
- The project's CI configuration (`ci.yaml`) already includes Python 3.14.2 in `ALL_PYTHON_VERSIONS`, confirming compatibility.
- The `wheels.yml` workflow already builds wheels for `cp314`, showing infrastructure support.
- The `pyproject.toml` already lists `"Programming Language :: Python :: 3.14"` as a classifier.

### Risk Assessment
- **Low risk**: The project already tests against Python 3.14 in CI.
- Some components (e.g., `apple_tv`, `profiler`) have known incompatibilities with Python 3.14, but these are handled gracefully with warning messages already in the codebase.
- The `standard-aifc` and `standard-telnetlib` backport libraries (version 3.13.0) are library versions, not Python version-specific, and will continue to work.

## Actions Taken

### 1. Version Reference Updates

| File | Change | Reason |
|------|--------|--------|
| `homeassistant/const.py` | `REQUIRED_PYTHON_VER`: (3, 13, 2) -> (3, 14, 0) | Set minimum required Python version |
| `homeassistant/const.py` | `REQUIRED_NEXT_PYTHON_VER`: (3, 13, 2) -> (3, 14, 0) | Set next required Python version |
| `pyproject.toml` | `requires-python`: >=3.13.2 -> >=3.14.0 | Update minimum Python requirement |
| `pyproject.toml` | Remove `"Programming Language :: Python :: 3.13"` classifier | No longer targeting 3.13 |
| `pyproject.toml` | `py-version`: "3.13" -> "3.14" (pylint config) | Update pylint target version |
| `mypy.ini` | `python_version`: 3.13 -> 3.14 | Update mypy target version |
| `.python-version` | 3.13 -> 3.14 | Update pyenv/uv version file |
| `.github/workflows/ci.yaml` | `DEFAULT_PYTHON`: "3.13.11" -> "3.14.2" | Update CI default Python |
| `.github/workflows/ci.yaml` | `ALL_PYTHON_VERSIONS`: removed 3.13.11, kept 3.14.2 | Only test against 3.14 |
| `.github/workflows/translations.yml` | `DEFAULT_PYTHON`: "3.13" -> "3.14" | Update workflow Python version |
| `.github/workflows/wheels.yml` | `DEFAULT_PYTHON`: "3.13" -> "3.14" | Update workflow Python version |
| `.github/workflows/wheels.yml` | Wheel matrix: removed cp313, kept cp314 | Only build wheels for 3.14 |
| `.github/workflows/builder.yml` | `DEFAULT_PYTHON`: "3.13" -> "3.14" | Update workflow Python version |
| `script/hassfest/docker.py` | `FROM python:3.13-alpine` -> `python:3.14-alpine` in template | Update hassfest Docker template (auto-generates Dockerfile) |
| `script/hassfest/docker/Dockerfile` | `FROM python:3.13-alpine` -> `python:3.14-alpine` | Update Docker base image (auto-generated from template) |

### 2. Files NOT Changed (intentional)
- `aiohttp==3.13.2` in requirements files - This is the aiohttp library version, not a Python version reference.
- `standard-aifc==3.13.0` and `standard-telnetlib==3.13.0` - These are library versions providing backports of removed stdlib modules.
- Test fixture JSON files containing "3.13" in data values.
- Comments referencing Python 3.13 removal of aifc/telnetlib modules (historical facts).
- Pytest filter warnings about Python 3.13 removals (still valid for the backport libraries).
- `Dockerfile` and `Dockerfile.dev` - These use `BUILD_FROM` arg or `.python-version` file respectively, not hardcoded Python versions.

### 3. Issues Encountered
None - the project was already prepared for Python 3.14 support with existing CI testing.

## Final Recommendation
The upgrade to Python 3.14 is straightforward as the project already had Python 3.14 compatibility testing in place. All configuration files have been updated to use Python 3.14 as the default/minimum version. Monitor CI for any regressions and address component-specific incompatibilities as they arise.
