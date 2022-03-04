from functions_3rd_day import get_max


def test_get_max():
    #given
    a = 5
    b = 10
    #when
    result = get_max(a, b)
    #then
    assert result == 10


def test_get_max_when_the_first_value_is_greater():
    assert get_max(200, 5) == 200
