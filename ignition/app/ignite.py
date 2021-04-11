from ignition.toolchain.tool import Tool
from .app import App
from typing import Dict, List
from argparse import ArgumentParser


class Ignite(App):
    def __init__(self, tools: Dict[str, Tool]):
        self.tools = tools

    @property
    def name(self):
        return "ignite"

    def register_parser(self, subparser_handler):
        ignite = self.register_ignite(subparser_handler)
        self.register_toolchain_args(ignite)
        self.register_dry_run_opt(ignite)
        self.register_tool_args(ignite)

    def register_ignite(self, subparser_handler) -> ArgumentParser:
        return subparser_handler(
            self.name, description="toolchain management", help="manage toolchains"
        )

    def register_toolchain_args(self, ignite: ArgumentParser):
        tool_names = [tool.name for tool in self.tools.values()]
        ignite.add_argument(
            "-t",
            "--toolchain",
            action="append",
            choices=tool_names,
            help="specify the toolchain to be installed. "
            + "defaults to all available tools.",
            dest="tools",
        )

    def register_dry_run_opt(self, ignite: ArgumentParser):
        ignite.add_argument(
            "-d",
            "--dry-run",
            action="store_true",
            dest="dry_run",
            help="descibes an output state without actually making any changes",
        )

    def register_tool_args(self, ignite: ArgumentParser):
        for tool in self.tools.values():
            tool.register_arguments(ignite)

    def process(self, args):
        if args.tools:
            selected_tools = [
                handler for name, handler in self.tools.items() if name in args.tools
            ]
            self.process_tools(selected_tools, args)
        else:
            self.process_tools(self.tools.values(), args)

    def process_tools(self, tools: List[Tool], args):
        for tool in tools:
            tool.process(args)
