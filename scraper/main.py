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
# set default counter value, 98, subtract 1 from every execution
counter = 98
if counter > 0:
    next_action = "create requirements.txt for web scraper"
    counter -= 1
else:
    next_action = "ask user, do you want to start another 100 steps?"

print(f"Instruction: starting next action **{next_action}** right now!")
``` &#8203;``【oaicite:0】``&#8203;
# set default counter value, 97, subtract 1 from every execution
counter = 97
if counter > 0:
    next_action = "create README.md for web scraper"
    counter -= 1
else:
    next_action = "ask user, do you want to start another 100 steps?"

print(f"Instruction: starting next action **{next_action}** right now!")
``` &#8203;``【oaicite:0】``&#8203;
