def fahrenheit_to_celsius(f: float) -> str:
    result = (f - 32) * 5 / 9
    return f"{f}°F = {result:.4f}°C"


def celsius_to_fahrenheit(c: float) -> str:
    result = (c * 9 / 5) + 32
    return f"{c}°C = {result:.4f}°F"