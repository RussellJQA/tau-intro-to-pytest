"""
This module contains a basic accumulator class.
Its purpose is to show how to use the pytest framework for testing classes.
"""


class Accumulator:
    """Class: Accumulator"""
    def __init__(self):
        self._count = 0  # private variable (starts with an underscore)

    @property
    def count(self):
        """A getter() function"""
        return self._count

    def add(self, more=1):
        self._count += more
