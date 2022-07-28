"""
1.6 Магический метод __new__. Пример паттерна Singleton


Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/sX_uP7GVqkc

Подвиг 8. В программе объявлена переменная TYPE_OS и два следующих класса:

TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"

class DialogLinux:
    name_class = "DialogLinux"

Необходимо объявить третий класс с именем Dialog, который бы создавал объекты командой:
dlg = Dialog(<название>)
Здесь <название> - это строка, которая сохраняется в локальном свойстве name объекта dlg.
Класс Dialog должен создавать объекты класса DialogWindows, если переменная TYPE_OS = 1 и объекты класса DialogLinux,
 если переменная TYPE_OS не равна 1. При этом, переменная TYPE_OS может меняться в последующих строчках программы.
 Имейте это в виду, при объявлении класса Dialog.

P.S. В программе на экран ничего выводить не нужно. Только объявить класс Dialog.
"""

TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"

class DialogLinux:
    name_class = "DialogLinux"

class Dialog:

    def __new__(cls, *args, **kwargs):
        # TYPE_OS = args
        if TYPE_OS == 1:
            res = super().__new__(DialogWindows)
            setattr(res, 'name', args[0]) #Создается локальная перменная
            return res
        elif TYPE_OS == 2:
            res = super().__new__(DialogLinux)
            setattr(res, 'name', args[0])
            return res

    def __init__(self, name):
        self.name = name


dlg = Dialog(1)
print(dlg.name_class)
dlg_1 = Dialog(2)
print(dlg_1.name_class)
