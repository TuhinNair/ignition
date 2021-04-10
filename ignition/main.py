from typing import Optional
from .parser import Parser
from .ignite import Ignite
import sys


class Git:
    name = "git"


def main():
    git = Git()
    ignite_app = Ignite([git])
    app = Parser([ignite_app])
    args = app.parse_args(sys.argv[1:])
    print(args)
