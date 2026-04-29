from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.shared import functions
from selenium.common.exceptions import TimeoutException

class User:
    def __init__(self):
        self.driver, self.wait = functions.iniciar_driver()
    def ir_para_login(self):
        login_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/login"]'))
        )
        print(f"Navegando para: {login_link.text}")
        login_link.click()

    def selecionar_mr(self):
        functions.find_click(self.wait, 'label[for="id_gender1"]')

    def realizar_signup(self, user):
        functions.find_tap(self.wait, '[name="name"]', user["Name"], by=By.CSS_SELECTOR)
        functions.find_tap(self.wait, '[data-qa="signup-email"]', user["Email"], by=By.CSS_SELECTOR)
        functions.find_click(self.wait, 'button[data-qa="signup-button"]')
        print("Botão Signup clicado!")

    def usuario_ja_existe(self):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[contains(text(), 'already exist')]")
                )
            )
            return True
        except:
            return False

    def preencher_conta(self, user):
        functions.find_tap(self.wait, '[data-qa="password"]', user["password"])

        functions.select_option(self.wait, "days", user["birthday"], mode="value")
        functions.select_option(self.wait, "months", user["birthmonth"], mode="text")
        functions.select_option(self.wait, "years", user["birthyear"], mode="value")

        if user["Singin"]:
            functions.find_click(self.wait, "#newsletter")

        if user["Receive"]:
            functions.find_click(self.wait, "#optin")

    def preencher_endereco(self, user):
        functions.find_tap(self.wait, "#first_name", user["First Name"])
        functions.find_tap(self.wait, "#last_name", user["Last Name"])
        functions.find_tap(self.wait, "#address1", user["Address"])
        functions.select_option(self.wait, "country", user["Country"], mode="text")
        functions.find_tap(self.wait, "#state", user["State"])
        functions.find_tap(self.wait, "#city", user["City"])
        functions.find_tap(self.wait, "#zipcode", user["Zipcode"])
        functions.find_tap(self.wait, "#mobile_number", user["phone"])

    def criar_conta(self):
        functions.find_click(self.wait, '[data-qa="create-account"]')
        continue_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="continue-button"]'))
        )
        continue_link.click()
        print('O botão foi clicado')


    def delete_account(self):
        delete_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/delete_account"]'))
        )
        print(f"Navegando para: {delete_link.text}")
        delete_link.click()
        continue_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="continue-button"]'))
        )
        continue_link.click()
        print('O botão foi clicado')
        
    def fechar_ads(self, wait):
        try:
            close_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[text()[contains(., 'Close')]]"))
            )
            close_btn.click()
            print("Ad fechado")
        except TimeoutException:
            print("Nenhum ad apareceu")