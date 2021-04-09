from typing import Optional
from .parser import Parser


def main():
    app = Parser()
    args = app.parse_args()
    output = process_input(args.input, args.name)

    if output:
        print(output)
    else:
        app.print_help()


def process_input(input: str, name: Optional[str]) -> Optional[str]:
    if input == "hello":
        target = "world" if not name else name
        return f"Hello {target}!"
    return None
