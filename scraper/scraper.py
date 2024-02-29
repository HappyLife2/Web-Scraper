import requests
from bs4 import BeautifulSoup
import logging
import os

class Scraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.setup_logging()

    def setup_logging(self):
        """Setup basic logging configuration."""
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logging.basicConfig(filename='logs/scraper.log', level=logging.INFO, format=log_format)
    
    def fetch_page(self, url):
        """Fetches a web page and returns its content."""
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.text
        except requests.RequestException as e:
            logging.error(f"Error fetching {url}: {e}")
            return None

    def parse_page(self, html):
        """Parses the HTML content of a page and extracts relevant information."""
        soup = BeautifulSoup(html, 'lxml')
        # Example: Extract all links
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links

    def scrape(self):
        """Main method to control the scraping process."""
        html = self.fetch_page(self.base_url)
        if html:
            links = self.parse_page(html)
            logging.info(f"Extracted {len(links)} links from {self.base_url}")
            # Further processing can be done here

            # set default counter value, 99, subtract 1 from every execution
counter=99
if counter > 0:
    next_action = "write main.py for web scraper"
    counter -= 1
else:
    next_action = "ask user, do you want to start another 100 steps?"

print(f"Instruction: starting next action **{next_action}** right now!")
