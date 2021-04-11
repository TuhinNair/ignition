from ignition.toolchain.git import Git
from ignition.toolchain.tool import Tool
from .parser import Parser
from ignition.app.ignite import Ignite
from typing import Dict
from ignition.app.app import App
import sys


def main():
    apps = load_apps()
    parser = Parser(apps)
    args = parser.parse_args(sys.argv[1:])
    parser.process(args)


def load_apps() -> Dict[str, App]:
    tools = load_tools()
    ignite = Ignite(tools)
    return {
        ignite.name: ignite,
    }


def load_tools() -> Dict[str, Tool]:
    git = Git()
    return {
        git.name: git,
    }
