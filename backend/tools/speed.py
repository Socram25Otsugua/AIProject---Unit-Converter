def mph_to_kmh(mph: float) -> str:
    result = mph * 1.60934
    return f"{mph} mph = {result:.4f} km/h"


def kmh_to_mph(kmh: float) -> str:
    result = kmh / 1.60934
    return f"{kmh} km/h = {result:.4f} mph"