import requests
from bs4 import BeautifulSoup


def scrape():
    # https: // www.webscraper.io / test - sites / e - commerce / allinone
    result = requests.get("https://reddit.com")
    soup = BeautifulSoup(result.content, features="html.parser")
    variable = soup.find_all("a")
    for v in variable:
        print(v.get('href'))


class Scraper:
    def __init__(self):
        scrape()
