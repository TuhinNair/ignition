import abc
from argparse import _SubParsersAction


class App(abc.ABC):
    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractmethod
    def register_parser(self, subparser_handler: _SubParsersAction):
        pass

    @abc.abstractmethod
    def process(self, args):
        pass
