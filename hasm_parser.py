from constants import COMMENT, VAR_START


class Parser:
    """Class to parse a file into a list of instructions"

    Attributes:
        `instructions` (list[str]): a list of instructions from the
            file passed to the constructor.
        `commands` (dict[int, string]): a dictionary with line number
            and Instruction object that holds the necessary fields of the instruction

    """

    def __init__(self, file: str) -> None:
        self.instructions: list[str] = self._read_instructions(file)

    def _read_instructions(self, file: str) -> list[str]:
        """Private method to read in a file and parse it into
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


class Instruction:
    """Class to hold the main string representation of any instruction
        and its 3 primary fields

    Attributes:
        `type` (str): One of A, C, or Label
        `comp` (str | None): The comp parts of the C instruction
        `dest` (str | None): The dest parts of the C instruction
        `jump` (str | None): The jump parts of the C instruction

    """

    def __init__(self, instruction: str):
        self.type = self._parse_type(instruction)
        self.comp = self._parse_comp(instruction)
        self.dest = self._parse_dest(instruction)
        self.jump = self._parse_jump(instruction)

    def _parse_type(self, instruction: str) -> str:
        if instruction[0] == VAR_START:
            return "A"
        else:
            return "C"

    def _parse_comp(self, instruction: str):
        raise NotImplementedError

    def _parse_dest(self, instruction: str):
        raise NotImplementedError

    def _parse_jump(self, instruction: str):
        raise NotImplementedError
