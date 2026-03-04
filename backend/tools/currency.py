# Static fallback rates relative to USD
# In a real app these would come from a live API
RATES_TO_USD = {
    "USD": 1.0,
    "EUR": 0.92,
    "DKK": 6.88,
    "GBP": 0.79,
    "SEK": 10.42,
    "NOK": 10.55,
}


def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in RATES_TO_USD:
        return f"Unsupported currency: {from_currency}. Supported: {', '.join(RATES_TO_USD)}"
    if to_currency not in RATES_TO_USD:
        return f"Unsupported currency: {to_currency}. Supported: {', '.join(RATES_TO_USD)}"

    in_usd = amount / RATES_TO_USD[from_currency]
    result = in_usd * RATES_TO_USD[to_currency]
    return f"{amount} {from_currency} = {result:.2f} {to_currency} (static rates)"