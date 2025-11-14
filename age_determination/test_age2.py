import pytest
from age import categorize_byAge


def test_child():
    assert categorize_byAge(9) == "Child"
def test_teenager():
    assert categorize_byAge(18) == "Teenager"
def test_adult():
    assert categorize_byAge(64) == "Adult"
def test_goldenage():
    assert categorize_byAge(100) == "Golden Age"