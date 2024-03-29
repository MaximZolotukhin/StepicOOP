"""
1.7 Методы класса (classmethod) и статические методы (staticmethod)

Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/YkDq9p8n17A

Подвиг 9. Объявите в программе класс Video с двумя методами:

create(self, name) - для задания имени name текущего видео (метод сохраняет имя name в локальном атрибуте name объекта класса Video);
play(self) - для воспроизведения видео (метод выводит на экран строку "воспроизведение видео <name>").

Объявите еще один класс с именем YouTube, в котором объявите два метода (с декоратором @classmethod):

add_video(cls, video) - для добавления нового видео (метод помещает объект video класса Video в список);
play(cls, video_indx) - для проигрывания видео из списка по указанному индексу (индексация с нуля).

(здесь cls - ссылка на класс YouTube). И список (тоже внутри класса YouTube):

videos - для хранения добавленных объектов класса Video (изначально список пуст).

Метод play() класса YouTube должен обращаться к объекту класса Video по индексу списка videos и, затем, вызывать метод
play() класса Video.

Методы add_video и play вызывайте напрямую из класса YouTube. Создавать экземпляр этого класса не нужно.

Создайте два объекта v1 и v2 класса Video, затем, через метод create() передайте им имена "Python" и "Python ООП".
После этого с помощью метода add_video класса YouTube, добавьте в него эти два видео и воспроизведите
(с помощью метода play класса YouTube) сначала первое, а затем, второе видео.

Sample Input:
Sample Output:
воспроизведение видео Python
воспроизведение видео Python ООП
"""
class Video:
    def __int__(self):
        pass

    def create(self, name): # для задания имени name текущего видео (метод сохраняет имя name в локальном атрибуте name объекта класса Video)
        self.name = name
        return self.name

    def play(self, name):
        print(f"воспроизведение видео {name}") # для воспроизведения видео (метод выводит на экран строку "воспроизведение видео <name>")


class YouTube:
    video_list = []

    @classmethod
    def add_video(cls, video, *args): # для добавления нового видео (метод помещает объект video класса Video в список)
        cls.video_list.append(video)
        return cls.video_list

    @classmethod
    def play(cls, video_indx): # для проигрывания видео из списка по указанному индексу (индексация с нуля).
        play_video = Video()
        return play_video.play(cls.video_list[video_indx])

v1 = Video()
v2 = Video()
YouTube().add_video(v1.create('Python'))
YouTube().add_video(v2.create('Python ООП'))
YouTube().play(0)
YouTube().play(1)
