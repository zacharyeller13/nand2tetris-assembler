"""
Module to handle symbols in the .asm files
"""

from constants import PRE_DEFINED_SYMBOLS, LABEL_START, LABEL_END, VAR_START


class SymbolHandler:
    """
    Class that maintains the Symbol table and labels for a .asm file.

    Attributes:
        `symbol_table` (dict[str, int]): The symbol table that contains `PRE_DEFINED_SYMBOLS`
            as well as any symbols encountered in the .asm file.
            Pre-defined symbols and @var symbols reference a memory address.
            (Labels) reference the next line number in the file.
        `next_address` int: Starting at 16, represents the memory address to be assigned to the next
            encountered variable.
    """

    def __init__(self) -> None:
        self.symbol_table: dict[str, int] = PRE_DEFINED_SYMBOLS.copy()
        self._next_address: int = 16

    def handle_symbols(self, instructions: list[str]) -> None:
        """
        Handle all symbols in an instruction set by adding to the symbol table where necessary

        Args:
            `instructions` (list[str]): A list of .asm instructions
        """

        # TODO - May not actually be necessary if we read in at time of parsing instructions
        raise NotImplementedError

    def handle_symbol(self, symbol: str, line_num: int) -> str | None:
        """
        Handle a supplied symbol by adding it to the symbol table if it does not already exist there

        Args:
            `symbol` (str): The symbol to be checked and added to the `symbol_table`
                if it does not already exist
            `line_num` (int): The line number of this symbol in the .asm file

        Returns:
            str | None: The cleaned symbol (removed '@') if symbol is an @var;
                None if symbol is a (Label) declaration
        """

        if self._is_label(symbol):
            self._handle_label(symbol, line_num)
        else:
            symbol = symbol.removeprefix(VAR_START)
            if not self.symbol_table.get(symbol):
                self._add_var(symbol)
            return symbol

    def _is_label(self, symbol: str) -> bool:
        """
        Check if a symbol being handled is a label

        Args:
            `symbol` (str): The symbol to be checked
        """

        return symbol.startswith(LABEL_START) and symbol.endswith(LABEL_END)

    def _handle_label(self, label: str, line_num: int) -> None:
        """
        Handle supplied label by adding it to the symbol table if it does not already exist

        Args:
            `label` (str): The label to be checked and added to the `symbol_table`
            `line_num` (int): The line number passed through from `handle_symbol`
        """

        label = label.removeprefix(LABEL_START).removesuffix(LABEL_END)

        if not self.symbol_table.get(label):
            self.symbol_table[label] = line_num

    def _add_var(self, symbol: str) -> None:
        """
        Add a symbol to the `symbol_table` and increment `_next_address`
        
        Args:
            `symbol`: The symbol to be added
        """

        self.symbol_table[symbol] = self._next_address
        self._next_address += 1