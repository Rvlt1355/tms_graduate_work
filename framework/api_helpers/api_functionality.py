from framework.api_helpers.api_client import APIClient


class FuncApi(APIClient):
    def __init__(self):
        super().__init__()
        self.first_name = "firstName"
        self.last_name = "lastName"
        self.email = "test@test.com"
        self.phone = "1234567890"

    def create_user(self, id: int = None, username: str = None,
                    passwd: str = None, expected_result: dict = None):
        url = self.url + 'v2/user'
        body = {
                  "id": int(id),
                  "username": username,
                  "firstName": self.first_name,
                  "lastName": self.last_name,
                  "email": self.email,
                  "password": passwd,
                  "phone": self.phone,
                  "userStatus": 1
                }
        self.post(url, expected_result, body)

    def login_user(self, user_name='', paswd=''):
        url = f'{self.url}v2/user/login?username={user_name}&password={paswd}'
        self.get(url, retry_attempts=0, retry_delay=2)

    def check_user_info(self, uname, expected_result: dict = None):
        url = f'{self.url}v2/user/{uname}'
        self.get(url, expected_result, retry_attempts=1, retry_delay=2)

    def logout_user(self, expected_result: dict = None):
        url = f'{self.url}v2/user/logout'
        self.get(url, expected_result)

    def delete_user(self, uname: str):
        """if user_name is None:
            user_name = self.test_username"""
        url = f'{self.url}v2/user/{uname}'
        self.delete(url, retry_attempts=1, retry_delay=2)
