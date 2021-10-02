import random
import string


def generator_id():
    return ''.join(random.choice(string.digits) for i in range(7))


def generator_name():
    return ''.join(random.choice(string.ascii_letters) for i in range(10))
