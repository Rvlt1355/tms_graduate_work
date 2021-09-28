from framework.db_client import ClientDB


def test_create_group(pages, db_client):
    pages.login_user('admin', 'password')
    pages.find_group_in_table()


def test_create_user(pages, db_client):
    db = ClientDB()
    pages.login_user('admin', 'password')
    pages.open_add_user_page()
    pages.add_user()
    pages.choose_group_user_and_save()
    db.check_add_user_in_group()
