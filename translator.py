"""
Translator module to translate instructions from decimal and symbolic representations
into binary machine code
"""

from constants import BIN_START, COMP_TABLE, DEST_TABLE, JUMP_TABLE, NO_DEST, NO_JUMP
from hasm_parser import CInstruction
from symbol_handler import SymbolHandler


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


def c_inst_to_bin(c_inst: CInstruction) -> str:
    """
    Translate full C-Instruction into its binary representation

    Args:
        `c_inst` (`CInstruction`): The `CInstruction` to be translated.
            E.g.: "D=M+1"

    Returns:
        str: The binary representation of the C-Instruction output as a string.
    """
    return "".join(
        [
            BIN_START,
            comp_to_bin(c_inst.comp),
            dest_to_bin(c_inst.dest),
            jump_to_bin(c_inst.jump),
        ]
    )


def a_inst_to_bin(a_inst: int) -> str:
    """
    Translate full A-Instruction into its 16-bit representation

    Args:
        `a_inst` (int): The A-Instruction to be translated.

    Returns:
        str: The 16-bit representation of the A-Instruction output as a string.
    """

    return bin(a_inst)[2:].zfill(16)


def translate_instructions(
    instructions: dict[int, str | CInstruction], symbol_handler: SymbolHandler
) -> list[str]:
    """
    Translate a dictionary of Assembly instructions into a list of binary instructions

    Args:
        `instructions` (dict[int, str | CInstruction]): The dictionary of assembly instructions

    Returns:
        `list[str]`: The list of instructions in binary (as strings)
    """

    binary_instructions = []

    for _, instruction in instructions.items():
        if isinstance(instruction, CInstruction):
            binary_instructions.append(c_inst_to_bin(instruction))
        else:
            if not instruction.isdigit():
                instruction = symbol_handler.lookup_symbol(instruction)
            binary_instructions.append(a_inst_to_bin(int(instruction)))

    return binary_instructions
