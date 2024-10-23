"""Sensor platform for Postnord Package Tracking."""
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from .const import DOMAIN

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
):
    """Set up the Postnord sensor."""
    tracking_number = config_entry.data["tracking_number"]
    async_add_entities([PostnordPackageSensor(tracking_number)], True)

class PostnordPackageSensor(SensorEntity):
    """Representation of a Postnord Package sensor."""

    def __init__(self, tracking_number):
        """Initialize the sensor."""
        self._tracking_number = tracking_number
        self._attributes = {}
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"Postnord Package {self._tracking_number}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return self._attributes

    async def async_update(self):
        """Fetch new state data for the sensor."""
        # Implement the API call to Postnord here
        # Update self._state and self._attributes with the fetched data
        pass
