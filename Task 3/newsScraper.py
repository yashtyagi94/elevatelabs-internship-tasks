import requests
from bs4 import BeautifulSoup

# Step 1: Choose a news website (example: https://www.bbc.com/news)
url = "https://www.bbc.com/news"

try:
    # Step 2: Fetch the HTML content
    response = requests.get(url)
    response.raise_for_status()  # Raise an error if the request failed
except requests.exceptions.RequestException as e:
    print(f"❌ Error fetching the page: {e}")
    exit()

# Step 3: Parse the HTML with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Extract headlines from <h2> or <title> tags
headlines = []

# Add headlines from <h2> tags
for tag in soup.find_all('h2'):
    text = tag.get_text(strip=True)
    if text:
        headlines.append(text)

# Also add the <title> of the page
title_tag = soup.find('title')
if title_tag:
    headlines.insert(0, title_tag.get_text(strip=True))

# Step 5: Save headlines to a .txt file
output_file = "top_headlines.txt"
try:
    with open(output_file, "w", encoding="utf-8") as file:
        for i, headline in enumerate(headlines[:20], 1):  # Limit to top 20
            file.write(f"{i}. {headline}\n")
    print(f"✅ Headlines saved to {output_file}")
except IOError as e:
    print(f"❌ File write error: {e}")