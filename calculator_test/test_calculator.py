import pytest
from calculator import sum, subtract, multiply, divide

def test_sum():
    assert sum(3, 5) == 8
    assert sum(-1, 1) == 0
    assert sum(0, 0) == 0
    assert sum(-2, -3) == -5

def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(-1, 1) == -1
    assert multiply(0, 1111) == 0
    assert multiply(-2, -3) == 6

def test_subtract():
    assert subtract(3, 5) == -2
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0
    assert subtract(-2, -3) == 1

def test_divide():
    assert divide(10, 5) == 2
    assert divide(25, 5) == 5
    assert divide(10, 0) == "Error: Division by zero"

#python -m pytest .\test_calculator.py -v