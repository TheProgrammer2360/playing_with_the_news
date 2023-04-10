import datetime
import requests
from datetime import date
import os
# -------------------------------------------- PARAMETERS -----------------------------------------------------------
API_KEY = os.getenv("API_KEYS")
ENDPOINT = "https://newsapi.org/v2/everything"
# ----------------------------------------GETTING THE CORRECT DATE ---------------------------------------------------
# getting today's date with correct format
today = date.today()
today_with_correct_format = today.strftime("%Y-%m-%d")
# getting yesterday's date with correct format
yesterday = date.today()
yesterday -= datetime.timedelta(days=1)
yesterday_with_correct_format = yesterday.strftime("%Y-%m-%d")
# ----------------------------------------- REQUEST -------------------------------------------------------------------
parameters = {"apiKey": API_KEY, "q": "apple", "from": yesterday_with_correct_format, "to": today_with_correct_format}
request = requests.get(url=ENDPOINT, params=parameters)
request.raise_for_status()
# getting hold of that number of data that we have
data = request.json()
print(data["totalResults"])

