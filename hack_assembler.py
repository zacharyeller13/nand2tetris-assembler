from argparse import ArgumentParser, Namespace
import sys

from hasm_parser import parse_file, parse_instructions
from translator import translate_instructions


def initialize_argparser() -> ArgumentParser:
    """
    Initialize the ArgumentParser for command-line-arguments
    """

    arg_parser = ArgumentParser(
        prog="HackAssembler", description="Assemble Hack .asm file into machine code."
    )
    arg_parser.add_argument(
        "file",
        metavar="file.asm",
        type=str,
        help="absolute filepath of the .asm file to be assembled",
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
    args = initialize_argparser()
    file = initialize_arguments(args).file

    parsed_file = parse_file(file)
    parsed_instructions = parse_instructions(parsed_file)

    # Test the printout of the instructions dict
    # print(*zip(parsed_instructions.keys(), map(str, parsed_instructions.values())))

    binary_instructions = translate_instructions(parsed_instructions)

    # print(binary_instructions)

    with open(f"{file[:-4]}.hack", 'w', encoding="UTF-8") as f:
        f.write('\n'.join(binary_instructions))
