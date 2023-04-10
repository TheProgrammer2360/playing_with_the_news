import requests
import os

API_KEY = os.getenv("API_KEYS")
parameters = {"apiKey": API_KEY, "country": "us"}
ENDPOINT = "https://newsapi.org/v2/top-headlines"
request = requests.get(url=ENDPOINT, params=parameters)
request.raise_for_status()

