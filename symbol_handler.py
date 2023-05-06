"""
Module to handle symbols in the .asm files
"""

from constants import PRE_DEFINED_SYMBOLS, LABEL_START, LABEL_END, VAR_START


class SymbolHandler:
    """
    Class that maintains the Symbol table and labels for a .asm file.

    Attributes:
        `symbol_table` (dict[str, int]): The symbol table that contains `PRE_DEFINED_SYMBOLS` as well as any
            symbols encountered in the .asm file. Pre-defined symbols and @var symbols reference a memory address.
            (Labels) reference the next line number in the file.
        `next_address` int: Starting at 16, represents the memory address to be assigned to the next
            encountered variable.
    """

    def __init__(self) -> None:
        self.symbol_table: dict[str, int] = PRE_DEFINED_SYMBOLS
        self._next_address: int = 16


    def handle_symbols(self, instructions: list[str]) -> None:
        """
        Handle all symbols in an instruction set by adding to the symbol table where necessary

        Args:
            `instructions` (list[str]): A list of .asm instructions
        """

        raise NotImplementedError


    def handle_symbol(self, symbol: str) -> None:
        """
        Handle a supplied symbol by adding it to the symbol table if it does not already exist there

        Args:
            `symbol` (str): The symbol to be checked and added to the `symbol_table` 
                if it does not already exist
        """

        raise NotImplementedError


    def _handle_label(self, label: str) -> None:
        """
        Labels are different from regular symbols in that they reference the next line-number 
            rather than a memory address.  Handle them by maintaining the surrounding '()'
            and making their value the next line-number (or even the next statement?).
            Add to `symbol_table`

        Args:
            `label` (str): The label to be handled 
        """

        raise NotImplementedError
