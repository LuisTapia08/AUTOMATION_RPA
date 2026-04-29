import csv
import requests
from bs4 import BeautifulSoup
from time import sleep
from src.modules.beautifulsoup.data_handler import DataHandler
import src.modules.beautifulsoup.utils.constants_urls as URL
from src.modules.beautifulsoup.scrapy import Action

def main():
    response = requests.get(URL.BASE, timeout=3)
    soup = BeautifulSoup(response.content, "html.parser")
    cards = soup.select(".product-image-wrapper")
    action = Action(cards)
    action.extract()
    items = action.items
    data_handler = DataHandler(data=items)
    data_handler.save()

if __name__ == "__main__":    main()