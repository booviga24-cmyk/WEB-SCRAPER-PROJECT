import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

quotes = soup.find_all("span", class_="text")

data = []

for q in quotes:
    data.append(q.text)

print("Quotes found:", len(data))

df = pd.DataFrame(data, columns=["Quote"])
df.to_csv("quotes.csv", index=False)

print("CSV saved successfully")