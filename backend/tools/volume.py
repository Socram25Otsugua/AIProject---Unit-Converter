def gallons_to_liters(gallons: float) -> str:
    result = gallons * 3.78541
    return f"{gallons} gallons = {result:.4f} liters"


def liters_to_gallons(liters: float) -> str:
    result = liters / 3.78541
    return f"{liters} liters = {result:.4f} gallons"