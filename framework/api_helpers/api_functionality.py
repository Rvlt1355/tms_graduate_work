from framework.api_helpers.api_client import APIClient


class FuncApi(APIClient):
    def __init__(self):
        super().__init__()
        self.test_username = "tester"
        self.first_name = "firstName"
        self.last_name = "lastName"
        self.email = "test@test.com"
        self.passwd = "password"
        self.phone = "1234567890"

    def func_create_user(self, expected_result):
        url = self.url + 'v2/user'
        body = {
                  "id": 1,
                  "username": self.test_username,
                  "firstName": self.first_name,
                  "lastName": self.last_name,
                  "email": self.email,
                  "password": self.passwd,
                  "phone": self.phone,
                  "userStatus": 1
                }
        self.method_post_and_check_body(url, expected_result, body)

    def func_login_user(self, user_name=None, paswd=None):
        if user_name is None and paswd is None:
            user_name = self.test_username
            paswd = self.passwd
        url = f'{self.url}v2/user/login?username={user_name}&password={paswd}'
        self.method_get_and_check_status(url)

    def func_get_user_info(self, expected_result):
        url = f'{self.url}v2/user/{self.test_username}'
        self.method_get_and_check_body(url, expected_result)

    def func_logout_user(self, expected_result):
        url = f'{self.url}v2/user/logout'
        self.method_get_and_check_body(url, expected_result)

    def delete_user(self, user_name=None):
        if user_name is None:
            user_name = self.test_username
        url = f'{self.url}v2/user/{user_name}'
        self.method_delete_and_check_status(url)
