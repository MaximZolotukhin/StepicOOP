"""
1.4 Методы классов. Параметр self

Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/ljahVEppmxM

Подвиг 9. Из входного потока читаются строки данных с помощью команды:

lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока

в формате: id, name, old, salary (записанные через пробел). Например:

1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200
...

То есть, каждая строка - это элемент списка lst_in.

Необходимо в класс DataBase:

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

добавить два метода:

insert(self, data) - для добавления в список lst_data новых данных из переданного списка строк data;
select(self, a, b) - возвращает список из элементов списка lst_data в диапазоне [a; b] (включительно)
по их индексам (не id, а индексам списка); также учесть, что граница b может превышать длину списка.

Каждая запись в списке lst_data должна быть представлена словарем (добавление с помощью метода insert) в формате:
{'id': 'номер', 'name': 'имя', 'old': 'возраст', 'salary': 'зарплата'}

Например:
{'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'}

Примечание: в этой задаче число элементов в строке (разделенных пробелом) всегда совпадает с числом полей в коллекции FIELDS.

P. S. Ваша задача только добавить два метода в класс DataBase.

Sample Input:
1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200
"""

import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def insert(self, data):
        """
        Функция преобразовывает данные из потокового ввода в вложенный списко и возвращает
        словарь с данными
        :param data:
        :return:
        """
        date_out = [[x for x in out.split()] for out in data] # Разиваю даныне на отдельные списки

        for val_in in date_out:
            # self.lst_data.append({self.FIELDS[index_in]:value for index_in, value in enumerate(val_in)})
            self.lst_data.append(dict(zip(self.FIELDS, val_in)))

        # return self.lst_data

    def select(self, a, b):
        try:
            if len(self.lst_data) >= a and len(self.lst_data) >= b:
                return self.lst_data[a:b+1]
        except:
            print(f"привышен диапазон хранимых данный, максимальный диапазон равен {len(self.lst_data)}")


db = DataBase()
db.insert(lst_in)
print(db.select(0, 2))
