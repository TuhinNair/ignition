import abc


class Tool(abc.ABC):
    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractmethod
    def register_arguments(self, parser_handler):
        pass
