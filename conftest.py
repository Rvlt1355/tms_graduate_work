import pytest
from selenium import webdriver
from framework.db_client import ClientDB
from framework.pages import UIWorker
from framework.api_helpers.api_functionality import FuncApi


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
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
    yield db
    db.close_connect()


"""Фикстура для очистки auth_group"""


@pytest.fixture
def trunc_table_auth_group(db_client):
    yield
    db_client.trunc_table_auth_group()


"""Фикстура для удаления определенного пользователя"""


@pytest.fixture
def delete_test_user_in_auth_user(db_client):
    yield
    db_client.delete_test_user()


"""Фикстура удаляет всех тестовых пользователей в auth_user 
    кроме суперпользователя admin"""


@pytest.fixture
def delete_users_in_auth_user(db_client):
    yield
    db_client.delete_users_not_admin_in_auth_user()


@pytest.fixture
def api_client():
    api_client = FuncApi()
    return api_client

