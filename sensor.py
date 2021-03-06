"""
A sensor created to read temperature from Adax radiators
For more details about this platform, please refer to the documentation at
https://github.com/kayjei/adax_wifi
"""
import logging
import json
import requests
import voluptuous as vol
from .connect import Adax
from .parameters import set_param

from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import (PLATFORM_SCHEMA)
from homeassistant.const import (TEMP_CELSIUS)

_LOGGER = logging.getLogger(__name__)



ZONE_URL = 'https://heater.azurewebsites.net/sheater-client-api/rest/zones/list/' + set_param("account_id")



def setup_platform(hass, config, add_devices, discovery_info=None):
    _LOGGER.debug("Adding sensor component: adax wifi ...")
    """Set up the sensor platform"""
    
    params = {"signature": set_param("zone_signature"), "appVersion": set_param("appVersion"), "device": set_param("device"), 
        "os": set_param("os"), "timeOffset": set_param("timeOffset"), "timeZone": set_param("timeZone")}

    zones_json = Adax.do_api_request(ZONE_URL, params)

    for zone in zones_json[1]:
        zone_id = int(zone["id"])
        zone_name = str(zone["name"])

        HEAT_URL = 'https://heater.azurewebsites.net/sheater-client-api/rest/zones/' + str(zone_id) + '/heaters/' + set_param("account_id")
        params = {"signature": set_param("heat_signature"), "appVersion": set_param("appVersion"), "device": set_param("device"), 
                "os": set_param("os"), "timeOffset": set_param("timeOffset"), "timeZone": set_param("timeZone")}

        data = Adax.do_api_request(HEAT_URL, params)
        device_list = []

        for heater in data[1]:
            device_id = int(heater["id"])
            name = heater["name"]
            state = round(float(heater["currentTemperature"]) / 100, 2)

            add_devices([AdaxDevice(device_id, zone_name, name, state)], True)


class AdaxDevice(Entity):
    def __init__(self, device_id, zone_name, name, temperature):
        self._device_id = device_id
        self._entity_id = "sensor.adax_" + str(self._device_id)
        self._zone_name = zone_name
        self._name = name
        self._temperature = temperature
        self.update()

    def update(self):
        """Heaters"""
        params = {"signature": set_param("zone_signature"), "appVersion": set_param("appVersion"), "device": set_param("device"), 
                "os": set_param("os"), "timeOffset": set_param("timeOffset"), "timeZone": set_param("timeZone")}

        zones_json = Adax.do_api_request(ZONE_URL, params)

        for zone in zones_json[1]:
            zone_id = int(zone["id"])
            zone_name = str(zone["name"])
            child_lock = bool(zone["heatersLocked"])

            HEAT_URL = 'https://heater.azurewebsites.net/sheater-client-api/rest/zones/' + str(zone_id) + '/heaters/' + set_param("account_id")
            params = {"signature": set_param("heat_signature"), "appVersion": set_param("appVersion"), "device": set_param("device"), 
                    "os": set_param("os"), "timeOffset": set_param("timeOffset"), "timeZone": set_param("timeZone")}

            data = Adax.do_api_request(HEAT_URL, params)
            device_list = []

            for heater in data[1]:
                if self._device_id == heater["id"]:
                    self._state = round(float(heater["currentTemperature"]) / 100, 2)
                    self._name = heater["name"]
                    self._target = round(float(heater["targetTemperature"]) / 100, 2)
                    self._locked = child_lock
                    self._zone_name = zone_name
                    _LOGGER.debug("Temp is %s for %s", self._state, self._name)

    @property
    def entity_id(self):
        """Return the id of the sensor"""
        return self._entity_id

    @property
    def name(self):
        """Return the name of the sensor"""
        return self._name

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement."""
        return '°C'

    @property
    def temperature_unit(self):
        """Return the unit of measurement."""
        return TEMP_CELSIUS

    @property
    def state(self):
        """Return the state of the sensor"""
        return self._state

    @property
    def icon(self):
        """Return the icon of the sensor"""
        return 'mdi:radiator'
    
    @property
    def device_class(self):
        """Return the device class of the sensor"""
        return 'temperature'


    @property
    def device_state_attributes(self):
        """Return the attribute(s) of the sensor"""
        return {
            "targetTemperature": self._target,
            "childLock": self._locked,
            "zone": self._zone_name
        }
