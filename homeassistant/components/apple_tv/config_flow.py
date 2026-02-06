"""Config flow for Apple TV integration.

Note: pyatv is not supported on Python 3.14+, so this module provides a stub config flow.
"""

from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo

from .const import DOMAIN


class AppleTVConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Apple TV.

    Note: pyatv is not supported on Python 3.14+, so this config flow
    will abort with an error message.
    """

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        return self.async_abort(reason="not_supported")

    async def async_step_zeroconf(
        self, discovery_info: ZeroconfServiceInfo
    ) -> ConfigFlowResult:
        """Handle device found via zeroconf."""
        # Set a unique ID to satisfy hassfest validation for discoverable config flows
        await self.async_set_unique_id(discovery_info.host)
        return self.async_abort(reason="not_supported")
