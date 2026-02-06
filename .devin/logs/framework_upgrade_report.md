# Framework Upgrade Report

## Task Summary
**Task:** Upgrade Python Framework to aiohttp==3.13.3 and SQLAlchemy==2.0.44
**Repository:** https://github.com/AI-Data-Ranch/core-home-assistant-fork.git
**Base Branch:** dev
**Result Branch:** feature/framework-update_20260205_173717704
**PR:** https://github.com/AI-Data-Ranch/core-home-assistant-fork/pull/8

---

## Task Metrics

| Metric | Value |
|--------|-------|
| **Task Result** | SUCCESS |
| **Task Duration** | ~75 minutes |
| **Input Tokens (estimated)** | ~150,000 |
| **Output Tokens (estimated)** | ~25,000 |
| **Cached Input Tokens (estimated)** | ~50,000 |
| **Cached Output Tokens (estimated)** | ~5,000 |
| **Cost in Dollar Amount (estimated)** | ~$2.50 |
| **Task Completion Status** | SUCCESS |
| **Errors/Exceptions Occurred** | 1 (mypy type: ignore - fixed) |
| **Files Updated** | 9 |
| **Files Added** | 2 (this report + upgrade log) |

---

## Version Changes

| Package | Previous Version | New Version |
|---------|-----------------|-------------|
| aiohttp | 3.13.2 | 3.13.3 |
| SQLAlchemy | 2.0.41 | 2.0.44 |

---

## Files Modified

1. **pyproject.toml** - Updated aiohttp and SQLAlchemy versions (source of truth)
2. **requirements.txt** - Updated aiohttp and SQLAlchemy versions
3. **requirements_all.txt** - Updated SQLAlchemy version
4. **requirements_test_all.txt** - Updated SQLAlchemy version
5. **homeassistant/package_constraints.txt** - Updated aiohttp and SQLAlchemy versions
6. **homeassistant/components/recorder/manifest.json** - Updated SQLAlchemy version
7. **homeassistant/components/sql/manifest.json** - Updated SQLAlchemy version
8. **homeassistant/components/recorder/db_schema.py** - Removed unused type: ignore comments (SQLAlchemy 2.0.44 improved type stubs)
9. **homeassistant/components/recorder/util.py** - Removed unused type: ignore comments

---

## Submodules

No submodules found in this project.

---

## CI Check Results

### Passing Checks (14)
- Check mypy ✓
- Check pylint ✓
- Check pylint on tests ✓
- Check all requirements ✓
- Check other linters ✓
- Check ruff-format ✓
- Check ruff ✓
- Check Dockerfile ✓
- Check Dockerfile.dev ✓
- Check script/hassfest/docker/Dockerfile ✓
- Prepare dependencies (3.13.11) ✓
- Prepare dependencies (3.14.2) ✓
- Prepare pre-commit base ✓
- Collect information & changes data ✓

### Failing Checks (4 - Pre-existing Issues, NOT Related to Changes)
1. **Dependency review** - Repository configuration issue (Dependency graph not enabled)
2. **Audit licenses (3.13.11)** - Pre-existing issue with caio@0.9.25 package
3. **Audit licenses (3.14.2)** - Pre-existing issue with caio@0.9.25 package
4. **Check hassfest** - Pre-existing issues with tami4 integration

**Note:** All failing checks are NOT marked as required. The PR is mergeable.

---

## Local Testing Results

| Test | Result |
|------|--------|
| Lint (ruff check) | PASSED |
| Core Tests (pytest tests/test_core.py) | PASSED (161 passed, 1 skipped) |
| Home Assistant Startup | PASSED (running on localhost:8123) |
| Pre-commit Hooks | PASSED |
| Mypy Type Check | PASSED |

---

## Code Refactoring Required

SQLAlchemy 2.0.44 includes improved type stubs, making several `# type: ignore` comments unnecessary:

### Removed Type Ignores:
- `homeassistant/components/recorder/db_schema.py:195` - mysql.INTEGER(unsigned=True)
- `homeassistant/components/recorder/db_schema.py:209` - mysql.DATETIME(timezone=True, fsp=6)
- `homeassistant/components/recorder/db_schema.py:214` - mysql.DOUBLE(asdecimal=False)
- `homeassistant/components/recorder/util.py:450` - dbapi_connection.isolation_level
- `homeassistant/components/recorder/util.py:451` - dbapi_connection.isolation_level = None
- `homeassistant/components/recorder/util.py:453` - dbapi_connection.isolation_level = old_isolation

### Retained Type Ignore:
- `homeassistant/components/recorder/db_schema.py:210` - FAST_PYSQLITE_DATETIME() (local untyped function)

---

## Commits

1. **7c41417ca0a** - Upgrade aiohttp to 3.13.3 and SQLAlchemy to 2.0.44
2. **6263545ed82** - Fix mypy errors: remove unused type: ignore comments for SQLAlchemy 2.0.44

---

## Session Information

- **Devin Session:** https://jpmc-oss.devinenterprise.com/sessions/3bf210de10cc4e9e9b85efc9cbd5707f
- **Requested By:** feimvnc@gmail.com (@feimvnc)
- **Date:** 2026-02-06

---

## Recommendations

1. The PR is ready for review and merge
2. All code-related CI checks pass
3. The 4 failing checks are pre-existing repository issues unrelated to this upgrade
4. Consider enabling Dependency graph in repository settings to fix the Dependency review check
5. Consider updating the caio package or adding it to license exceptions to fix Audit licenses checks
6. Consider fixing the tami4 integration's selenium dependency issues to fix hassfest check
