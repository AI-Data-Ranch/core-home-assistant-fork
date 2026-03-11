"""Tests for Apple TV."""

import pytest

# Apple TV is not supported on Python 3.14
collect_ignore_glob = ["test_*.py"]

# Make asserts in the common module display differences
pytest.register_assert_rewrite("tests.components.apple_tv.common")
