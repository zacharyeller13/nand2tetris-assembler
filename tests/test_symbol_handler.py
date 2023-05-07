"""
Test methods for hasm_parser module
"""

from constants import PRE_DEFINED_SYMBOLS
from symbol_handler import SymbolHandler

test_handler = SymbolHandler()
expected_handler = SymbolHandler()

def test_handler_base() -> None:
    assert test_handler.symbol_table == PRE_DEFINED_SYMBOLS
    assert test_handler._next_address == 16


def test_handler_is_label() -> None:
    assert test_handler._is_label("(Label)") is True


def test_handler_is_label_false() -> None:
    assert test_handler._is_label("@var") is False


def test_handle_symbol_var() -> None:
    test_handler.handle_symbol("@var", 1)
    expected_handler.symbol_table["var"] = 16
    assert test_handler.symbol_table == expected_handler.symbol_table


def test_handle_symbol_label() -> None:
    test_handler.handle_symbol("(Label)", 2)
    expected_handler.symbol_table["Label"] = 2
    assert test_handler.symbol_table == expected_handler.symbol_table
