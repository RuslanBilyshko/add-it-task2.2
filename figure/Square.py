from figure.Figure import Figure


class Square(Figure):

    type = 'square'
    __width = 20


    def width(self, width):
        self.__width = float(width)

    @property
    def draw(self):
        return "draw"

    def toString(self):
        return "width: {}".format(self.__width)



