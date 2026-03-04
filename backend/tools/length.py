def meters_to_feet(meters: float) -> str:
    result = meters * 3.28084
    return f"{meters} meters = {result:.4f} feet"


def feet_to_meters(feet: float) -> str:
    result = feet / 3.28084
    return f"{feet} feet = {result:.4f} meters"