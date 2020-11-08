"""
This module contains basic unit tests for math operations.
Their puspose is to show how to use the pytest framework by example.
"""


def test_one_plus_one():
    assert 1 + 1 == 2


def test_one_plus_two():
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
