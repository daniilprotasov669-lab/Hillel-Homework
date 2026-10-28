import requests
import csv
from bs4 import BeautifulSoup

HEADERS = { "User-Agent" }
BASE_URL = "https://quotes.toscrape.com"

response = requests.get(BASE_URL, headers=HEADERS, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")


with open("life.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["author", "text"])
    writer.writeheader()

    for quote in quotes:
        author = quote.find("small", class_="author").get_text(strip=True)
        text = quote.find("span", class_="text").get_text(strip=True)

        writer.writerow({
            "author": author,
            "text": text
        })