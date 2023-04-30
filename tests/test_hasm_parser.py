"""
Test methods for hasm_parser module
"""

import os

from hasm_parser import parse_file, parse_instructions


def test_parse_file_basic():
    parsed_file = parse_file(f"{os.path.dirname(__file__)}/parser_test_file")
    assert parsed_file == ["@1", "D=M+1", "@2"]


def test_parse_file_whitespace():
    parsed_file = parse_file(f"{os.path.dirname(__file__)}/parser_test_file_whitespace")
    assert parsed_file == ["@1", "D=M+1", "@2"]


def test_parse_file_comments():
    parsed_file = parse_file(f"{os.path.dirname(__file__)}/parser_test_file_comments")
    assert parsed_file == ["@1", "D=M+1", "@2"]


def test_parse_instructions():
    parsed_file = parse_file(f"{os.path.dirname(__file__)}/parser_test_file")
    assert parse_instructions(parsed_file) == {
        0: "1",
        1: "D=M+1",
        2: "2"
    }

def test_parse_instructions_with_labels():
    # TODO
    assert False