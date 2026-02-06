# Python 3.14 Upgrade Log

## File Changes Detail

### pyproject.toml
```diff
- "Programming Language :: Python :: 3.13",
+ "Programming Language :: Python :: 3.14",

- requires-python = ">=3.13.2"
+ requires-python = ">=3.14.0"

- py-version = "3.13"
+ py-version = "3.14"
```

### homeassistant/const.py
```diff
- REQUIRED_PYTHON_VER: Final[tuple[int, int, int]] = (3, 13, 2)
- REQUIRED_NEXT_PYTHON_VER: Final[tuple[int, int, int]] = (3, 13, 2)
+ REQUIRED_PYTHON_VER: Final[tuple[int, int, int]] = (3, 14, 0)
+ REQUIRED_NEXT_PYTHON_VER: Final[tuple[int, int, int]] = (3, 14, 0)
```

### mypy.ini
```diff
- python_version = 3.13
+ python_version = 3.14
```

### .github/workflows/ci.yaml
```diff
- DEFAULT_PYTHON: "3.13.2"
- ALL_PYTHON_VERSIONS: "['3.13.2']"
+ DEFAULT_PYTHON: "3.14.2"
+ ALL_PYTHON_VERSIONS: "['3.14.2']"
```

### .github/workflows/wheels.yml
```diff
- DEFAULT_PYTHON: "3.13"
+ DEFAULT_PYTHON: "3.14"

- abi: ["cp313", "cp314"]
+ abi: ["cp314"]
```

### .github/workflows/builder.yml
```diff
- DEFAULT_PYTHON: "3.13"
+ DEFAULT_PYTHON: "3.14"
```

### .github/workflows/translations.yml
```diff
- DEFAULT_PYTHON: "3.13"
+ DEFAULT_PYTHON: "3.14"
```

### script/hassfest/docker.py
```diff
- FROM python:3.13-alpine
+ FROM python:3.14-alpine
```

### script/hassfest/docker/Dockerfile
```diff
- FROM python:3.13-alpine
+ FROM python:3.14-alpine
```

## Commit Information
- **Commit Hash**: ba58dad2c0b66ca952b90b8951bd8e8db5371730
- **Author**: Devin AI
- **Message**: Upgrade Python from 3.13 to 3.14
- **Files Changed**: 9
- **Insertions**: 13
- **Deletions**: 14

## Validation Results
All pre-commit hooks passed:
- ✓ ruff
- ✓ codespell
- ✓ yamllint
- ✓ prettier
- ✓ mypy
- ✓ pylint
- ✓ gen_requirements_all
- ✓ hassfest
- ✓ hassfest-metadata
- ✓ hassfest-mypy-config
