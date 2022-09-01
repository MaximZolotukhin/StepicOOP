"""
2.1 Режимы доступа public, private, protected. Сеттеры и геттеры

Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/rcj0pB1aB5M

Подвиг 8. Объявите в программе два класса Point и Rectangle. Объекты первого класса должны создаваться командой:

pt = Point(x, y)

где x, y - координаты точки на плоскости (целые или вещественные числа). При этом в объектах класса Point должны формироваться следующие локальные свойства:

__x, __y - координаты точки на плоскости.

и один геттер:

get_coords() - возвращение кортежа текущих координат __x, __y

Объекты второго класса Rectangle (прямоугольник) должны создаваться командами:

r1 = Rectangle(Point(x1, y1), Point(x2, y2))

или

r2 = Rectangle(x1, y1, x2, y2)

Здесь первая координата (x1, y1) - верхний левый угол, а вторая координата (x2, y2) - правый нижний. При этом, в объектах класса Rectangle (вне зависимости от способа их создания) должны формироваться следующие локальные свойства:

__sp - объект класса Point с координатами x1, y1 (верхний левый угол);
__ep - объект класса Point с координатами x2, y2 (нижний правый угол).

Также к классе Rectangle должны быть реализованы следующие методы:

set_coords(self, sp, ep) - изменение текущих координат, где sp, ep - объекты класса Point;
get_coords(self) - возвращение кортежа из объектов класса Point с текущими координатами прямоугольника (ссылки на локальные свойства __sp и __ep);
draw(self) - отображение в консоли сообщения: "Прямоугольник с координатами: (x1, y1) (x2, y2)". Здесь x1, y1, x2, y2 - соответствующие числовые значения координат.

Создайте объект rect класса Rectangle с координатами (0, 0), (20, 34).

P.S. На экран ничего выводить не нужно.
"""

class Point:
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0][0], (int, float)) and isinstance(args[0][1], (int, float)):
                self.__x = args[0][0]
                self.__y = args[0][1]
        else:
            if isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)):
                self.__x = args[0]
                self.__y = args[1]


    def get_coords(self):
        return (self.__x, self.__y)


class Rectangle:
    def __init__(self, *args):
        if len(args) == 4:
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])
        elif isinstance(args[0], Point) or isinstance(args[0], Point):
            self.__sp = args[0]
            self.__ep = args[1]
        else:
            self.__sp = Point(args[0])
            self.__ep = Point(args[1])


    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return (self.__sp, self.__ep)

    def draw(self):
        print(f"Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}")



rect = Rectangle((0, 0), (20, 34))
pt = Point((12, 96))
print(pt.get_coords())
pt_2 = Point(12, 96)
print(pt_2.get_coords())
r1 = Rectangle(Point(12, 32), Point(142, 124))
r2 = Rectangle((3, 1), (40, 54))
r3 = Rectangle(0, 10, 100, 160)
r1.draw()
r2.draw()
r3.draw()
rect.draw()
#
r = Rectangle(1, 2.6, 3.3, 4)
r.set_coords(Point(1, 2), Point(3, 4))
sp, ep = r.get_coords()
print(sp, ep)
a, b = sp.get_coords()
print(a, b)
c, d = ep.get_coords()
print(c, d)
assert a == 1 and b == 2 and c == 3 and d == 4, "метод get_coords вернул неверные значения координат"

r = Rectangle(Point(1, 2), Point(3, 4))
sp, ep = r.get_coords()
a, b = sp.get_coords()
c, d = ep.get_coords()
assert a == 1 and b == 2 and c == 3 and d == 4, "метод get_coords вернул неверные значения координат"