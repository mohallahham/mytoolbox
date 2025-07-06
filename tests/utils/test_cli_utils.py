import pytest
from mytoolbox.utils.cli_utlis import prompt_input


def test_prompt_input_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "  hello  ")
    result = prompt_input()
    assert result == "hello"


def test_prompt_input_quit(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "q")

    with pytest.raises(SystemExit) as e:
        prompt_input()

    assert e.value.code == 0


def test_prompt_input_empty_then_valid(monkeypatch):
    inputs = iter(["   ", "test"])  # simulate first blank, then a real input
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = prompt_input()
    assert result == "test"
