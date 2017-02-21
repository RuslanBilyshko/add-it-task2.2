import _pickle as pickle
from Doc import Doc

"""Класс для загрузки и сохранения коллекции фигур"""


class Data(object):
    __file_name = 'data.pkl'

    @staticmethod
    def saveDoc(doc: Doc):
        """Сохранение данных"""
        output = open(Data.__file_name, 'wb')
        pickle.dump(doc, output, 2)
        output.close()

    @staticmethod
    def loadDoc() -> Doc:
        """Загрузка данных"""
        input = open(Data.__file_name, 'rb')
        doc = pickle.load(input)
        input.close()
        return doc
