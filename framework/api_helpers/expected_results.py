class CollectionExpectedResult:
    CREATE_USER_RESPONSE = {
                      "code": 200,
                      "type": "unknown",
                      "message": "1"
                      }

    LOGOUT_RESPONSE = {
                          "code": 200,
                          "type": "unknown",
                          "message": "ok"
                        }

    GET_USER_INFO_RESPONSE = {
        "id": 1,
        "username": "tester",
        "firstName": "firstName",
        "lastName": "lastName",
        "email": "test@test.com",
        "password": "password",
        "phone": "1234567890",
        "userStatus": 1
    }