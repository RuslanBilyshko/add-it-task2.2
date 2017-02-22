import os
import _pickle as pickle
from Doc import Doc

"""Класс для загрузки и сохранения коллекции фигур"""


class Data(object):
    __file_name = 'data.pyc'

    @staticmethod
    def saveDoc(doc: Doc):
        """Сохранение данных"""

        result = []
        for key, figure in doc.all().items():
            result.append(figure)

        output = open(Data.__file_name, 'wb')
        pickle.dump(result, output)
        output.close()

    @staticmethod
    def loadDoc() -> list:
        """Загрузка данных"""

        if os.path.exists(Data.__file_name):
            load = open(Data.__file_name, 'rb')
            figure_list = pickle.load(load)
            load.close()
        else:
            figure_list = []


        return figure_list
