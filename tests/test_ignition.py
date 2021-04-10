from ignition import __version__
from ignition.parser import Parser
import unittest


class TestAppMeta(unittest.TestCase):
    def test_version(self):
        self.assertEqual(__version__, "0.1.0")


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()
