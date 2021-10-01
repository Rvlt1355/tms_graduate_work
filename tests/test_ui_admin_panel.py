import allure


@allure.feature('Тест на создание группы')
def test_create_group(pages, db_client, insert_test_group):
    with allure.step('Создаем группу в бд'):
        insert_test_group(db_client)
    with allure.step('Логинимся админом в приложениии'):
        pages.login_user('admin', 'password')
    with allure.step('Открываем страницу с группами и ищем название созданной группы'):
        pages.find_group_in_table()


@allure.feature('Тест на создание и добавление пользователя в группу')
def test_create_user_and_add_group(pages, db_client, create_user_in_auth_group_bd,
                                   check_user_in_group):
    with allure.step('Создаем группу пользователю'):
        create_user_in_auth_group_bd(db_client)
    with allure.step('Логинимся админом в приложениии'):
        pages.login_user('admin', 'password')
    with allure.step('Переходим на страницу создания пользователя'):
        pages.open_add_user_page()
    with allure.step('Создаем тестового пользователя'):
        pages.add_user()
    with allure.step('Открываем страницу пользователя и добавляем в группу'):
        pages.choose_group_user_and_save()
    with allure.step('Проверяем что пользователь добавлен в группу'):
        check_user_in_group(db_client)

