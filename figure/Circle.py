from figure.Figure import Figure


class Circle(Figure):
    type = 'circle'
    __radius = 50

    def radius(self, radius):
        self.__radius = float(radius)

    def toString(self) -> str:
        return "radius: {};".format(self.__radius)


