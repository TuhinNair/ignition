from ignition.toolchain.tool import Tool


class Git(Tool):
    @property
    def name(self):
        return "git"

    def register_arguments(self, parser_handler):
        parser_handler.add_argument(
            "--first-name",
            dest="first_name",
        )
        parser_handler.add_argument(
            "--last-name",
            dest="last_name",
        )
        parser_handler.add_argument(
            "--email",
            dest="email",
        )
