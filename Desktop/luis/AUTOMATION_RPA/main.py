from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://automationexercise.com"

class User:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)
        self.wait = WebDriverWait(self.driver, 10)

    def ir_para_login(self):
        login_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/login"]')))
        print(f"Navegando para: {login_link.text}")
        login_link.click()

    def realizar_signup(self, nome, email):
        campo_nome = self.wait.until(EC.visibility_of_element_located((By.NAME, 'name')))
        campo_email = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-qa="signup-email"]')))
        
        campo_nome.clear()
        campo_nome.send_keys(nome)
        sleep(1) 
        
        campo_email.clear()
        campo_email.send_keys(email)
        sleep(1)
  
        botao_signup = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="signup-button"]')))
        botao_signup.click()
        print("Botão Signup clicado!")

    def get_element(self, selector, by=By.CSS_SELECTOR):
        return self.wait.until(EC.visibility_of_element_located((by, selector)))
    
    def find_click(self, selector, by=By.CSS_SELECTOR):
        element = self.get_element(selector, by)
        element.click()

    def find_tap(self, selector, text='', by=By.CSS_SELECTOR):
        element = self.get_element(selector, by)
        element.clear()
        element.send_keys(text)

if __name__ == "__main__":
    usuario = User()
    usuario.ir_para_login()
    usuario.realizar_signup("Luis Sousa", "luissousa@teste.com")
    
    sleep(5)
    usuario.driver.quit()