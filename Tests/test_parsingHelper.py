from unittest import TestCase
from custom_string_parser import ParsingHelper

__author__ = 'Lukas Salkauskas'

class TestParsingHelper(TestCase):
    def test_extract_tag(self):
        sampleTag = 'this is the tag'

        result = ParsingHelper.extract_tag(sampleTag, 'this is ', ' tag')
        self.assertEqual('the', result[0])
