# web_scraper.py

import requests
from bs4 import BeautifulSoup

# Step 1: Choose a public news website
URL = "https://www.bbc.com/news"

# Step 2: Send a GET request to fetch the page content
response = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
response.raise_for_status()  # Ensures the request was successful

# Step 3: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Extract headline tags (BBC uses <h2> for headlines)
headlines = soup.find_all('h2')

# Step 5: Store all non-empty headline texts
news_list = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]

# Step 6: Save the results to a text file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for i, headline in enumerate(news_list, 1):
        file.write(f"{i}. {headline}\n")

print(f"✅ {len(news_list)} headlines saved to 'headlines.txt'")
