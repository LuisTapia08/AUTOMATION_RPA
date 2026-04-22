from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from src.constants.url import URL
from src.modules.mock import mockuser


class User:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(URL)
        self.wait = WebDriverWait(self.driver, 10)
        self.wait = WebDriverWait(self.driver, 10)

    def ir_para_login(self):
        login_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/login"]'))
        )
        print(f"Navegando para: {login_link.text}")
        login_link.click()

    def selecionar_mr(self):
        self.find_click('label[for="id_gender1"]')


    def realizar_signup(self, user):
        campo_nome = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "name"))
        )
        campo_email = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-qa="signup-email"]'))
        )

        campo_nome.clear()
        campo_nome.send_keys(user["Name"])

        campo_email.clear()
        campo_email.send_keys(user["Email"])

        botao_signup = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="signup-button"]'))
        )
        botao_signup.click()
        print("Botão Signup clicado!")

    def get_element(self, selector, by=By.CSS_SELECTOR):
        return self.wait.until(
            EC.visibility_of_element_located((by, selector))
        )

    def find_click(self, selector, by=By.CSS_SELECTOR):
        element = self.get_element(selector, by)
        element.click()

    def find_tap(self, selector, text="", by=By.CSS_SELECTOR):
        element = self.get_element(selector, by)
        element.clear()
        element.send_keys(str(text))

    def select_date(self, selector, value, by=By.ID, mode="value"):
        element = self.wait.until(
            EC.visibility_of_element_located((by, selector))
        )
        select = Select(element)

        if mode == "value":
            select.select_by_value(str(value))
        elif mode == "text":
            select.select_by_visible_text(str(value))
        elif mode == "index":
            select.select_by_index(int(value))

    def preencher_conta(self, user):
        self.find_tap('[data-qa="password"]', user["password"])

        self.select_date("days", user["birthday"], mode="value")
        self.select_date("months", user["birthmonth"], mode="text")
        self.select_date("years", user["birthyear"], mode="value")

        if user["Singin"]:
            self.find_click("#newsletter")

        if user["Receive"]:
            self.find_click("#optin")

    def preencher_endereco(self, user):
        self.find_tap("#first_name", user["First Name"], by=By.CSS_SELECTOR)
        self.find_tap("#last_name", user["Last Name"], by=By.CSS_SELECTOR)
        self.find_tap("#address1", user["Address"], by=By.CSS_SELECTOR)
        self.find_tap("#state", user["State"], by=By.CSS_SELECTOR)
        self.find_tap("#city", user["City"], by=By.CSS_SELECTOR)
        self.find_tap("#zipcode", user["Zipcode"], by=By.CSS_SELECTOR)
        self.find_tap("#mobile_number", user["phone"], by=By.CSS_SELECTOR)
        
    def select_country(self, selector, user, by=By.ID, mode="text"):
        self.select_date("country", user["Country"], mode="text")

        self.find_tap("#state", user["State"], by=By.CSS_SELECTOR)
        self.find_tap("#city", user["City"], by=By.CSS_SELECTOR)
        self.find_tap("#zipcode", user["Zipcode"], by=By.CSS_SELECTOR)
        self.find_tap("#mobile_number", user["phone"], by=By.CSS_SELECTOR)

    def criar_conta(self):
        self.find_click('[data-qa="create-account"]')
