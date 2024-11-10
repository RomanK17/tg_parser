import time
import requests
from bs4 import BeautifulSoup
import random

class ItemsParser:
    FAKE_HEADERS = [
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        },
        {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
        },
    ]

    def __init__(self, page_name: str, item_class_name: str):
        self.page_name = page_name
        self.item_class_name = item_class_name
        self.all_cards : list = []
        self.page_number = 1
        self.previous_cards : list = []


    def get_items_from_page(self):
        retries = 3
        for i in range(retries):
            try:
                response = requests.get(
                f"https://i-ray.ru/{self.page_name}?PAGEN_1={self.page_number}", headers=random.choice(self.FAKE_HEADERS)
                )
                time.sleep(5)
                soup = BeautifulSoup(response.text, "html.parser")
                return soup.find_all(class_=self.item_class_name)
            except requests.exceptions.RequestException as e:
                print(f"Attempt {i + 1} failed: {e}")
                time.sleep(2)
        raise ValueError("не получилось обратиться к сайту!")
        

    def parse_items(self):
        while True:
            cards_from_page = self.get_items_from_page()
            if not self.page_number == 1:
                if cards_from_page == self.previous_cards:
                    break
                self.previous_cards = cards_from_page

            if not cards_from_page:
                break

            self.all_cards.extend(cards_from_page)
            self.page_number += 1
        return self.all_cards

