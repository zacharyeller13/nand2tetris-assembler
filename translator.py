"""
Translator module to translate instructions from decimal and symbolic representations
into binary machine code
"""

from constants import BIN_START, COMP_TABLE, DEST_TABLE, JUMP_TABLE, NO_DEST, NO_JUMP


def comp_to_bin(comp: str) -> str:
    """
    Translate comp part of instruction to binary

    Args:
        `comp` (str): String representation of the comp part of a CInstruction

    Returns:
        str: The binary representation of the comp part output as a string
    """

    return COMP_TABLE[comp]


def dest_to_bin(dest: str | None) -> str:
    """
    Translate dest part of instruction to binary

    Args:
        `dest` (str | None): String representation of the dest part of a CInstruction
            or None if no dest part

    Returns:
        str: The binary representation of the dest part output as a string.
            if `dest=None` then output "000"
    """

    if not dest:
        return NO_DEST

    return DEST_TABLE[dest]


def jump_to_bin(jump: str | None) -> str:
    """
    Translate jump part of instruction to binary

    Args:
        `jump` (str | None): String representation of the jump part of a CInstruction
            or None if no jump part

    Returns:
        str: The binary representation of the jump part output as a string
            if `jump=None` then output "000"
    """

    if not jump:
        return NO_JUMP

    return JUMP_TABLE[jump]
