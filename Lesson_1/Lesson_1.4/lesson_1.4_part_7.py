"""
1.4 Методы классов. Параметр self

Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/IxXtZXrnnDY

Подвиг 7. Имеется следующий класс для считывания информации из входного потока:
import sys

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res

Которым, затем, можно воспользоваться следующим образом:
sr = StreamReader()
data, result = sr.readlines()

Необходимо перед классом StreamReader объявить еще один класс StreamData с методом:
def create(self, fields, lst_values): ...

который бы на входе получал список FIELDS из названий локальных атрибутов (передается в атрибут fields) и список строк
lst_in (передается в атрибут lst_values) и формировал бы в объекте класса StreamData локальные свойства с именами полей
из fields и соответствующими значениями из lst_values.

Если создание локальных свойств проходит успешно, то метод create() возвращает True, иначе - False.
Если число полей и число строк не совпадает, то метод create() возвращает False и локальные атрибуты создавать не нужно.

P.S. В программе нужно дополнительно объявить только класс StreamData. Больше ничего делать не нужно.
Пример входной информации (Sample Input):
10
Питон - основы мастерства
512
"""
import sys

# здесь объявляется класс StreamData
import sys

# здесь объявляется класс StreamData
class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False

        for index, key in enumerate(fields):
            setattr(self, key, lst_values[index])

        return True

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()

"""
Понимал условие задачи я около часа, причем при помощи комментов. Сейчас попробую пояснить моменты которые мне были не понятны. 
Причем автор очень классно объясняет тему урока, прямо максимально понятно все и последовательно. 
Как при этом этот человек так плохо формулирует условия к задачам для меня остается загадка)))

Что мы имеем по исходным данным:
1. переменные lst_in и FIELDS уже созданы в классе StreamReaders. Я не сразу обратил на это внимание и подумал 
что их надо как-то создавать.
Чтобы протестировать код в IDE, вам достаточно в переменную lst_in вместо list(map(str.strip, sys.stdin.readlines())), 
вставить какой-нибудь список.
2. Экземпляр класса StreamData у нас также уже создан в классе StreamReaders (в функции readlines), его создавать не надо.
3. Из класса StreamReaders (функции readlines) в класс StreamData передаются 2 переменные FIELDS (в fields) и lst_in (в lst_values)
 

что нам надо сделать в классе StreamData:
1. Создать локальные свойства из переменных которые имеют пару. Где название свойства берется из списка FIELDS, 
а значение из списка lst_in (lst_values). Отправлять в Return их не надо. Если не создадите локальные свойства задача 
не засчитается.

2. Сделать проверку и вывести True если оба списка равны по длине или False в обратном случае.
 

подсказка:
Для начала я создал словарь в стримдата
после чего из словаря записал переменные в локальные свойства через цикл и сетаттр
далее в ретурне сделал проверку, результат которой возвращает тру или фолс
вот и вся задача.
"""