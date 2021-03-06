from framework.pages.base_page import Page
from framework.locators import locators as lc


class UserPage(Page):
    def add_user(self, user_name='Testuser', paswd='Password123QWE',
                 confirm_paswd='Password123QWE'):
        self.find_and_input(user_name, lc.INPUT_USER_NAME)
        self.find_and_input(paswd, lc.INPUT_PASSWORD)
        self.find_and_input(confirm_paswd, lc.INPUT_PASSWORD_CONFIRM)
        self.find_and_click(lc.BUTTON_SAVE)

    def select_and_add_user_to_the_group(self):
        """Добавляем группу для пользователя из списка доступных
        И сохраняем изменения
        """
        self.find_and_click(lc.GROUPS_TABLE)
        self.find_and_click(lc.GROUP_IN_TABLE)
        self.find_and_click(lc.ACTIVATION_GROUP_USER)
        self.find_and_click(lc.BUTTON_SAVE)
