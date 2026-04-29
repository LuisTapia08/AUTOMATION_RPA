from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.shared import functions



class ContactUs:
    def __init__(self, wait):
        self.wait = wait

    def ir_para_contact(self):
        contact_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/contact_us"]'))
        )
        print(f"Navegando para: {contact_link.text}")
        contact_link.click()

    def preencher_formulario(self, user, mensagem):
        functions.find_tap(self.wait, '[data-qa="name"]', user["Name"])
        functions.find_tap(self.wait, '[data-qa="email"]', user["Email"])
        functions.find_tap(self.wait, '[data-qa="subject"]', "Suporte Automação")
        functions.find_tap(self.wait, '[data-qa="message"]', mensagem)
        file_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]'))
        )
        file_input.send_keys(r"C:\Users\etech\Desktop\luis\AUTOMATION_RPA\banner-reclamacoes.png")

    def enviar(self):
        functions.find_click(self.wait, '[data-qa="submit-button"]')

        
        alert = self.wait._driver.switch_to.alert
        alert.accept()

        print("Formulário enviado!")

    def validar_sucesso(self):
        success_msg = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".status.alert.alert-success")
            )
        )
        print("Mensagem de sucesso:", success_msg.text)
