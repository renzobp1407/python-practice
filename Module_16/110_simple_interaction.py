import requests

APP_ID = "4b1198b8ca574a0aa302761d9a924987"
ENDPOINT = "https://openexchangerates.org/api/latest.json"

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
exchange_rates = response.json()

usd_amount = 1000
gbp_amount = usd_amount * exchange_rates['rates']['GBP']

print(f"USD{usd_amount} is GBP{gbp_amount}")