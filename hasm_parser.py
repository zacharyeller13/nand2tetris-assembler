"""
Parser module to parse .asm file into a dictionary of lines
and their corresponding instructions
"""

from constants import COMMENT, VAR_START, LABEL_START
from symbol_handler import SymbolHandler


class CInstruction:
    """
    Class to parse a C-Instruction into its component parts for easier processing later

    Attributes:
        `instruction`: the full string representation of the instruction
        `comp`: string comp part of the instruction
        `dest`: string destination part of the instruction.  None if there is no destination
        `jump`: string jump part of the instruction. None if no jump being made
    """

    def __init__(self, instruction: str) -> None:
        self.instruction = instruction
        self.comp = self.parse_comp(instruction)
        self.dest = self.parse_dest(instruction)
        self.jump = self.parse_jump(instruction)

    def parse_comp(self, instruction: str) -> str:
        """
        Parse out the comp part of a C-Instruction

        Args:
            `instruction` (str): The C-Instruction

        Returns:
            the comp part of a C-Instruction
        """

        if (end_index := instruction.find(";")) == -1:
            end_index = len(instruction)

        if (start_index := instruction.find("=") + 1) != 0:
            return instruction[start_index:end_index]

        return instruction[:end_index]

    def parse_dest(self, instruction: str) -> str | None:
        """
        Parse out the dest part of a C-Instruction

        Args:
            `instruction` (str): The C-Instruction

        Returns:
            str | None: the dest part of a C-Instruction or None if there is no dest part
        """

        if (end_index := instruction.find("=")) != -1:
            return instruction[:end_index]

    def parse_jump(self, instruction: str) -> str | None:
        """
        Parse out the jump part of a C-Instruction

        Args:
            `instruction` (str): The C-Instruction

        Returns:
            str | None: the jump part of a C-Instruction or None if there is no jump part
        """

        if (index := instruction.find(";")) != -1:
            return instruction[index + 1 :]

    def __str__(self) -> str:
        return f"{self.dest=}, {self.comp=}, {self.jump=}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, CInstruction):
            raise NotImplementedError

        return (
            self.comp == other.comp
            and self.dest == other.dest
            and self.jump == other.jump
        )


def parse_file(file: str) -> list[str]:
    """
    Read in a file and parse it into
    a list of instructions without whitespace or comments

    Args:
        `file` (str): The filepath to the file to be parsed

    Returns:
        list[str]: The file parsed into a list of strings without
            whitespace or comments

    """

    with open(file, "r", encoding="UTF-8") as f:
        lines = f.read().split("\n")
        lines = [
            line.split(COMMENT)[0].strip()
            for line in lines
            if line != "" and line[:2] != COMMENT
        ]

        return lines


def parse_instructions(
    instructions: list[str], symbol_handler: SymbolHandler
) -> dict[int, str | CInstruction]:
    """
    Parse `instructions` into a dictionary with keys representing line-numbers
        and values representing the instruction (without any leading instruction chars like '@')

    Args:
        `instructions` (list[str]): the list of instructions
        `symbol_handler` (`SymbolHandler`): A symbol handler for adding any @vars and
            (Labels) to the symbol table.

    Returns:
        dict[int, str | CInstruction]: `instructions` parsed into a dictionary of line-numbers and
            their corresponding instruction values as strings or CInstruction objects
    """

    parsed_instructions = {}
    # Separate from the actual iteration of the instructions list so we can skip an increment if
    # symbol is a (Label)
    line_num = 0

    # Handle all labels first so as not to accidentally add them as vars
    # if a reference appears before the label is declared
    symbol_handler.handle_labels(instructions)

    for instruction in instructions:
        if instruction[0] not in (VAR_START, LABEL_START):
            parsed_instructions[line_num] = CInstruction(instruction)
            line_num += 1
        elif instruction.startswith(VAR_START) and instruction[1:].isdigit():
            parsed_instructions[line_num] = instruction.removeprefix(VAR_START)
            line_num += 1
        else:
            # We pass the @var or (Label) into the symbol handler to be
            # added to the symbol table where necessary as well as to be cleaned
            # and return back to the dictionary of instructions.
            # If it's a label declaration, we return None and skip that line
            if (
                parsed_instruction := symbol_handler.handle_symbol(
                    instruction, line_num
                )
            ) is not None:
                parsed_instructions[line_num] = parsed_instruction
                line_num += 1

    return parsed_instructions
