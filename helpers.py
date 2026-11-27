import random


# Генератор уникального email
def generate_email():
    number = random.randint(100, 999)
    return f"yaroslav_naumenko_59_{number}@yandex.ru"


# Генератор пароля
def generate_password():
    return "Test123456"