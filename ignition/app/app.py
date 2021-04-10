import abc


class App(abc.ABC):
    @abc.abstractmethod
    def register_parser(self, subparser_handler):
        pass
