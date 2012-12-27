from unittest import TestCase
from CustomStringParser import CustomStringParserCore, ParsingNode

__author__ = 'Lukas Salkauskas'

class TestCustomStringParserCore(TestCase):
    def setUp(self):
        self.parser = CustomStringParserCore('hello you coder')

    def tearDown(self):
        self.parser = None

    def test_add_parsing_node(self):
        self.parser.add_parser(None)
        self.assertEquals(1, len(self.parser.parsers))

    def test_parse(self):
        test_parsing_node = ParsingNode('testNode', 'hello', 'coder')
        self.parser.add_parser(test_parsing_node)
        self.parser.parse()

        if test_parsing_node.results is not None:
            self.assertEquals(' you ', test_parsing_node.results[0].value)
        else:
            self.fail()
