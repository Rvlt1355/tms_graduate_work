from framework.pages.base_page import Page
from framework.locators import locators as lc


class LoginPage(Page):
    def input_user_name(self, username):
        self.find_and_input(username, lc.INPUT_LOGIN)

    def input_password(self, passwd):
        self.find_and_input(passwd, lc.INPUT_PASSWD)

    def click_login(self):
        self.find_and_click(lc.BUTTON_LOGIN)

    def go_to_admin_page(self):
        self.find_and_click(lc.BUTTON_GO_TO_ADMIN)

    def login_user(self, username='admin', password='password'):
        self.go_to_admin_page()
        self.input_user_name(username)
        self.input_password(password)
        self.click_login()
