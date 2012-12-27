from unittest import TestCase
from CustomStringParser import ParsingHelper

__author__ = 'Lukas Salkauskas'

class TestParsingHelper(TestCase):
    def test_extract_tag(self):
        sampleTag = 'this is the tag'

        result = ParsingHelper.extract_tag(sampleTag, 'this is ', ' tag')
        self.assertEqual('the', result[0])
