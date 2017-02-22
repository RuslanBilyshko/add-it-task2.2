from figure.Figure import Figure
from figure.Circle import Circle
from figure.Square import Square

"""Класс, для хранения коллекции фигур"""
class Doc(object):

    __collection = {}

    def add(self, figure: Figure):
        """Добавление фигуры в коллекцию"""
        self.__collection.update({figure.name: figure})

    def update(self, figure: Figure):
        """Обовление фигуры"""
        self.add(figure)

    def get(self, key) -> dict:
        """Получение фигуры по имени"""
        return self.__collection[key]

    def remove(self, key):
        """Удаление фигуры из коллекции"""
        self.__collection.pop(key)


    def has(self, key):
        """Проверка на существование фигуры в коллекции"""
        if key in self.all():
            return True

        return False

    def all(self):
        """Возвращает коллекцию фигур"""
        return self.__collection

    # Сообщения при работе с коллекцией
    #-------------------------------------------
    def errorNotFoundFigure(self, figure: str):
        """Сообщение: если фигура не найдена"""
        return "Фигура с именем <{}> не найдена".format(figure)

    def errorIsHasFigure(self, name: str) -> str:
        """Сообщение: если фигура уже существует"""
        return "Фигура с именем \"{}\" уже существует, укажите другое имя".format(name)

    def successCreateFigure(self, name: str) -> str:
        """Сообщение: если фигура успешно создана"""
        return "Фигура с именем \"{}\" успешно создана".format(name)

    def successUpdateFigure(self, name: str) -> str:
        """Сообщение: если фигура успешно обновлена"""
        return "Фигура с именем \"{}\" успешно обновлена".format(name)

    def successRemoveFigure(self, name: str) -> str:
        """Сообщение: если фигура успешно удалена"""
        return "Фигура с именем \"{}\" успешно удалена".format(name)

    def __str__(self):

        if len(self.all()) > 0:
            result = ""
            for key, figure in self.all().items():
                result += "{}\n".format(figure)
            return result

        else:
            return"Пока не создано ниодной фигуры"


