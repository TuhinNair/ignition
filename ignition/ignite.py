from argparse import ArgumentParser
from typing import Optional


def main():
    parser = ArgumentParser("Ignition!")
    parser.add_argument("input", help="invoke a hello world with 'hello'")
    parser.add_argument("-n", "--name", dest="name")

    args = parser.parse_args()

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
