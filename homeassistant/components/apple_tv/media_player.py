"""Support for Apple TV media player.

Note: pyatv is not supported on Python 3.14+, so this module is a stub.
"""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Load Apple TV media player based on a config entry.

    Note: pyatv is not supported on Python 3.14+, so no entities are added.
    """
    # pyatv is not supported on Python 3.14+
