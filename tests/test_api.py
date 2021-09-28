from framework.api_helpers.expected_results import CollectionExpectedResult as ER


def test_api_create_user(api_client):
    api_client.func_create_user(ER.CREATE_USER_RESPONSE)
    api_client.func_login_user()
    api_client.func_get_user_info(ER.GET_USER_INFO_RESPONSE)
    api_client.func_logout_user(ER.LOGOUT_RESPONSE)
    api_client.delete_user()
