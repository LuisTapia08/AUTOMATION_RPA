from src.shared.functions import find_tap, find_click
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Navigation:
    def __init__(self, wait):
        self.wait = wait

    def realizar_login(self, user):
        find_tap(self.wait, '[data-qa="login-email"]', user["Email"])
        find_tap(self.wait, '[data-qa="login-password"]', user["password"])
        find_click(self.wait, '[data-qa="login-button"]')

    def realizar_logout(self):
        logout_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/logout"]'))
        )
        print(f"Navegando para: {logout_link.text}")
        logout_link.click()
        print("O botão de logout foi clicado. Logout realizado")

    def go_tests_cases(self):
        testcase_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/test_cases"]'))
        )
        print(f"Navegando para: {testcase_link.text}")
        testcase_link.click()
        print("O botão de logout foi clicado. Logout realizado")