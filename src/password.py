"""
File:   password.py
Brief:  This file contains the definition of a Game's Password.
Author: Marco Plaitano
Date:   02 Feb 2022

INTERACTIVE FICTION
A choice-based interactive fiction game implemented in Python.
"""


class GamePassword:
    """This class represents a password needed to complete an action in the game."""

    def __init__(self, string, fail):
        self._validate_parameters(string, fail)
        self._string = string.strip().lower()
        self._fail = fail


    def string(self):
        """Get password's string."""
        return self._string


    def fail(self):
        """Get password's fail tag."""
        return self._fail


    def _validate_parameters(self, string, fail):
        """Check that every parameter is of the correct type and that the values can be accepted.

        The need for this function arises from the fact that values are read from a JSON file."""
        if not isinstance(string, str) or len(string.strip()) == 0:
            raise TypeError("Password's string must be a non-empty string.")
        if not isinstance(fail, int) or fail < 0:
            raise TypeError("Password's fail must be a non-negative integer.")


    def __hash__(self):
        return hash(self._string, self._fail)


    def __eq__(self, other):
        if not isinstance(other, GamePassword):
            return False
        return self._string == other._string and self._fail == other._fail


    def __str__(self):
        return f"PASSWORD\nValue: {self._string}\nFail: {self._fail}"
