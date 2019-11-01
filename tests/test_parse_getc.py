from unittest import TestCase

from getcparser.getc_parser import GetCLexer, parse_getc


class TestParse_getc(TestCase):
    def test_parse_getc(self):
        text = "TODO: write a text expression for content url."
        for token in GetCLexer().tokenize(text):
            print(token)
        res = parse_getc(text)
        # TODO: write asserts
