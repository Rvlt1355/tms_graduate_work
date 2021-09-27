def test_create_group(pages, db_client):
    pages.login_user('admin', 'password')
    pages.find_group_in_table()


def test_create_user(pages):
    pages.login_user('admin')
    pages.open_add_user_page()
    pages.add_user()
    pages.choose_group_user()

