from figure.Figure import Figure
import turtle

class Square(Figure):

    type = 'square'
    __width = 20


    def width(self, width):
        self.__width = float(width)

    def draw(self, silly: turtle.Turtle):
        silly.reset()
        silly.forward(self.__width)
        silly.left(90)
        silly.forward(self.__width)
        silly.left(90)
        silly.forward(self.__width)
        silly.left(90)
        silly.forward(self.__width)
        silly.left(90)

    def toString(self):
        return "width: {}".format(self.__width)



