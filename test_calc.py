import pytest

from calc import add, divide


def test_add():
    assert add(2, 3) == 5


def test_divide_zero_should_raise_value_error():
    with pytest.raises(ValueError):
        divide(1, 0)
