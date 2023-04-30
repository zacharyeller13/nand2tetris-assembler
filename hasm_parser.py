from constants import COMMENT, VAR_START


def parse_file(file: str) -> list[str]:
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

def parse_instructions(instructions: list[str]) -> dict[int, str]:
    """
    Parse `instructions` into a dictionary with keys representing line-numbers
        and values representing the instruction (without any leading instruction chars like '@')

    Returns:
        dict[int, str]: `instructions` parsed into a dictionary of line-numbers and
            their corresponding instruction values as strings
    """

    parsed_instructions = {}

    for i, instruction in enumerate(instructions):
        parsed_instructions[i] = instruction.removeprefix(VAR_START)

    return parsed_instructions
