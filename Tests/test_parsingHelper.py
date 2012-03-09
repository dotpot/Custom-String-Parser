from unittest import TestCase
from CustomStringParser import ParsingHelper

__author__ = 'Lukas Salkauskas'

class TestParsingHelper(TestCase):
    def test_ExtractTagFromString(self):
        sampleTag = 'this is the tag'

        result = ParsingHelper.extractTagFromString(sampleTag, 'this is ', ' tag')
        self.assertEqual('the', result[0])

    def test_StripTags(self):
        sampleText = "<a> 1 <asff> 2 <sfdf/> b"

        result = ParsingHelper.StripTags(sampleText).strip()

        self.assertEqual('1  2  b', result)

#    def test_extractTagFromStringTillEndCount(self):
#        sampleText = '1 2 2 2 2'
#        result = ParsingHelper.extractTagFromStringTillEndCount(sampleText, '1', '2', 3)

#        self.assertEqual('2 2 2', result)
