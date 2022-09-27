import pytest
from natural import natural, SignError


def test_natural_ok():
    assert 421 == natural("421")
    assert 1001 == natural("1001")
    assert 9 == natural("9")


def test_natural_ok_limite():
    assert 0 == natural("0")
    assert 0 == natural("-0")


def test_natural_ValueError():
    with pytest.raises(ValueError):
        natural("abc")
    with pytest.raises(ValueError):
        natural("")


def test_natural_ValueError():
    with pytest.raises(SignError):
        natural("-421")
    with pytest.raises(SignError):
        natural("-1")

