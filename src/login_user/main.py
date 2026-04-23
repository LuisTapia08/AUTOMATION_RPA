from src.shared.functions import find_tap, find_click

class LoginUser:
    def __init__(self, wait):
        self.wait = wait

    def realizar_login(self, user):
        find_tap(self.wait, '[data-qa="login-email"]', user["Email"])
        find_tap(self.wait, '[data-qa="login-password"]', user["password"])
        find_click(self.wait, '[data-qa="login-button"]')
