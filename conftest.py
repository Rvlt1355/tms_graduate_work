import pytest
from selenium import webdriver
from framework.db_client import ClientDB
from framework.pages import UIWorker
from framework.api_helpers.api_functionality import FuncApi


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(4)
    yield driver
    driver.quit()


@pytest.fixture()
def pages(driver):
    """Воркер получает все экраны и работает с ними"""
    page = UIWorker(driver)
    page.open_screen()
    return page


@pytest.fixture
def db_client():
    db = ClientDB()
    db.insert_auth_group()
    yield db_client
    db.trunc_table_auth_group()
    db.close_connect()


@pytest.fixture
def api_client():
    api_client = FuncApi()
    return api_client