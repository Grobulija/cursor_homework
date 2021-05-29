import pytest
from functions_to_test import Calculator


def test_add_successful():
    assert Calculator.add(0, 0) == 0
    assert Calculator.add(1, -2) == -1
    assert Calculator.add(6.3, 4.4) == 10.7


def test_add_error():
    with pytest.raises(TypeError):
        Calculator.add(4, "5")
        Calculator.add("something", 0)
        Calculator.add({1}, [5])


def test_subtract_successful():
    assert Calculator.subtract(0, 0) == 0
    assert Calculator.subtract(1, -2) == 3
    assert Calculator.subtract(6.5, 3.25) == 3.25


def test_subtract_error():
    with pytest.raises(TypeError):
        Calculator.subtract(4, "5")
        Calculator.subtract("something", 0)
        Calculator.subtract({1}, [5])


def test_multiply_successful():
    assert Calculator.multiply(0, 0) == 0
    assert Calculator.multiply(1, -2) == -2
    assert Calculator.multiply(6.5, 3.25) == 21.125



def test_multiply_error():
    with pytest.raises(TypeError):
        Calculator.multiply({1}, [5])


def test_divide_successful():
    assert Calculator.divide(1, 1) == 1
    assert Calculator.divide(1, -2) == -0.5
    assert Calculator.divide(6.3, 4.2) == 1.5


def test_divide_error():
    with pytest.raises(TypeError):
        Calculator.divide(4, "5")
        Calculator.divide("something", 0)
        Calculator.divide({1}, [5])


if __name__ == "main":
    test_add_successful()
    test_add_error()
    test_subtract_successful()
    test_subtract_error()
    test_multiply_successful()
    test_multiply_error()
    test_divide_successful()
    test_divide_error()
