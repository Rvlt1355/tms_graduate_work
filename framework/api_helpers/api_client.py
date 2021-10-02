import json
import requests
from time import sleep


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
    default_status_code = 200
    GET = 'get'
    POST = 'post'
    DELETE = 'delete'

    def __init__(self):
        self.url = 'https://petstore.swagger.io/'
        self.headers = {'Content-Type': 'application/json'}

    def post(self, url, expected_result: dict = None, body: dict = None,  retry_attempts=0, retry_delay=1):
        if not expected_result:
            expected_result = self.default_status_code
        for retry_attempt in range(retry_attempts + 1):
            try:
                result = requests.post(url, data=json.dumps(body), headers=self.headers)
                ApiChecker.check_status(expected_result, result.status_code)
            except:
                if retry_attempt < retry_attempts:
                    sleep(retry_delay)
                    continue

    def get(self, url, expected_result=None, retry_attempts=0, retry_delay=1):
        if not expected_result:
            expected_result = self.default_status_code
        for retry_attempt in range(retry_attempts + 1):
            try:
                result = requests.get(url, headers=self.headers)
                ApiChecker.check_status(expected_result, result.status_code)
            except:
                if retry_attempt < retry_attempts:
                    sleep(retry_delay)
                    continue

    def delete(self, url, expected_result=None, retry_attempts=0, retry_delay=1):
        if not expected_result:
            expected_result = self.default_status_code
        for retry_attempt in range(retry_attempts + 1):
            try:
                result = requests.delete(url, headers=self.headers)
                ApiChecker.check_status(expected_result, result.status_code)
            except:
                if retry_attempt < retry_attempts:
                    sleep(retry_delay)
                    continue
