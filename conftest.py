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
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(4)
    yield driver
    driver.quit()


@pytest.fixture()
def pages(driver):
    """Воркер получает все экраны и работает с ними"""
    page = UIWorker(driver)
    page.open_screen_app()
    return page


@pytest.fixture
def db_client():
    db = ClientDB()
    yield db
    db.close_connect()


@pytest.fixture
def trunc_table_auth_group(db_client):
    """Фикстура для очистки таблицы auth_group"""
    yield
    db_client.trunc_table_auth_group()


@pytest.fixture
def delete_test_user_in_auth_user(db_client):
    """
    Фикстура для удаления определенного пользователя
    в таблице auth_user"""

    yield
    db_client.delete_test_user()


@pytest.fixture
def delete_users_in_auth_user(db_client):
    """Фикстура удаляет всех тестовых пользователей
    в auth_user кроме суперпользователя admin
    Использовать для api тестов"""
    yield
    db_client.delete_users_not_admin_in_auth_user()


@pytest.fixture
def api_client():
    """Фикстура для работы с веб-ервисами приложения"""
    api_client = FuncApi()
    return api_client

