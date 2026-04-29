from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from src.modules.beautifulsoup.utils.constants_urls import BASE


def iniciar_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.get(BASE)
    wait = WebDriverWait(driver, 10)

    return driver, wait


def get_element(wait, selector, by=By.CSS_SELECTOR):
    return wait.until(
        EC.visibility_of_element_located((by, selector))
    )


def find_click(wait, selector, by=By.CSS_SELECTOR):
    element = wait.until(
        EC.element_to_be_clickable((by, selector))
    )
    element.click()


def find_tap(wait, selector, text="", by=By.CSS_SELECTOR):
    element = get_element(wait, selector, by)
    element.clear()
    element.send_keys(str(text))


def select_option(wait, selector, value, by=By.ID, mode="value"):
    element = wait.until(
        EC.visibility_of_element_located((by, selector))
    )
    select = Select(element)

    if mode == "value":
        select.select_by_value(str(value))
    elif mode == "text":
        select.select_by_visible_text(str(value))
    elif mode == "index":
        select.select_by_index(int(value))