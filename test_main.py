import pytest


@pytest.mark.parametrize("test_input,expected", [
    (5.5 + 0.5, 6.0),
    (4 / 2, 2.0),
    (9999999999 - 1, 9999999998.0),
    (-9999999999 + 0, -9999999999)
])
def test_float_positive(test_input, expected):
    assert test_input == expected


def test_float_negative():
    with pytest.raises(TypeError):
        assert 2.0 * 'hello'


@pytest.mark.parametrize("test_input,expected", [
    ([1], [1, 2, 3, 1]),
    (['hello'], [1, 2, 3, 'hello']),
    ([1.1], [1, 2, 3, 1.1]),
    ([100, 200, 300], [1, 2, 3, 100, 200, 300]),
])
def test_list_positive(test_input, expected):
    my_list = [1, 2, 3]
    my_list.extend(test_input)
    assert my_list == expected


def test_list_negative():
    with pytest.raises(TypeError):
        assert [1, 2, 3] + {'key': 'value'}


@pytest.mark.parametrize("test_input,expected", [
    (['x', 'y', 'z'], ('x', 'y', 'z')),
    ([1, 2, 3], (1, 2, 3)),
])
def test_tuple_positive(test_input, expected):
    assert tuple(test_input) == expected


def test_tuple_negative():
    with pytest.raises(TypeError):
        my_tuple = (1, 2, 3)
        my_tuple[0] = 5
