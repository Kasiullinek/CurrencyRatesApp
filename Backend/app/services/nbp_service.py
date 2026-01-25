import requests
from datetime import date

NBP_API_URL = "https://api.nbp.pl/api/exchangerates/tables/A"

def fetch_rates_from_nbp():
    response = requests.get(NBP_API_URL, params={"format": "json"})
    response.raise_for_status()

    table = response.json()[0]
    rates = table["rates"]
    effective_date = table["effectiveDate"]

    return [
        {
            "currency": rate["code"],
            "rate": rate["mid"],
            "date": effective_date
        }
        for rate in rates
    ]
