"""
1.7 Методы класса (classmethod) и статические методы (staticmethod)

Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/9766M0dS1qc

Подвиг 8. Объявите класс CardCheck для проверки корректности информации на пластиковых картах.
Этот класс должен иметь следующие методы:

check_card_number(number) - проверяет строку с номером карты и возвращает булево значение True, если номер в
верном формате и False - в противном случае. Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9).
check_name(name) - проверяет строку name с именем пользователя карты. Возвращает булево значение True,
если имя записано верно и False - в противном случае.

Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными латинскими символами и цифрами. Например, SERGEI BALAKIREV.

Предполагается использовать класс CardCheck следующим образом (эти строчки в программе не писать):

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")

Для проверки допустимых символов в классе должен быть прописан атрибут:

CHARS_FOR_NAME = ascii_lowercase.upper() + digits

Подумайте, как правильнее объявить методы check_card_number и check_name (декораторами @classmethod и @staticmethod).

P.S. В программе только объявить класс. На экран ничего выводить не нужно.
"""
from string import ascii_lowercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits + '-'

    @classmethod
    def check_card_number(cls, number):
        res = number[4] == '-' and number[9] == '-'  and number[14] == '-' and len(number) == 19 and number.replace('-','').isdigit() # and number[4:15:5] == '-'
        return res

    @classmethod
    def check_name(cls, name):
        list_name = list(name.split(' '))
        if len(list_name) == 2 and all(map(lambda x: x in cls.CHARS_FOR_NAME, name.replace(' ',''))):
            return True
        else:
            return False


is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")

print(is_number)
print(is_name)


