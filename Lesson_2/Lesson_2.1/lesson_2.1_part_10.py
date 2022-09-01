"""
2.1 Режимы доступа public, private, protected. Сеттеры и геттеры


Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/HPgJtLb2NV8

Подвиг 10 (на повторение). Объявите класс EmailValidator для проверки корректности email-адреса. Необходимо запретить создание объектов этого класса: при создании экземпляров должно возвращаться значение None, например:

em = EmailValidator() # None

В самом классе реализовать следующие методы класса (@classmethod):

get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка);
check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае.

Корректность строки email определяется по следующим критериям:

- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.

Также в классе нужно реализовать приватный статический метод класса:

is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.

Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email. Если параметр email не является строкой, то check_email() возвращает False.

Пример использования класса EmailValidator (эти строчки в программе писать не нужно):

res = EmailValidator.check_email("sc_lib@list.ru") # True
res = EmailValidator.check_email("sc_lib@list_ru") # False

P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.
"""
import random
import string
import re

class EmailValidator:
    regex = re.compile(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    )

    def __new__(cls, *args, **kwargs):
        pass

    def __init__(self):
        self.length = int(random.random())

    def generate_random_string(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(self.length))
        return rand_string

    @classmethod
    def get_random_email(cls):
        email = EmailValidator.generate_random_string()
        return email

    @classmethod
    def check_email(cls, email):
        if
            if email in cls.regex:
                return True


    @staticmethod
    def is_email_str(email):
        if type(email) == str:
            return True
        else:
            return False




em = EmailValidator()
