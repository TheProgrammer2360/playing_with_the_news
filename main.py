import datetime
import requests
from datetime import date
import smtplib
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
# ----------------------------------------- SEND EMAIL WITH ARTICLE -------------------------------------------------
articles = data["articles"]
print(articles[0])
title = articles[0]["title"]
content = articles[0]["content"]
url = articles[0]["url"]

from_email = os.getenv("FROM_EMAIL")
to_email = os.getenv("TO_EMAIL")

# sending email to one user
# establish a connection with smtp server
connection = smtplib.SMTP("smtp.gmail.com")
# secure the connection
connection.starttls()
# login with the email you want to send the message via
connection.login(user=from_email, password=os.getenv("APP_PASSWORD"))
# sending emails about all the articles
for article in articles:
    try:
        # sometimes you an error shows up about ascii code cant encode character
        connection.sendmail(from_addr=from_email, to_addrs=to_email, msg=f"Subject:{article['title']}\n\n{article['url']}")
        # if this article has been
    except UnicodeEncodeError:
        pass
connection.close()