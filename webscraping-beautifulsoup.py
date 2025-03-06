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

"""
Explanation

    Fetches the HTML content of the news website using requests.
    Parses the HTML using BeautifulSoup.
    Extracts and prints the headlines (modify the tag h2 based on the actual website structure)."""
"""
output
Latest News Headlines:
1. BEST OF PREMIUM
2. Categories for you
3. Top News
4. Latest News
5. Categories for you
6. ICC Champions Trophy
7. City News​
8. Business
9. ONLY IN THE EXPRESS
10. SPORTS
11. Latest Video
12. Visual Stories
13. AUDIO
14. Technology
15. Trending
16. Education
17. OPINION
18. Today's Crossword

""" 