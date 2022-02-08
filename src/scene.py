"""
File:   scene.py
Brief:  This file contains the definition of a Game's Scene.
Author: Marco Plaitano
Date:   01 Feb 2022

INTERACTIVE FICTION
A choice-based interactive fiction game implemented in Python.
"""

from src.action import GameAction
from src.utils import clear_screen


class GameScene:
    """This class represents a scene of the game the player is presented with."""

    def __init__(self, tag: int, title, description, game_over, actions):
        self._validate_parameters(tag, title, description, game_over, actions)
        # Tag is a non-negative integer that identifies each scene; it should be unique.
        self._tag = tag
        self._title = title.upper()
        self._description = description
        self._actions = actions if actions else []
        self._game_over = game_over


    def tag(self):
        """Get scene's tag."""
        return self._tag


    def is_over(self):
        """Tell whether the game ends when reaching the scene."""
        return self._game_over


    def num_actions(self):
        """Get scene's total number of actions the player can perform."""
        return len(self._actions)


    def show(self):
        """Print scene in defined format."""
        clear_screen()
        if not self._game_over:
            print("Type 0 to access the game's menu")
            print("--------------------------------", end="\n\n")
        print(self._title)
        print(self._description, end="\n\n")
        for i in range(len(self._actions)):
            print(f"{i+1}.", end=" ")
            self._actions[i].show()


    def get_action(self, choice):
        """Get scene's action corresponding to (integer) choice.

        Params:
            `int` choice: representing the action chosen from the list."""
        return self._actions[choice]


    def _validate_parameters(self, tag, title, description, game_over, actions):
        """Check that every parameter is of the correct type and that the values can be accepted.

        The need for this function arises from the fact that values are read from a JSON file."""
        if not isinstance(tag, int) or tag < 0:
            raise TypeError("Scene's tag must be a non-negative, unique integer.")
        if not isinstance(title, str) or len(title) == 0:
            raise TypeError("Scene's title must be a non-empty string.")
        if not isinstance(description, str) or len(description) == 0:
            raise TypeError("Scene's description must be a non-empty string.")
        if not isinstance(actions, list):
            raise TypeError("Scene's actions must be a list of GameActions.")
        for action in actions:
            if not isinstance(action, GameAction):
                raise TypeError("Scene's actions must be of type GameAction")
        if not isinstance(game_over, bool):
            raise TypeError("Scene's game_over must be a boolean value.")
        if not game_over and len(actions) == 0:
            raise ValueError("Actions list cannot be empty if Scene does not conclude the game.")
        if game_over and len(actions) > 0:
            raise ValueError("Actions list must be empty if Scene does conclude the game.")


    def __hash__(self):
        return hash(self._tag, self._title, self._description)


    def __eq__(self, other):
        if not isinstance(other, GameScene):
            return False
        return  self._tag == other._tag and self._title == other._title and \
                self._description == other._description


    def __str__(self):
        string = "SCENE\n"
        string += f"Tag: {self._tag}\n"
        string += f"Game_over: {self._game_over}\n"
        string += f"Title: {self._title.upper()}\n"
        string += "Actions:\n"
        for action in self._actions:
            string += f"  - {action}\n"
        return string
