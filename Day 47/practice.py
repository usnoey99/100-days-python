from bs4 import BeautifulSoup
import requests

pratice_url = "http://appbrewery.github.io/instant_pot/"
live_url = "http://www.amzazon.com/dp/"

response = requests.get(pratice_url)

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(name="span", class_="a-offscreen").get_text()

price_without_currency = price.split("$")[1]

price_as_float = float(price_without_currency)

print(price_as_float)