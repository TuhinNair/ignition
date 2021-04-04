from typing import Optional
from . import parser


def main():
    app = parser.Parser()
    args = app.parse_args()
    output = valid_input(args.input, args.name)

    if output:
        print(output)
    else:
        parser.print_help()


def valid_input(input: str, name: Optional[str]) -> Optional[str]:
    if input == "hello":
        target = "world" if not name else name
        return f"Hello {target}!"
    return None
