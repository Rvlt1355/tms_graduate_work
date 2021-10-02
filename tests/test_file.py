from framework.locators import locators as lc
from selenium.webdriver.common.by import By


def test_google(pages):
    pages.find_element(By.CSS_SELECTOR('[alt="Google"]'))