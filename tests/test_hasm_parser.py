"""
Test methods for hasm_parser module
"""

import os

from hasm_parser import Parser


def test_parser_basic():
    parser = Parser(f"{os.path.dirname(__file__)}/parser_test_file")
    assert parser.instructions == ["@1", "D=M+1", "@2"]


def test_parser_whitespace():
    parser = Parser(f"{os.path.dirname(__file__)}/parser_test_file_whitespace")
    assert parser.instructions == ["@1", "D=M+1", "@2"]


def test_parser_comments():
    parser = Parser(f"{os.path.dirname(__file__)}/parser_test_file_comments")
    assert parser.instructions == ["@1", "D=M+1", "@2"]


def test_parse_instructions():
    parser = Parser(f"{os.path.dirname(__file__)}/parser_test_file")
    assert parser.parse_instructions() == {
        0: "1",
        1: "D=M+1",
        2: "2"
    }
