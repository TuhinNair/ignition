class Ignite:
    def __init__(self, tools):
        self.tools = tools

    def register_parser(self, subparser_handler):
        tool_names = [tool.name for tool in self.tools]
        ignition = subparser_handler(
            "ignite", description="toolchain management", help="manage toolchains"
        )
        ignition.add_argument(
            "-t",
            "--toolchain",
            action="append",
            choices=tool_names,
            help="specify the toolchain to be installed. "
            + "defaults to all available tools.",
            dest="tools",
        )
        ignition.add_argument(
            "-d",
            "--dry-run",
            action="store_true",
            dest="dry_run",
            help="descibes an output state without actually making any changes",
        )
