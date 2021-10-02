from framework.pages.user_page import UserPage
from framework.pages.login_page import LoginPage
from framework.pages.admin_page import AdminPage


class UIWorker(UserPage, LoginPage, AdminPage):
    """Класс через наследование работает со всеми экранами"""
    """Метод для открытия нужного экрана"""
    def open_screen(self, url='https://google.com'):
        self.open_page(url)
    """def open_screen(self, url='http://localhost:8000/'):
        self.open_page(url)"""
