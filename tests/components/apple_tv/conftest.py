"""Fixtures for component."""

from collections.abc import Generator
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

# Apple TV is not supported on Python 3.14
collect_ignore_glob = ["test_*.py"]


@pytest.fixture(autouse=True, name="mock_scan")
def mock_scan_fixture() -> Generator[AsyncMock]:
    """Mock pyatv.scan."""
    with patch("homeassistant.components.apple_tv.config_flow.scan") as mock_scan:

        async def _scan(
            loop, timeout=5, identifier=None, protocol=None, hosts=None, aiozc=None
        ):
            if not mock_scan.hosts:
                mock_scan.hosts = hosts
            return mock_scan.result

        mock_scan.result = []
        mock_scan.hosts = None
        mock_scan.side_effect = _scan
        yield mock_scan


@pytest.fixture(name="dmap_pin")
def dmap_pin_fixture() -> Generator[MagicMock]:
    """Mock pyatv.scan."""
    with patch("homeassistant.components.apple_tv.config_flow.randrange") as mock_pin:
        mock_pin.side_effect = lambda start, stop: 1111
        yield mock_pin


@pytest.fixture
def pairing_mock() -> Generator[AsyncMock]:
    """Mock pyatv.scan."""
    with patch("homeassistant.components.apple_tv.config_flow.pair") as mock_pair:

        async def _pair(config, protocol, loop, session=None, **kwargs):
            return mock_pair

        async def _begin():
            pass

        async def _close():
            pass

        mock_pair.close.side_effect = _close
        mock_pair.begin.side_effect = _begin
        mock_pair.pin = lambda pin: None
        mock_pair.side_effect = _pair
        yield mock_pair
