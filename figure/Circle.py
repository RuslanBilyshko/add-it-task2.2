from figure.Figure import Figure
import turtle

class Circle(Figure):
    type = 'circle'
    __radius = 50

    def radius(self, radius):
        self.__radius = float(radius)

    def draw(self, silly: turtle.Turtle):
        silly.reset()
        silly.circle(self.__radius)

    def toString(self) -> str:
        return "radius: {};".format(self.__radius)


