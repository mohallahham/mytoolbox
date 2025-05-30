"""
pytest for exercises/beginner/pig_latin.py
------------------------------------------

We load the exercise module dynamically *by file location* so we don't have
to alter PYTHONPATH or turn the exercises folder into a package.
"""

from pathlib import Path
import importlib.util
import sys

MODULE_PATH = Path(__file__).parents[1] / "exercises" / "beginner" / "pig_latin.py"

spec = importlib.util.spec_from_file_location("pig_latin", str(MODULE_PATH))
pig_latin = importlib.util.module_from_spec(spec)  # create empty module
sys.modules[spec.name] = pig_latin  # register (optional)
spec.loader.exec_module(pig_latin)  # run the file


def test_consonant_word():
    assert pig_latin.translate("python") == "ythonpay"


def test_vowel_word():
    assert pig_latin.translate("apple") == "appleyay"


def test_empty_string():
    assert pig_latin.translate("") == ""
