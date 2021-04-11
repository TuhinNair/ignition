import abc
from argparse import ArgumentParser


class Tool(abc.ABC):
    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractmethod
    def register_arguments(self, parser_handler: ArgumentParser):
        pass

    @abc.abstractmethod
    def process(self, args):
        pass
