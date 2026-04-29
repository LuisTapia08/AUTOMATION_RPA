from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.modules.beautifulsoup.utils.constants_urls import BASE


class Products:
    def __init__(self, wait):
        self.wait = wait

    def ir_para_products(self):
        produto_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/products"]'))
        )
        print(f"Navegando para: {produto_link.text}")
        produto_link.click()

        