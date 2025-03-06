import requests
from bs4 import BeautifulSoup

# URL of the news website
URL = "https://indianexpress.com/"  # Replace with an actual news website

# Send an HTTP request to the website
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all news headlines (Modify based on the actual website structure)
    headlines = soup.find_all('h2')  

    # Print the headlines
    print("Latest News Headlines:")
    for idx, headline in enumerate(headlines, 1):
        print(f"{idx}. {headline.text.strip()}")
else:
    print("Failed to retrieve the webpage.")
