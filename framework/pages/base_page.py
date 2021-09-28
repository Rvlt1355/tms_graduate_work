from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class Page:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator))

    def find_and_input(self, text: str, locator: str, time=5):
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator)).send_keys(text)

    def find_and_click(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)).click()

    def find_and_chek_text(self, locator, text, time=4):
        return WebDriverWait(self.driver, time).until(
            EC.text_to_be_present_in_element(locator, text))

    """Возвращает None при поиске нужно разобраться"""
    def select_item_element(self, locator):
        selected = Select(self.find_element(locator))
        return print(selected.select_by_visible_text('Test'))
