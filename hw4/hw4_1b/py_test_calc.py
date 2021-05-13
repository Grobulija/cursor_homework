import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator.add(0, 0) == 0
    assert Calculator.add(1, -2) == -1
    assert Calculator.add(6.3, 4.4) == 10.7
    with pytest.raises(TypeError):
        Calculator.add(4, "5")
        Calculator.add("something", 0)
        Calculator.add({1}, [5])


def test_subtract():
    assert Calculator.subtract(0, 0) == 0
    assert Calculator.subtract(1, -2) == 3
    assert Calculator.subtract(6.5, 3.25) == 3.25
    with pytest.raises(TypeError):
        Calculator.subtract(4, "5")
        Calculator.subtract("something", 0)
        Calculator.subtract({1}, [5])


def test_multiply():
    assert Calculator.multiply(0, 0) == 0
    assert Calculator.multiply(1, -2) == -2
    assert Calculator.multiply(6.5, 3.25) == 21.125
    with pytest.raises(TypeError):
        Calculator.multiply({1}, [5])


def test_divide():
    assert Calculator.divide(1, 1) == 1
    assert Calculator.divide(1, -2) == -0.5
    assert Calculator.divide(6.3, 4.2) == 1.5
    with pytest.raises(TypeError):
        Calculator.divide(4, "5")
        Calculator.divide("something", 0)
        Calculator.divide({1}, [5])


if __name__ == "main":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
