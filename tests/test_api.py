import allure
import framework.random_values as rm_values


@allure.feature('Тест API')
def test_api_create_user(api_client, delete_users_in_auth_user):
    paswd = rm_values.generator_pswd()
    user_name = rm_values.generator_name()
    id = rm_values.generator_id()
    with allure.step('Create user'):
        api_client.create_user(id, user_name, paswd)
    with allure.step('Login test user'):
        api_client.login_user(user_name, paswd)
    with allure.step('Check user_info'):
        api_client.check_user_info(user_name)
    with allure.step('Logout'):
        api_client.logout_user()
    with allure.step('Delete user'):
        api_client.delete_user(user_name)
