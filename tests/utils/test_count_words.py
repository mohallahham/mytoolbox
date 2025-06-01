from mytoolbox.utils.word_counter import count_words


def test_capital_normalization():
    assert count_words("hello Hello world") == {"hello": 2, "world": 1}


def test_empty_text():
    assert count_words("") == {}
