from third_day import is_ascending, word_concat


def test_is_ascending():

    assert is_ascending(1, 5, 4) == False


def test_word_concat():
    assert word_concat("ecet", "vala") == "ecetvala"

