"""Constants for the SolarMAN logger integration."""
from typing import Final
from enum import Enum

DOMAIN = "solarman-modbus"

SENSOR_VDC1: Final = "Voltage DC1"
SENSOR_IDC1: Final = "Current DC1"
SENSOR_VDC2: Final = "Voltage DC2"
SENSOR_IDC2: Final = "Current DC2"
SENSOR_VAC: Final = "Voltage AC"
SENSOR_IAC: Final = "Current AC"
SENSOR_FREQ: Final = "Frequency"
SENSOR_TEMP: Final = "Temperature"
SENSOR_PWR: Final = "Power"
SENSOR_ENERGY_DAY: Final = "Energy Today"
SENSOR_ENERGY_TOT: Final = "Energy Total"
SENSOR_HRS: Final = "Hours Total"

START: Final = 0x20c

from homeassistant.const import (
    ELECTRIC_POTENTIAL_VOLT,
    ELECTRIC_CURRENT_AMPERE,
    POWER_WATT,
    POWER_KILO_WATT,
    TEMP_CELSIUS,
    FREQUENCY_HERTZ,
    ENERGY_KILO_WATT_HOUR,
    TIME_HOURS
)

from homeassistant.components.sensor import (
    SensorDeviceClass,
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL_INCREASING,
)


class Device(Enum):
    LSW3 = 'LSW-3'

class Sensor(Enum):
    VDC1 = "Voltage DC1"
    IDC1 = "Current DC1"
    PDC1 = "Power DC1"
    VDC2 = "Voltage DC2"
    IDC2 = "Current DC2"
    PDC2 = "Power DC2"
    VAC = "Voltage AC"
    IAC = "Current AC"
    FREQ = "Frequency"
    TEMP = "Temperature"
    PWR = "Power"
    ENERGY_DAY = "Energy Today"
    ENERGY_TOT = "Energy Total"
    HRS = "Hours Total"

class SensorDefinition:
    """A definition of a sensor

    :param name: The human-readable name of the sensor
    :param device_class: The HomeAssistant class of the device, e.g. DEVICE_CLASS_VOLTAGE
    :param state_class: The HomeAssistant class of the device's state, e.g. STATE_CLASS_MEASUREMENT for one-off measurements or STATE_CLASS_TOTAL_INCREASING for measurements that count up
    :param unit: The units of the measurement, e.g. ELECTRIC_POTENTIAL_VOLT (volts), ELECTRIC_CURRENT_AMPERE (amps)
    :param signed: Is the value for this measure signed i.e. positive or negative
    :param mb_offset: The modbus register offset for this sensor reading
    :param mb_size: The size of this sensor reading in bytes in the modbus response. Most sensor readings are 2-bytes, some are more.
    :param mb_mult: A multiplier to apply to the raw modbus value to convert it into the appropriate units.
    """
    def __init__(
        self,
        name: str,
        device_class: str,
        state_class: str,
        unit: str,
        signed,
        mb_offset: int,
        mb_size: int = 2,
        mb_mult: int = 1
    ):
        self.name = name
        self.device_class = device_class
        self.state_class = state_class
        self.unit = unit
        self.signed = signed
        self.mb_offset = mb_offset
        self.mb_size = mb_size
        self.mb_mult = mb_mult

# NB: device sensors MUST be in order of mb_offset
SENSOR_DEFINITIONS: Final = {
    Device.LSW3: [
        SensorDefinition(
            name="Inverter Frequency",
            device_class=SensorDeviceClass.FREQUENCY,
            state_class=STATE_CLASS_MEASUREMENT,
            unit=FREQUENCY_HERTZ,
            signed=False,
            mb_offset=0x20c-START,
            mb_size=1,
            mb_mult=0.01,
        ),
        SensorDefinition(
            name="Battery Charge/Discharge",
            device_class=SensorDeviceClass.POWER,
            state_class=STATE_CLASS_MEASUREMENT,
            unit=POWER_WATT,
            signed=True,
            mb_offset=0x20d-START,
            mb_size=1,
            mb_mult=10,
        ),
        SensorDefinition(
            name="Battery Charge",
            device_class=SensorDeviceClass.ENERGY,
            state_class=STATE_CLASS_MEASUREMENT,
            unit=ENERGY_KILO_WATT_HOUR,
            signed=False,
            mb_offset=0x210-START,
            mb_size=1,
            mb_mult=1,
        ),
        SensorDefinition(
            name="Battery Temp",
            device_class=SensorDeviceClass.TEMPERATURE,
            state_class=STATE_CLASS_MEASUREMENT,
            unit=TEMP_CELSIUS,
            signed=False,
            mb_offset=0X211-START,
            mb_size=1,
            mb_mult=1,
        ),
        SensorDefinition(
            name="Grid Power IO",
            device_class=SensorDeviceClass.POWER,
            state_class=STATE_CLASS_MEASUREMENT,
            unit=POWER_WATT,
            signed=True,
            mb_offset=0x212-START,
            mb_size=1,
            mb_mult=-10,
        ),
        SensorDefinition(
            name="House Consumption",
            device_class=SensorDeviceClass.POWER,
            state_class=STATE_CLASS_MEASUREMENT,
            unit=POWER_WATT,
            signed=False,
            mb_offset=0x213-START,
            mb_size=1,
            mb_mult=10,
        ),
        SensorDefinition(
            name="PV Power",
            device_class=SensorDeviceClass.POWER,
            state_class=STATE_CLASS_MEASUREMENT,
            unit=POWER_WATT,
            signed=False,
            mb_offset=0x215-START,
            mb_size=1,
            mb_mult=10,
        ),
        SensorDefinition(
            name="Today Generated Power",
            device_class=SensorDeviceClass.ENERGY,
            state_class=STATE_CLASS_TOTAL_INCREASING,
            unit=ENERGY_KILO_WATT_HOUR,
            signed=False,
            mb_offset=0x218-START,
            mb_size=1,
            mb_mult=0.01,
        ),
        SensorDefinition(
            name="Today Sold Power",
            device_class=SensorDeviceClass.ENERGY,
            state_class=STATE_CLASS_TOTAL_INCREASING,
            unit=ENERGY_KILO_WATT_HOUR,
            signed=False,
            mb_offset=0x219-START,
            mb_size=1,
            mb_mult=0.01,
        ),
        SensorDefinition(
            name="Today Bought Power",
            device_class=SensorDeviceClass.ENERGY,
            state_class=STATE_CLASS_TOTAL_INCREASING,
            unit=ENERGY_KILO_WATT_HOUR,
            signed=False,
            mb_offset=0x21a-START,
            mb_size=1,
            mb_mult=0.01,
        ),
        SensorDefinition(
            name="Today Consumption Power",
            device_class=SensorDeviceClass.ENERGY,
            state_class=STATE_CLASS_TOTAL_INCREASING,
            unit=ENERGY_KILO_WATT_HOUR,
            signed=False,
            mb_offset=0x21b-START,
            mb_size=1,
            mb_mult=0.01,
        ),
        SensorDefinition(
            name="Battery Cycles",
            device_class=None,
            state_class=STATE_CLASS_TOTAL_INCREASING,
            unit=None,
            signed=False,
            mb_offset=0x22c-START,
            mb_size=1,
            mb_mult=1,
        ),
        SensorDefinition(
            name="Inverter Temp",
            device_class=SensorDeviceClass.TEMPERATURE,
            state_class=STATE_CLASS_MEASUREMENT,
            unit=TEMP_CELSIUS,
            signed=False,
            mb_offset=0x238-START,
            mb_size=1,
            mb_mult=1,
        ),
        SensorDefinition(
            name="Inverter Heatsink Temp",
            device_class=SensorDeviceClass.TEMPERATURE,
            state_class=STATE_CLASS_MEASUREMENT,
            unit=TEMP_CELSIUS,
            signed=False,
            mb_offset=0x239-START,
            mb_size=1,
            mb_mult=1,
        ),   
    ]
}
