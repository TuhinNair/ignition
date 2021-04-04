from ignition import __version__
from ignition.parser import Parser
import unittest


class TestAppMeta(unittest.TestCase):
    def test_version(self):
        self.assertEqual(__version__, "0.1.0")


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_hello_arg(self):
        args = self.parser.parse_args(["hello"])
        self.assertEqual(args.input, "hello")

    def test_name_option(self):
        args = self.parser.parse_args(["hello", "-n", "tuhin"])
        self.assertEqual(args.name, "tuhin")
