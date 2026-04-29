import csv
import src.modules.beautifulsoup.utils.constants as C

class DataHandler:
    def __init__(self, data):
        self.data = data

    def save(self):
        with open(C.FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "nome", "preco", "link"])
            writer.writeheader()
            writer.writerows(self.data)