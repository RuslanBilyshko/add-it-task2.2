import turtle


class Figure(object):

    type = "figure"

    def __init__(self, name):
        self.__name = name

    # Доступ к свойству name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    # Рисуем фигуру
    def draw(self, silly: turtle.Turtle): pass

    # Дополнение до строкового представления фигуры
    # В осоновном - это индивидуальные параметры фмгуры
    # Думаю что тут надо было воспользоваться декоратором
    # Но чувствую надо еще с ним разобраться :(
    def toString(self) -> str: return ""

    def __str__(self):
        default = "Figure - type: {}; name: {}; ".format(self.type, self.name)
        default += self.toString()
        return default


