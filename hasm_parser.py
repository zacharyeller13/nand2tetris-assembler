import constants


class Parser:
    def __init__(self, file: str) -> None:
        self.instructions = self._read_instructions(file)

    def _read_instructions(self, file: str) -> list[str]:
        """Private method to read in a file and parse it into
        a list of instructions without whitespace or comments

        Args:
            file (str): The filepath to the file to be parsed

        Returns:
            list[str]: The file parsed into a list of strings without
                whitespace or comments

        """
        with open(file, "r", encoding="UTF-8") as f:
            lines = f.read().split("\n")
            lines = [
                line.split("//")[0].strip()
                for line in lines
                if line != "" and line[:2] != "//"
            ]

            return lines
