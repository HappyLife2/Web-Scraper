# scraper/main.py

from scraper import Scraper

def main():
    # Base URL of the website to scrape
    base_url = "https://example.com"
    
    # Create an instance of the Scraper class
    scraper = Scraper(base_url)
    
    # Start the scraping process
    scraper.scrape()

if __name__ == "__main__":
    main()