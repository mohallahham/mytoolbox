from mytoolbox.utils.word_counter import (
    count_words,
    remove_punctuations,
    sort_words_by_frequency,
)


def test_capital_normalization():
    input = "hello Hello world"
    expected_output = {"hello": 2, "world": 1}
    assert count_words(input) == expected_output


def test_empty_text():
    input = ""
    expected_output = {}
    assert count_words(input) == expected_output


def test_remove_punctuations():
    input = "hello, world!"
    expected_output = "hello world"
    assert remove_punctuations(input) == expected_output


def test_sort_words_by_frequency_normal():
    input = {"hello": 3, "world": 2, "python": 5}
    expected_output = [("python", 5), ("hello", 3), ("world", 2)]
    assert sort_words_by_frequency(input) == expected_output


def test_sort_words_by_frequency_empty():
    input = {}
    expected_output = []
    assert sort_words_by_frequency(input) == expected_output


def test_sort_words_by_frequency_single_item():
    input = {"onlyword": 1}
    expected_output = [("onlyword", 1)]
    assert sort_words_by_frequency(input) == expected_output
