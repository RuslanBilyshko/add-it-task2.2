import argparse

from figure import Figure
from figure.Circle import Circle
from figure.Square import Square


class FCreator(object):
    __types = ['square', 'circle']

    def createParser(self, line: str):
        parser = argparse.ArgumentParser()
        parser.add_argument('-t', '--type', required=True, choices=self.__types)
        parser.add_argument('-n', '--name', required=True)
        parser.add_argument('-w', '--width', default=20, type=float)
        parser.add_argument('-r', '--radius', default=20, type=float)

        return parser.parse_args(line.split())

    def editParser(self, line: str):
        parser = argparse.ArgumentParser()
        parser.add_argument('-n', '--name', required=True)
        parser.add_argument('-w', '--width', type=float)
        parser.add_argument('-r', '--radius', type=float)

        return parser.parse_args(line.split())



    def create(self, line: str) -> Figure:

        params = self.createParser(line)

        if params.type == 'square':
            return self.createSquare(params.name, params.width)

        if params.type == 'circle':
            return self.createCircle(params.name, params.radius)


    def edit(self, params, figure: Figure):

        if figure.type == 'square':
            return self.createSquare(params.name, params.width)

        if figure.type == 'circle':
            return self.createCircle(params.name, params.radius)

    def createSquare(self, name: str, width: float):
        square = Square(name)
        square.width(width)
        return square

    def createCircle(self, name: str, radius: float):
        circle = Circle(name)
        circle.radius(radius)
        return circle

    def getTypes(self) -> str:
        return "".join("{}\n".format(t) for t in self.__types)


fcreator = FCreator()
