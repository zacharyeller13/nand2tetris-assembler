"""
Test methods for translator module
"""

from translator import comp_to_bin, dest_to_bin, jump_to_bin

def test_comp_to_bin_0() -> None:
    assert comp_to_bin(comp="0") == "0101010"


def test_comp_to_bin_D() -> None:
    assert comp_to_bin(comp="D") == "0001100"


def test_comp_to_bin_D_plus_M() -> None:
    assert comp_to_bin(comp="D+M") == "1000010"


def test_comp_to_bin_D_or_A() -> None:
    assert comp_to_bin(comp="D|A") == "0010101"


def test_dest_to_bin_None() -> None:
    assert dest_to_bin(dest=None) == "000"


def test_dest_to_bin_M() -> None:
    assert dest_to_bin(dest="M") == "001"


def test_dest_to_bin_AM() -> None:
    assert dest_to_bin(dest="AM") == "101"


def test_jump_to_bin_None() -> None:
    assert jump_to_bin(jump=None) == "000"


def test_jump_to_bin_JGT() -> None:
    assert jump_to_bin(jump="JGT") == "001"


def test_jump_to_bin_JLE() -> None:
    assert jump_to_bin(jump="JLE") == "110"
