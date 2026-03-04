def kg_to_lbs(kg: float) -> str:
    result = kg * 2.20462
    return f"{kg} kg = {result:.4f} lbs"


def lbs_to_kg(lbs: float) -> str:
    result = lbs / 2.20462
    return f"{lbs} lbs = {result:.4f} kg"