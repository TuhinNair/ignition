from argparse import ArgumentParser
from typing import Dict
from ignition.app.app import App


class Parser:
    def __init__(self, apps: Dict[str, App]):
        self.apps = apps
        self.parser = ArgumentParser("Ignition")
        self.subparsers_handler = self.parser.add_subparsers(
            dest="command", help="commands", required=True
        )

        for app in self.apps.values():
            app.register_parser(self.register_subparser)

    def parse_args(self, args=None):
        return self.parser.parse_args(args)

    def print_help(self):
        self.parser.print_help()

    def register_subparser(self, app_command, description=None, help=None):
        return self.subparsers_handler.add_parser(
            app_command, description=description, help=help
        )

    def process(self, args):
        cmd = args.command
        app_processor = self.apps[cmd]

        if app_processor is None:
            self.parser.print_help()
        else:
            app_processor.process(args)
