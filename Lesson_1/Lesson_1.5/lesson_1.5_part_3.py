"""
1.5 Инициализатор __init__ и финализатор __del__

Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/DEyOq7Gpko4

Подвиг 3. Объявите класс Point так, чтобы объекты этого класса можно было создавать командами:

p1 = Point(10, 20)
p2 = Point(12, 5, 'red')

Здесь первые два значения - это координаты точки на плоскости (локальные свойства x, y),
а третий необязательный аргумент - цвет точки (локальное свойство color).
Если цвет не указывается, то он по умолчанию принимает значение black.

Создайте тысячу таких объектов с координатами (1, 1), (3, 3), (5, 5), ... то есть,
с увеличением на два для каждой новой точки. Каждый объект следует поместить в список points (по порядку).
Для второго объекта в списке points укажите цвет 'yellow'.

P.S. На экран в программе ничего выводить не нужно.
"""
import pprint
class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = []
for i in range(1, 2000, 2):
    if i == 3:
        points.append(Point(i, i, color='yellow'))
    else:
        points.append(Point(i, i))


print(points[1].x)
print(points[1].y)
print(points[1].color)
