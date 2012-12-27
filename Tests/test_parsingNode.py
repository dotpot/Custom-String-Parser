from unittest import TestCase
from CustomStringParser import ParsingNode

__author__ = 'Lukas Salkauskas'

class TestParsingNode(TestCase):
    def setUp(self):
        self.parsingNode = ParsingNode('testNode', 'start_tag', 'end_tag')

    def tearDown(self):
        self.parsingNode = None

    def test_start_tag(self):
        self.assertEqual('start_tag', self.parsingNode.start_tag)

    def test_end_tag(self):
        self.assertEqual('end_tag', self.parsingNode.end_tag)

    def test_name(self):
        self.assertEqual('testNode', self.parsingNode.name)

    def test_parse(self):
        sample_value = 'blah start_tag aaa end_tag start_tag bbb end_tag, start_tag 2 blah 2 end_tag'
        results = self.parsingNode.parse(sample_value)
        self.assertEqual(3, len(results))
        self.assertEqual(' aaa ', results[0].value)
        self.assertEqual(' bbb ', results[1].value)
        self.assertEqual(' 2 blah 2 ', results[2].value)

    def test_add_parser(self):
        self.parsingNode.add_parser(None)
        self.assertEqual(1, len(self.parsingNode.parsers))
