import pytest
from fuel import convert, gauge


def test_convert_valid():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("0/1") == 0


def test_convert_round():
    assert convert("1/3") == 33
    assert convert("2/3") == 67


def test_convert_value_err():
    with pytest.raises(ValueError):
        convert("cat/2")
    with pytest.raises(ValueError):
        convert("2/cat")
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_convert_floats():
    with pytest.raises(ValueError):
        convert("1.5/3")
    with pytest.raises(ValueError):
        convert("0.5/1.0")


def test_convert_invalid_percentage():
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ValueError):
        convert("1/-2")


def test_convert_zero_division_err():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge_number():
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(33) == "33%"
    assert gauge(67) == "67%"


def test_gauge_empty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
