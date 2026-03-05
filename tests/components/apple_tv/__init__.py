"""Tests for Apple TV."""

import pytest

try:
    import pyatv  # noqa: F401

    # Make asserts in the common module display differences
    pytest.register_assert_rewrite("tests.components.apple_tv.common")
except ImportError:
    pass
