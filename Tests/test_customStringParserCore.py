from unittest import TestCase
from CustomStringParser import CustomStringParserCore, ParsingNode

__author__ = 'Lukas Salkauskas'

class TestCustomStringParserCore(TestCase):
    def setUp(self):
        self.parser = CustomStringParserCore('hello you coder')

    def tearDown(self):
        self.parser = None

    def test_AddParsingNode(self):
        self.parser.addParsingNode(None)
        self.assertEquals(1, len(self.parser.parsers))

    def test_Parse(self):
        testParsingNode = ParsingNode('testNode', 'hello', 'coder')
        self.parser.addParsingNode(testParsingNode)
        self.parser.parse()

        if testParsingNode.results is not None:
            self.assertEquals(' you ', testParsingNode.results[0].value)
        else:
            self.fail()