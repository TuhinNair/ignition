from argparse import ArgumentParser
from typing import List
from ignition.app.app import App


class Parser:
    def __init__(self, apps: List[App]):
        self.apps = apps
        self.parser = ArgumentParser("Ignition")
        self.subparsers_handler = self.parser.add_subparsers(
            dest="command", help="commands"
        )

        for app in self.apps:
            app.register_parser(self.register_subparser)

    def parse_args(self, args=None):
        return self.parser.parse_args(args)

    def print_help(self):
        self.parser.print_help()

    def register_subparser(self, app_command, description=None, help=None):
        return self.subparsers_handler.add_parser(
            app_command, description=description, help=help
        )
