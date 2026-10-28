import pytest

from shop import discount


def test_discount_10_percent():
    assert discount(100, 10) == 90

def test_discount_0_percent():
    assert discount(100, 0) == 100

def test_discount_150_percent():
    raise ValueError