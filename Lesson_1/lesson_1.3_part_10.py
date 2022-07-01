"""
1.3 Классы и объекты. Атрибуты классов и объектов

Подвиг 10. Объявите класс с именем Person и атрибутами:

name: 'Сергей Балакирев'
job: 'Программист'
city: 'Москва'

Создайте экземпляр p1 этого класса и проверьте, существует ли у него локальное свойство с именем job.
Выведите True, если оно присутствует в объекте p1 и False - если отсутствует.
"""
class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'

p1 = Person()
p1.work = 'Кодер'
print('job' in p1.__dict__) # 'job' in p1.__dict__ ищет значение непосредственно в экземпляре класс
print(hasattr(p1, 'work')) # hasattr(класс, 'атрибут в формате str') Проверяет наличие элемента в классе
