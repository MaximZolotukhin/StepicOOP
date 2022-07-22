"""
1.5 Инициализатор __init__ и финализатор __del__

Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/HbtVara1GPI

Подвиг 8. Объявите в программе класс Cart (корзина), объекты которого создаются командой:

cart = Cart()

Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки (объекты классов Table, TV, Notebook и Cup). Изначально этот список должен быть пустым.

В классе Cart объявить методы:

add(self, gd) - добавление в корзину товара, представленного объектом gd;
remove(self, indx) - удаление из корзины товара по индексу indx;
get_list(self) - получение из корзины товаров в виде списка из строк:

['<наименовние_1>: <цена_1>',
'<наименовние_2>: <цена_2>',
...
'<наименовние_N>: <цена_N>']

Объявите в программе следующие классы для описания товаров:

Table - столы;
TV - телевизоры;
Notebook - ноутбуки;
Cup - кружки.

Объекты этих классов должны создаваться командой:

gd = ИмяКласса(name, price)

Каждый объект классов товаров должен содержать локальные свойства:

name - наименование;
price - цена.

Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV), один стол (Table), два ноутбука (Notebook) и одну кружку (Cup). Названия и цены придумайте сами.

P.S. Отображать на экране ничего не нужно, только создать объекты по указанным требованиям.
"""
class Cart:
    def __init__(self):
        self.goods = []

    # добавление в корзину товара, представленного объектом gd
    def add(self, *gd):
        for val in gd:
            self.goods.append(val)
        return self.goods

    # удаление из корзины товара по индексу indx
    def remove(self, indx):
        del self.goods[indx]
        return self.goods


    # получение из корзины товаров в виде списка из строк
    def get_list(self):
        return [f"{i.name}: {i.price}" for i in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = Cart() # создаю корзину
gd1 = TV('Sony', 50000)
gd2 = TV('Samsung', 65999)
gd3 = Table('Пенёк лесной', 150000)
gd4 = Notebook('Asus', 76000)
gd5 = Notebook('Lenovo', 56000)
gd6 = Cup('Graal', 25000)
cart.add(gd1, gd2, gd3, gd4, gd5, gd6)# заполняю корзину товаром
print(cart.get_list())
