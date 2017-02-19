from copyreg import constructor


class Figure(object):

    type = "figure"

    _params = []

    def __init__(self, name):
        self.__name = name
        self.constructor()

    def constructor(self): pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name



    def draw(self): pass

    def toString(self) -> str: return ""

    def __str__(self):
        default = "Figure - type: {}; name: {}; ".format(self.type, self.name)
        default += self.toString()
        return default


