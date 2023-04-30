from argparse import ArgumentParser, Namespace
import sys

from hasm_parser import Parser


def initialize_argparser() -> ArgumentParser:
    """
    Initialize the ArgumentParser for command-line-arguments
    """

    arg_parser = ArgumentParser(
        prog="HackAssembler", description="Assemble Hack .asm file into machine code."
    )
    arg_parser.add_argument(
        "file", metavar="file.asm", type=str, help="absolute filepath of the .asm file to be assembled"
    )

    return arg_parser


def initialize_arguments(arg_parser: ArgumentParser) -> Namespace:
    """
    Parse command-line-arguments
    """

    arg_namespace = arg_parser.parse_args()

    if arg_namespace.file[-4:] != ".asm":
        arg_parser.print_usage()
        sys.exit()

    return arg_namespace


if __name__ == "__main__":
    
    arg_parser = initialize_argparser()
    file = initialize_arguments(arg_parser).file
