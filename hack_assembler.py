from argparse import ArgumentParser, Namespace

from hasm_parser import Parser


def initialize_arguments() -> Namespace:
    """
    Initialize the ArgumentParser for command-line-arguments
    """

    arg_parser = ArgumentParser(
        prog="HackAssembler", description="Assemble Hack .asm file into machine code."
    )
    arg_parser.add_argument(
        "file", type=str, help="absolute filepath to the .asm file to be assembled"
    )

    return arg_parser.parse_args()


if __name__ == "__main__":
    file = initialize_arguments().file

    print(file)
