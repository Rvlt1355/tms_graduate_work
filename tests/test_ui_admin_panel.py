import allure
import framework.random_values as rm_values


@allure.story('UI тесты')
@allure.feature('Тест на создание группы')
def test_create_group(pages, db_client, trunc_table_auth_group):
    group_id = rm_values.generator_id()
    group_name = rm_values.generator_name()
    with allure.step('Создаем группу в БД'):
        db_client.insert_auth_group(group_id,
                                    group_name)
    with allure.step('Логинимся админом в приложениии'):
        pages.login_user('admin', 'password')
    with allure.step('Открываем страницу с группами и ищем название созданной группы'):
        pages.find_group_in_table(group_name)

@allure.story('UI тесты')
@allure.feature('Тест на создание и добавление пользователя в группу')
def test_create_user_and_add_group(pages, db_client,
                                   delete_test_user_in_auth_user,
                                   trunc_table_auth_group):
    group_id = rm_values.generator_id()
    group_name = rm_values.generator_name()
    user_name = rm_values.generator_name()
    with allure.step('Создаем группу в БД'):
        db_client.insert_auth_group(group_id, group_name)
    with allure.step('Логинимся админом в приложениии'):
        pages.login_user('admin', 'password')
    with allure.step('Переходим на страницу создания пользователя'):
        pages.open_add_user_page()
    with allure.step('Создаем тестового пользователя'):
        pages.add_user(user_name)
    with allure.step('Открываем страницу пользователя и добавляем в группу'):
        pages.select_and_add_user_to_the_group()
    with allure.step('Проверяем что пользователь добавлен в группу'):
        db_client.check_add_user_in_group(group_id, user_name)

