"""
This module contains basic unit tests for the accum module
Their purpose is to show how to use the pytest framework by example.
"""

# Imports

import pytest

from stuff.accum import Accumulator

# Tests


def test_accumulator_init():
    """Verify that new Accumulator instance has a starting count of 0"""
    accum = Accumulator()
    assert accum.count == 0


def test_accumulator_add_one():
    """Verify that, by default, add() adds 1 to the accumulator count"""
    accum = Accumulator()  # Arrange
    accum.add()  # Act
    assert accum.count == 1  # Assert


def test_accumulator_add_three():
    """Verify that add(3) adds 3 to the accumulator count"""
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3


def test_accumulator_add_twice():
    """Verify that the count increases appropriately w. multiple add() calls"""
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2


def test_accumulator_cannot_set_count_directly():
    """Verify that the count attribute cannot be assigned directly"""
    accum = Accumulator()
    # with pytest.raises(AttributeError, match=r"can't set attribute") as e:
    with pytest.raises(AttributeError, match=r"can't set attribute"):
        accum.count = 10
