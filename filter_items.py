class FilterItems:
    def __init__(self, all_cards) -> None:
        self.all_cards = all_cards
        self.res : list = []

    def items_to_dict(self):
        for card in self.all_cards:
            title_el = card.find("span", itemprop="name")
            title = title_el.get_text(strip=True) if title_el else None

            price_el = card.find("div", class_="prise_block").find("p")
            price = price_el.get_text(strip=True) if price_el else None

            if price and title and price != "Предзаказ":
                self.res.append({"name": title, "price": price}) 
            else:
                print(f"У элемента {card} нет цены или названия")
        return self.res