import random
import string


def generator_id():
    # Генератор для id возвращает строку
    return ''.join(random.choice(string.digits) for i in range(2))


def generator_name():
    # Генератор для имени возвращает строку
    return ''.join(random.choice(string.ascii_letters) for i in range(10))


def generator_pswd():
    # Генератор для пароля возвращает строку, доработать шаблон
    template_password = f"{string.digits}{string.ascii_letters}!$&()?"
    return ''.join(random.choice(template_password) for i in range(10))
