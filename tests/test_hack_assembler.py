"""
Test methods for main hack_assembler module
"""
import sys
from io import StringIO
from pytest import MonkeyPatch, raises
from hack_assembler import initialize_arguments, initialize_argparser, Namespace

monkeypatch = MonkeyPatch()
arg_parser = initialize_argparser()

def test_initialize_arguments():
    mock_filepath = "C:/File/Path.asm"

    monkeypatch.setattr("argparse.ArgumentParser.parse_args", lambda _: Namespace(file=mock_filepath))

    args = initialize_arguments(arg_parser)

    assert args.file == mock_filepath

def test_initialize_arguments_invalid_file():
    mock_filepath = "C:/File/Path"

    monkeypatch.setattr("argparse.ArgumentParser.parse_args", lambda _: Namespace(file=mock_filepath))

    with raises(SystemExit):
        initialize_arguments(arg_parser)
