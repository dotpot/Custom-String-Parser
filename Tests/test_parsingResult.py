from unittest import TestCase
from CustomStringParser import ParsingResult

__author__ = 'Lukas Salkauskas'

class TestParsingResult(TestCase):
    def setUp(self):
        self.parsingResult = ParsingResult('testName', 'testValue', None)

    def tearDown(self):
        self.parsingResult = None

    def test_value(self):
        self.assertEquals('testValue', self.parsingResult.value)

    def test_name(self):
        self.assertEquals('testName', self.parsingResult.name)

    def test_parsing_node(self):
        self.assertEquals(None, self.parsingResult.parsing_node)

    def test_add_sub_result(self):
        self.parsingResult.add_sub_result(None)
        self.assertEquals(None, self.parsingResult.sub_results[0])

    def test_sub_results(self):
        self.parsingResult.add_sub_result(None)
        self.parsingResult.add_sub_result(None)

        sr = self.parsingResult.sub_results
        self.assertEquals(2, len(sr))

    def test_clear_sub_results(self):
        self.parsingResult.add_sub_result(None)
        self.parsingResult.add_sub_result(None)

        sr = self.parsingResult.sub_results
        self.assertEquals(2, len(sr))

        self.parsingResult.clear_sub_results()

        sr = self.parsingResult.sub_results
        self.assertIsNone(sr, 'should be None')
