import pytest

from calc import add, divide


def test_add():
    assert add(2, 3) == 5


def test_divide_normal():
    assert divide(6, 3) == 2
    assert divide(7, 2) == 3.5


def test_divide_zero_should_raise_value_error():
    with pytest.raises(ValueError) as excinfo:
        divide(1, 0)
    # 抛出的异常应带可读说明，而非未处理的 ZeroDivisionError
    assert "0" in str(excinfo.value)
    assert str(excinfo.value).strip()


@pytest.mark.parametrize("b", [0, 0.0, -0.0])
def test_divide_zero_variants_raise_value_error(b):
    with pytest.raises(ValueError):
        divide(1, b)


def test_divide_zero_does_not_raise_zero_division_error():
    try:
        divide(1, 0)
    except ValueError:
        pass
    except ZeroDivisionError as exc:
        pytest.fail(f"不应抛出 ZeroDivisionError: {exc}")
    else:
        pytest.fail("除数为 0 时应抛出 ValueError")


@pytest.mark.parametrize("a", [0, -1, 3])
def test_divide_zero_raises_value_error_for_any_numerator(a):
    # 0 / 0、负数 / 0 等原本同样会抛出未处理的 ZeroDivisionError
    with pytest.raises(ValueError):
        divide(a, 0)


def test_divide_zero_error_message_is_descriptive():
    with pytest.raises(ValueError) as excinfo:
        divide(1, 0)
    message = str(excinfo.value).strip()
    assert message, "ValueError 应携带可读说明"
    assert "0" in message, "说明中应指出除数 0"
