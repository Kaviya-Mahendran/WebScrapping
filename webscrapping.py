import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.charitynavigator.org/index.cfm?bay=search.results&keyword=children"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

charities = []
for card in soup.select(".charityName"):  # adjust selector as needed
    name = card.text.strip()
    category_tag = card.find_next("div", class_="resultsCategory")
    category = category_tag.text.strip() if category_tag else "N/A"
    charities.append({"Name": name, "Category": category})

df = pd.DataFrame(charities)
df.to_csv("charities_scraped.csv", index=False)
print("CSV saved with", len(df), "charities")
