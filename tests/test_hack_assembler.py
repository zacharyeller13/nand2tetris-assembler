"""
Test methods for main hack_assembler module
"""
from pytest import MonkeyPatch, raises
from hack_assembler import initialize_arguments, Namespace

monkeypatch = MonkeyPatch()

def test_initialize_arguments():
    mock_filepath = "C:/File/Path.asm"

    monkeypatch.setattr("argparse.ArgumentParser.parse_args", lambda _: Namespace(file=mock_filepath))

    args = initialize_arguments()

    assert args.file == mock_filepath

def test_initialize_arguments_invalid_file():
    mock_filepath = "C:/File/Path"

    monkeypatch.setattr("argparse.ArgumentParser.parse_args", lambda _: Namespace(file=mock_filepath))

    args = initialize_arguments()

    assert False # TODO
