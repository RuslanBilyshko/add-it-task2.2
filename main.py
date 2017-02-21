import cmd
from Data import Data
from figure.FCreator import fcreator

# состояние изменений в коллекцию фигур

doc = Data.loadDoc()


class Cli(cmd.Cmd):


    _isChange = False


    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "> "
        self.intro = "Добро пожаловать\nДля справки наберите 'help'"
        self.doc_header = "Доступные команды (для справки по конкретной команде наберите 'help _команда_')"

    def do_print(self, figure: str):
        """Распечатка фигуры\nДля вывода на экран введите "print <figure_name>"
        """
        if doc.has(figure):
            print(doc.get(figure))
        else:
            print(doc.errorNotFoundFigure(
                figure) + "\nВы можете посмотреть список доступных фигур выполнив команду <list>")



    def do_create(self, line: str):
        """Создание фигуры.
        Введите "create [--type тип_фигуры] параметры через пробел в виде [--параметр значение]"
        Например: create --type square --name f3 -radius 50
        Для просмотра доступных типов и их параметров введите get_types"""

        # create -t square -n f3 -r 50
        f = fcreator.create(line)

        if doc.has(f.name):
            print(doc.errorIsHasFigure(f.name))
        else:
            doc.add(f)
            self._isChange = True
            print(doc.successCreateFigure(f.name))

    def do_edit(self, line: str):
        """Редактировать фигуру. Введите "edit [--name имя_фигуры] [--параметр значение]"""

        params = fcreator.editParser(line)

        if doc.has(params.name):
            figure = doc.get(params.name)
            figure = fcreator.edit(params, figure)
            doc.update(figure)
            print(doc.successUpdateFigure(figure.name))
        else:
            print(doc.errorNotFoundFigure(params.name))

    def do_list(self, line: str):
        """Список всех созданных фигур"""
        print(doc)

    def do_get_types(self, line: str):
        """Список доступных типов для создания фигур"""
        print(fcreator.getTypes())

    def do_exit(self, line):
        """Выход из программы"""
        if self._isChange:
            inpt = input('Сохранить изменения? Y/N: ')
            if inpt == 'y' or inpt == "н":
                Data.saveDoc(doc)



        return True

    def default(self, line):
        print("Несуществующая команда")


if __name__ == "__main__":
    cli = Cli()
    try:
        cli.cmdloop()

    except KeyboardInterrupt:
        print("завершение сеанса...")
