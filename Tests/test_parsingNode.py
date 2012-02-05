from unittest import TestCase
from CustomStringParser import ParsingNode

__author__ = 'lus'

class TestParsingNode(TestCase):
    def setUp(self):
        self.parsingNode = ParsingNode('testNode', 'startTag', 'endTag')

    def tearDown(self):
        self.parsingNode = None

    def test_GetStartTag(self):
        self.assertEqual('startTag', self.parsingNode.startTag)

    def test_GetEndTag(self):
        self.assertEqual('endTag', self.parsingNode.endTag)

    def test_GetName(self):
        self.assertEqual('testNode', self.parsingNode.name)

    def test_Parse(self):
        sampleString = 'blah startTag aaa endTag startTag bbb endTag, startTag 2 blah 2 endTag'
        results = self.parsingNode.parse(sampleString)
        self.assertEqual(3, len(results))
        self.assertEqual(' aaa ', results[0].value)
        self.assertEqual(' bbb ', results[1].value)
        self.assertEqual(' 2 blah 2 ', results[2].value)

    def test_AddParser(self):
        self.parsingNode.addParser(None)
        self.assertEqual(1, len(self.parsingNode.parsers))