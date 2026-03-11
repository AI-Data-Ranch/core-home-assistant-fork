"""The Apple TV integration."""

from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_ADDRESS, Platform  # noqa: F401
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import HomeAssistantError

PLATFORMS = [Platform.MEDIA_PLAYER, Platform.REMOTE]


type AppleTvConfigEntry = ConfigEntry[AppleTVManager]


class AppleTVManager:
    """Stub manager for type checking - Apple TV not supported on Python 3.14."""

    atv: Any = None
    is_on: bool = False
    is_connecting: bool = False

    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None:
        """Initialize power manager."""
        self.config_entry = config_entry
        self.hass = hass

    async def connect(self) -> None:
        """Connect to device."""

    async def disconnect(self) -> None:
        """Disconnect from device."""

    async def init(self) -> None:
        """Initialize power management."""


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up a config entry for Apple TV."""
    raise HomeAssistantError("Apple TV is not supported on Python 3.14.")


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload an Apple TV config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
