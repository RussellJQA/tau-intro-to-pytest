"""
This module contains basic unit tests for math operations.
Their puspose is to show how to use the pytest framework by example.
"""

import pytest


@pytest.mark.math
def test_one_plus_one():
    """A most basic test function"""
    assert 1 + 1 == 2


@pytest.mark.math
def test_one_plus_two():
    """A test function to show assertion introspection"""
    a = 1
    b = 2

    # The assert below will fail with pytest assert introspection displaying:
    #   E        assert (1 + 2) == 0
    # immediately below it.
    # c = 0
    # assert a + b == c

    # The assert below will pass.
    c = 3
    assert a + b == c


@pytest.mark.math
def test_divide_by_zero():
    """A test function that verifies an exception"""
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)


products = [  # Multiplication test cases:
    (2, 3, 6),  # two positive integers
    (1, 99, 99),  # identity: multiplying any number by 1
    (0, 100, 0),  # zero: multiplying any number by 0
    (2, -3, -6),  # positive by a negative
    (-2, -3, 6),  # negative by a negative
    (2.5, 2.5, 6.25)  # multiply floats
]

# def test_multiply_two_positive_ints():
#     assert 2 * 3 == 6
# def test_multiply_identify():
#     assert 1 * 99 == 99
# def test_multiply_zerio():
#     assert 0 * 100 == 0


# DRY Principle: Don't Repeat Yourself!
@pytest.mark.math
@pytest.mark.parametrize("a, b, product", products)
def test_multiply_two_numbers(a, b, product):
    """A parametrized test function"""
    assert a * b == product
