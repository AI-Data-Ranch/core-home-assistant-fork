"""The Apple TV integration entity base class.

Note: pyatv is not supported on Python 3.14+, so this module provides stub classes.
"""

from __future__ import annotations

from typing import Any

from homeassistant.helpers.entity import Entity


class AppleTVEntity(Entity):
    """Device that sends commands to an Apple TV.

    Note: pyatv is not supported on Python 3.14+, so this is a stub class.
    """

    _attr_should_poll = False
    _attr_has_entity_name = True
    _attr_name = None
    atv: Any = None

    def __init__(self, name: str, identifier: str, manager: Any) -> None:
        """Initialize device."""
        self.manager = manager
        self._attr_unique_id = identifier
