"""
Parser module to parse .asm file into a dictionary of lines
and their corresponding instructions
"""

from constants import COMMENT, VAR_START


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
        if instruction[1] == '=':
            return instruction[2:]
        else:
            return instruction[:instruction.index(';')]

    def parse_dest(self, instruction: str) -> str | None:
        if instruction[1] == '=':
            return instruction[:1]
        
    def parse_jump(self, instruction: str) -> str | None:
        if (index := instruction.find(';')) != -1:
            return instruction[index+1:]
        
    def __str__(self) -> str:
        return f"{self.dest=}, {self.comp=}, {self.jump=}"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, CInstruction):
            raise NotImplementedError
        
        return self.comp == other.comp and self.dest == other.dest and self.jump == other.jump


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

def parse_instructions(instructions: list[str]) -> dict[int, str | CInstruction]:
    """
    Parse `instructions` into a dictionary with keys representing line-numbers
        and values representing the instruction (without any leading instruction chars like '@')

    Returns:
        dict[int, str]: `instructions` parsed into a dictionary of line-numbers and
            their corresponding instruction values as strings
    """

    parsed_instructions = {}

    for i, instruction in enumerate(instructions):
        if instruction[0] != VAR_START:
            parsed_instructions[i] = CInstruction(instruction)
        else:
            parsed_instructions[i] = instruction.removeprefix(VAR_START)

    return parsed_instructions
