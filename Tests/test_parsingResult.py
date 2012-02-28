from unittest import TestCase
from CustomStringParser import ParsingResult

__author__ = 'Lukas Salkauskas'

class TestParsingResult(TestCase):
    def setUp(self):
        self.parsingResult = ParsingResult('testName', 'testValue', None)

    def tearDown(self):
        self.parsingResult = None

    def test_GetValue(self):
        self.assertEquals('testValue', self.parsingResult.value)

    def test_GetName(self):
        self.assertEquals('testName', self.parsingResult.name)

    def test_GetParsingNode(self):
        self.assertEquals(None, self.parsingResult.parsingNode)

    def test_AddSubResult(self):
        self.parsingResult.addSubResult(None)
        self.assertEquals(None, self.parsingResult.subResults[0])

    def test_GetSubResults(self):
        self.parsingResult.addSubResult(None)
        self.parsingResult.addSubResult(None)

        sr = self.parsingResult.subResults
        self.assertEquals(2, len(sr))

    def test_ClearSubResults(self):
        self.parsingResult.addSubResult(None)
        self.parsingResult.addSubResult(None)

        sr = self.parsingResult.subResults
        self.assertEquals(2, len(sr))

        self.parsingResult.clearSubResults()

        sr = self.parsingResult.subResults
        self.assertIsNone(sr, 'should be None')

    def test_GetSubResultsByName(self):
        pr = ParsingResult('testName', '12', None)
        pr2 = ParsingResult('testName2', '24', None)

        self.parsingResult.addSubResult(pr)
        self.parsingResult.addSubResult(pr2)

        self.assertEqual('12', self.parsingResult.getSubResultByName('testName')[0].value)
        self.assertEqual('24', self.parsingResult.getSubResultByName('testName2')[0].value)