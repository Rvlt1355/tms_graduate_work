from framework.pages.user_page import UserPage
from framework.pages.login_page import LoginPage
from framework.pages.admin_page import AdminPage


class UIWorker(UserPage, LoginPage, AdminPage):
    """Класс для работы со всеми экранами приложения"""
    def open_screen_app(self, url='http://localhost:8000/'):
        self.open_page(url)
