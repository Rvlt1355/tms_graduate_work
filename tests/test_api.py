import allure
from framework.api_helpers.expected_results import CollectionExpectedResult as ER
from time import sleep


@allure.feature('Тест API')
def test_api_create_user(api_client):
    with allure.step('Создаем пользователя'):
        api_client.func_create_user(ER.CREATE_USER_RESPONSE)
        sleep(3)
    with allure.step('Логинимся тестовым пользователем'):
        api_client.func_login_user()
    with allure.step('Получаем данные пользователя'):
        api_client.func_get_user_info(ER.GET_USER_INFO_RESPONSE)
    with allure.step('Логаут пользователем'):
        api_client.func_logout_user(ER.LOGOUT_RESPONSE)
    with allure.step('Удаляем пользоваетеля'):
        api_client.delete_user()
