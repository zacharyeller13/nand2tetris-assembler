"""
Parser class to parse .asm file into a hashtable (dictionary) of lines
and their corresponding instructions
"""

from constants import COMMENT, VAR_START


class Parser:
    """
    Class to parse a file into a list of instructions"

    Attributes:
        `instructions` (list[str]): a list of instructions from the
            file passed to the constructor.

    """

    def __init__(self, file: str) -> None:
        self.instructions: list[str] = self._read_instructions(file)

    def _read_instructions(self, file: str) -> list[str]:
        """
        Private method to read in a file and parse it into
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

    def parse_instructions(self) -> dict[int, str]:
        """
        Parse `instructions` into a dictionary with keys being line-numbers
            and values being the instruction (without any leading instruction chars like '@')

        Returns:
            dict[int, str]: `self.instructions` parsed into a dictionary of line-numbers and
                their corresponding instruction values as strings
        """

        parsed_instructions = {}

        for i, instruction in enumerate(self.instructions):
            parsed_instructions[i] = instruction.removeprefix(VAR_START)

        return parsed_instructions
