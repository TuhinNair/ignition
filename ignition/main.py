from ignition.toolchain.git import Git
from ignition.toolchain.tool import Tool
from .parser import Parser
from ignition.app.ignite import Ignite
from typing import List
from ignition.app.app import App
import sys


def main():
    apps = load_apps()
    parser = Parser(apps)
    args = parser.parse_args(sys.argv[1:])
    print(args)


def load_apps() -> List[App]:
    tools = load_tools()
    ignite = Ignite(tools)
    return [ignite]


def load_tools() -> List[Tool]:
    git = Git()
    return [git]