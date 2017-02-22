from figure.Figure import Figure
from figure.Circle import Circle
from figure.Square import Square


class Doc(object):

    __collection = {}

    def add(self, figure: Figure):
        self.__collection.update({figure.name: figure})

    def update(self, figure: Figure):
        self.add(figure)

    def get(self, key) -> dict:
        return self.__collection[key]

    def remove(self, key):
        self.__collection.pop(key)


    def has(self, key):
        if key in self.all():
            return True

        return False

    def all(self):
        return self.__collection

    def errorNotFoundFigure(self, figure: str):
        return "Фигура с именем <{}> не найдена".format(figure)

    def errorIsHasFigure(self, name: str) -> str:
        return "Фигура с именем \"{}\" уже существует, укажите другое имя".format(name)

    def successCreateFigure(self, name: str) -> str:
        return "Фигура с именем \"{}\" успешно создана".format(name)

    def successUpdateFigure(self, name: str) -> str:
        return "Фигура с именем \"{}\" успешно обновлена".format(name)

    def successRemoveFigure(self, name: str) -> str:
        return "Фигура с именем \"{}\" успешно удалена".format(name)

    def __str__(self):

        if len(self.all()) > 0:
            result = ""
            for key, figure in self.all().items():
                result += "{}\n".format(figure)
            return result

        else:
            return"Пока не создано ниодной фигуры"


