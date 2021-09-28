import json
import requests


class ApiChecker:
    @staticmethod
    def check_body(expected_result, result):
        assert expected_result == result
        print(f'exp: {expected_result} act: {result}')

    @staticmethod
    def check_status(expected_result, result):
        assert expected_result == result
        print(f'status code: exp:{expected_result} act:{result}')


class APIClient:

    def __init__(self):
        self.url = 'https://petstore.swagger.io/'
        self.headers = {'Content-Type': 'application/json'}

    def method_post_and_check_body(self, url, expected_result=None, body=None):
        result = requests.post(url, data=json.dumps(body), headers=self.headers)
        ApiChecker.check_body(expected_result, result.json())

    def method_get_and_check_status(self, url, expected_result=None):
        if expected_result is None:
            expected_result = 200
        result = requests.get(url, headers=self.headers)
        ApiChecker.check_status(expected_result, result.status_code)

    def method_get_and_check_body(self, url, expected_result=None):
        result = requests.get(url, headers=self.headers)
        ApiChecker.check_body(expected_result, result.json())

    def method_delete_and_check_status(self, url, expected_result=None):
        if expected_result is None:
            expected_result = 200
        result = requests.delete(url, headers=self.headers)
        ApiChecker.check_status(expected_result, result.status_code)
