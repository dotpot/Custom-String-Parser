from unittest import TestCase
from CustomStringParser import ParsingHelper

__author__ = 'lus'

class TestParsingHelper(TestCase):
    def test_ExtractTagFromString(self):
        sampleTag = 'this is the tag'

        result = ParsingHelper.extractTagFromString(sampleTag, 'this is ', ' tag')
        self.assertEqual('the', result[0])