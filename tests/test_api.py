import allure
from framework.api_helpers.expected_results import CollectionExpectedResult as ER


@allure.feature('Тест API')
def test_api_create_user(api_client):
    with allure.step('Create user'):
        api_client.func_create_user(ER.CREATE_USER_RESPONSE)
    with allure.step('Login test user'):
        api_client.func_login_user()
    with allure.step('Get info test user'):
        api_client.func_get_user_info(ER.GET_USER_INFO_RESPONSE)
    with allure.step('Logout'):
        api_client.func_logout_user(ER.LOGOUT_RESPONSE)
    with allure.step('Delete user'):
        api_client.delete_user()
