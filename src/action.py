"""
File:   action.py
Brief:  This file contains the definition of a Game's Action.
Author: Marco Plaitano
Date:   01 Feb 2022

INTERACTIVE FICTION
A choice-based interactive fiction game implemented in Python.
"""

from src.password import GamePassword


class GameAction:
    """This class represents an action the player can perform in the game."""

    def __init__(self, prompt, result, password):
        self._validate_parameters(prompt, result, password)
        self._prompt = prompt.strip()
        self._result = result
        self._password = password


    def show(self):
        """Print action in defined format."""
        print(f"{self._prompt}")


    def result(self):
        """Get action's result.

        Result is the tag of the Scene this action leads to when performed."""
        return self._result


    def needs_password(self):
        """Tell whether the player has to input a password to perform the action."""
        return self._password is not None


    def password(self):
        """Get action's password."""
        return self._password


    def _validate_parameters(self, prompt, result, password):
        """Check that every parameter is of the correct type and that the values can be accepted.

        The need for this function arises from the fact that values are read from a JSON file."""
        if not isinstance(prompt, str) or len(prompt.strip()) == 0:
            raise TypeError("Action's prompt must be a non-empty string.")
        if not isinstance(result, int) or result < 0:
            raise TypeError("Action's result must be a non-negative integer.")
        if password is not None:
            if not isinstance(password, GamePassword):
                raise TypeError("Action's password must be of type GamePassword.")


    def __hash__(self):
        return hash(self._prompt, self._result)


    def __eq__(self, other):
        if not isinstance(other, GameAction):
            return False
        return self._prompt == other._prompt and self._result == other._result


    def __str__(self):
        return f"ACTION\nPrompt: {self._prompt}\nResult: {self._result}\nPassword: {self._password}"
