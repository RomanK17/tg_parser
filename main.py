import asyncio
from parse_items import ItemsParser
from filter_items import FilterItems
from tg_bot import send_message
from message_formater import format_message


all_cards = ItemsParser("iphone", "b-card category_product").parse_items()
res = FilterItems(all_cards).items_to_dict()
messages = format_message(res)

async def main():
    tasks = [send_message(message) for message in messages]
    await asyncio.gather(*tasks)

asyncio.run(main())

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

# from bs4 import BeautifulSoup
# import time


# path_to_driver = ChromeDriverManager().install()
# service = Service(executable_path=path_to_driver)
# driver = webdriver.Chrome(service=service)


# driver.get("https://i-ray.ru/iphone")

# time.sleep(5)

# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")

# cards = soup.find_all(class_="b-card category_product")

# for card in cards:
#     print(card.prettify())

# driver.quit()