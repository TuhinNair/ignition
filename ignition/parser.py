from argparse import ArgumentParser


class Parser:
    def __init__(self):
        self.parser = ArgumentParser("Ignition!")
        self.parser.add_argument("input", help="invoke a hello world with 'hello'")
        self.parser.add_argument("-n", "--name", dest="name")

    def parse_args(self, args=None):
        return self.parser.parse_args(args)
