from framework.pages.base_page import Page
from framework.locators import locators as lc


class AdminPage(Page):
    def open_groups_page(self):
        self.find_and_click(lc.BUTTON_GROUPS)

    def click_group(self):
        self.find_and_click(lc.GROUPS_NAME)

    def find_title_group(self):
        self.find_element(lc.GROUPS_TITLE)

    def find_group_in_table(self, group_name="Test"):
        """Метод открывает страницу с группами ищет группу
        и сравнивает с созданной"""
        self.open_groups_page()
        self.find_and_chek_text(lc.GROUPS_NAME, group_name)

    def open_group(self):
        self.open_groups_page()
        self.click_group()
        self.find_title_group()

    def open_add_user_page(self):
        self.find_and_click(lc.USER_ADD)
