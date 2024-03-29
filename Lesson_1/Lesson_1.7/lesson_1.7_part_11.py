"""
1.7 Методы класса (classmethod) и статические методы (staticmethod)

Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/38QoBSpQqnM

Подвиг 11 (на повторение). Объявите класс для мессенджера с именем Viber. В этом классе должны быть следующие методы:

add_message(msg) - добавление нового сообщения в список сообщений;
remove_message(msg) - удаление сообщения из списка;
set_like(msg) - поставить/убрать лайк для сообщения msg (т.е. изменить атрибут fl_like объекта msg: если лайка нет
то он ставится, если уже есть, то убирается);

show_last_message(число) - отображение последних сообщений;
total_messages() - возвращает общее число сообщений.

Эти методы предполагается использовать следующим образом (эти строчки в программе не писать):

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)

Класс Message (необходимо также объявить) позволяет создавать объекты-сообщения со следующим набором локальных свойств:

text - текст сообщения (строка);
fl_like - поставлен или не поставлен лайк у сообщения (булево значение True - если лайк есть и False -
в противном случае, изначально False);

P.S. Как хранить список сообщений, решите самостоятельно.
"""
class Viber:
    global messge_list
    messge_list = list()

    def __init__(self):
        pass

    @staticmethod
    def add_message(msg): # добавление нового сообщения в список сообщений;
       messge_list.append(msg)

    @staticmethod
    def remove_message(msg): # удаление сообщения из списка;
        messge_list.remove(msg)

    @staticmethod
    def set_like(msg): #поставить / убрать лайк для сообщения    msg(т.е.изменить
        if msg.fl_like == False:
            msg.fl_like = True
            return msg.fl_like
        else:
            msg.fl_like = False
            return msg.fl_like

    @staticmethod
    def show_last_message(num): # отображение последних сообщений;
        print(messge_list[num:-1])

    @staticmethod
    def total_messages(): # общее число сообщений.
        return (len(messge_list))


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text # текст сообщения (строка);
        self.fl_like = fl_like # поставлен или не поставлен лайк у сообщения (булево значение True - если лайк есть и
        # False - в противном случае, изначально False);


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.total_messages()
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Это курс по Python ООП."))

Viber.total_messages()
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.total_messages()
Viber.set_like(msg)
Viber.remove_message(msg)
Viber.total_messages()

Viber.show_last_message(4)
Viber.total_messages()
