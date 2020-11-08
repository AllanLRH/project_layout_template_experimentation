import pytest
from src.ahrithemetic import *


def test_my_sum_1():
    assert my_sum(2, 3) == 5


def test_my_sum_2():
    with pytest.raises(AssertionError):
        assert my_sum(2, 3) == 4


def test_my_sum_3():
    assert my_sum('b', 'r' * 8) == 'brrrrrrrr'
