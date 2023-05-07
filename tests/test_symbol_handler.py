"""
Test methods for hasm_parser module
"""

from symbol_handler import SymbolHandler

test_handler = SymbolHandler()

def test_handler_is_label() -> None:
    assert test_handler._is_label("(Label)") == True


def test_handler_is_label_false() -> None:
    assert test_handler._is_label("@var") == False


def test_handle_symbol_var() -> None:
    # TODO
    assert False


def test_handle_symbol_label() -> None:
    # TODO
    assert False
