"""
Test methods for hasm_parser module
"""

import os

from hasm_parser import parse_file, parse_instructions, CInstruction

expected_c_instruction = CInstruction("D=M+1")
expected_c_instruction.comp = "M+1"
expected_c_instruction.dest = "D"
expected_c_instruction.jump = None

expected_jmp_instruction = CInstruction("0;JMP")
expected_jmp_instruction.jump = "JMP"

expected_full_c_instruction = CInstruction("MD=A-1;JGE")
expected_full_c_instruction.dest = "MD"
expected_full_c_instruction.comp = "A-1"
expected_full_c_instruction.jump = "JGE"


def test_parse_file_basic():
    parsed_file = parse_file(f"{os.path.dirname(__file__)}/parser_test_file.asm")
    assert parsed_file == ["@1", "D=M+1", "@2", "0;JMP"]


def test_parse_file_whitespace():
    parsed_file = parse_file(f"{os.path.dirname(__file__)}/parser_test_file_whitespace.asm")
    assert parsed_file == ["@1", "D=M+1", "@2", "0;JMP"]


def test_parse_file_comments():
    parsed_file = parse_file(f"{os.path.dirname(__file__)}/parser_test_file_comments.asm")
    assert parsed_file == ["@1", "D=M+1", "@2", "0;JMP"]


def test_full_c_instruction():
    assert CInstruction("MD=A-1;JGE") == expected_full_c_instruction


def test_parse_instructions():
    parsed_file = parse_file(f"{os.path.dirname(__file__)}/parser_test_file.asm")
    assert parse_instructions(parsed_file) == {
        0: "1",
        1: expected_c_instruction,
        2: "2",
        3: expected_jmp_instruction
    }


def test_parse_instructions_with_labels():
    # TODO
    assert False