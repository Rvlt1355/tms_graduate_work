from framework.pages.base_page import Page
from framework.pages.admin_page import AdminPage
from framework.locators import locators as lc


class UserPage(Page):
    def add_user(self, user_name='Username',paswd='Password123QWE',
                 confirm_paswd='Password123QWE'):
        self.find_and_input(user_name, lc.INPUT_USER_NAME)
        self.find_and_input(paswd, lc.INPUT_PASSWORD)
        self.find_and_input(confirm_paswd, lc.INPUT_PASSWORD_CONFIRM)
        self.find_and_click(lc.BUTTON_SAVE)

    def choose_group_user(self):
        self.select_item_element(lc.GROUPS_FORM, 1)
        self.find_and_click(lc.BUTTON_CHOOSE)
