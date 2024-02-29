# README.md for Web Scraper Project

## Project Overview

This project is a simple web scraper built with Python. It uses `requests` to fetch web pages and `BeautifulSoup` to parse HTML content. This scraper is designed to extract and log links from a specified webpage.

## Setup Instructions

1. **Clone the Repository**
   - Clone this repository to your local machine using `git clone <repository-url>`.

2. **Install Dependencies**
   - Run `pip install -r requirements.txt` to install the required Python packages.

3. **Configuration**
   - Edit `scraper/main.py` to set the `base_url` to the website you want to scrape.

4. **Run the Scraper**
   - Navigate to the project directory and run `python scraper/main.py` to start the scraping process.

## Project Structure

- `/scraper` contains the Python scripts for the scraping logic.
- `/logs` will hold log files generated during the scraping process.
- `requirements.txt` lists the project dependencies.
- `README.md` provides project documentation.

## Logging

- The scraper logs its activity to `logs/scraper.log`. Check this file for debug information and the results of the scraping session.

## Disclaimer

- Please be mindful and respectful of websites' terms of service and robots.txt files when using this scraper. Always ensure your scraping activities are legal and ethical.
