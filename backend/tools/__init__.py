# tools package - each module is one conversion tool for the agent
from .weight import kg_to_lbs, lbs_to_kg
from .volume import gallons_to_liters, liters_to_gallons
from .length import meters_to_feet, feet_to_meters
from .temperature import fahrenheit_to_celsius, celsius_to_fahrenheit
from .speed import mph_to_kmh, kmh_to_mph
from .currency import convert_currency

__all__ = [
    "kg_to_lbs", "lbs_to_kg",
    "gallons_to_liters", "liters_to_gallons",
    "meters_to_feet", "feet_to_meters",
    "fahrenheit_to_celsius", "celsius_to_fahrenheit",
    "mph_to_kmh", "kmh_to_mph",
    "convert_currency",
]