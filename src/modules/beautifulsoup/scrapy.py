import src.modules.beautifulsoup.utils.constants_selectores as SELECTOR
import src.modules.beautifulsoup.utils.constants_urls as URL

class Action:
    def __init__(self, data: list):
        self.data = data
        self.items = []

    def extract(self):
        for card in self.data:
            name = card.select_one(SELECTOR.NAME)
            price = card.select_one(SELECTOR.PRICE)
            button = card.select_one(SELECTOR.ADD_BUTTON)
            link = card.select_one(SELECTOR.LINK)

    
            if link:
                item = self.build_item(button, name, price, link)
                print(item)
                self.populate_item(item=item)

    def build_item(self, button, name, price, link):
        return {
            "id": button.get("data-product-id"),
            "nome": name.get_text(strip=True),
            "preco": price.get_text(strip=True),
            "link": URL.BASE + link.get("href")
        }
        
    def populate_item(self, item):
        self.items.append(item)