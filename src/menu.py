"""
File:   utils.py
Brief:  This file contains the definition of the Game's Menu.
Author: Marco Plaitano
Date:   02 Feb 2022

INTERACTIVE FICTION
A choice-based interactive fiction game implemented in Python.
"""

from src.utils import ask_choice, clear_screen, game_error


class GameMenu:
    """This class represents the game's menu."""

    def __init__(self, data_file, all_scenes):
        # File containing the progress data.
        self._data_file = data_file
        # All the game's scenes.
        self._all_scenes = all_scenes
        # Menu's options; each of these has a corresponding method.
        self._options = {1: "Resume", 2: "Save", 3: "Load", 4: "Quit"}


    def open(self, curr_scene):
        """Open the menu and let the user choose an option to execute.

        Params:
            `GameScene` curr_scene: player's current scene.
        Return:
            `GameScene` new scene for the player to start from."""
        # Display the menu with its options.
        clear_screen()
        print("MENU\nThis is the game's menu.\n")
        for option in self._options:
            print(f"{option}. {self._options[option]}")

        # Ask for the option to execute.
        choice = ask_choice(1, len(self._options.keys()))
        option = self._options[choice]

        # Execute menu option.
        if "Resume" == option:
            return self._resume(curr_scene)
        if "Save" == option:
            return self._save(curr_scene)
        if "Load" == option:
            return self._load(curr_scene)
        if "Quit" == option:
            self._quit()


    def _resume(self, curr_scene):
        """Exit menu and resume game from current scene.

        Params:
            `GameScene` curr_scene: player's current scene.
        Return:
            `GameScene` current scene."""
        return curr_scene


    def _save(self, curr_scene):
        """Save current progress to a file.

        Params:
            `GameScene` curr_scene: player's current scene.
        Return:
            `GameScene` current scene."""
        try:
            with open(self._data_file, "w", encoding="UTF-8") as file:
                file.write(str(curr_scene.tag()))
            input("Done.\nPress ENTER to continue...")
        except OSError:
            game_error("Could not save the data to a file.", False)
        return curr_scene


    def _load(self, curr_scene):
        """Load previously saved game.

        Params:
            `GameScene` curr_scene: player's current scene.
        Return:
            `GameScene` new scene (or current one if load from file fails)."""
        try:
            with open(self._data_file, "r", encoding="UTF-8") as file:
                tag = file.readline()
            try:
                tag = int(tag)
                if tag < 0:
                    raise ValueError
            except ValueError:
                game_error("Corrupted data; could not load previous game.", False)
                return curr_scene
        except FileNotFoundError:
            game_error("Data file not found; could not load previous game.", False)
            return curr_scene

        if self._all_scenes.get(tag) is not None:
            input("Done.\nPress ENTER to continue...")
            return self._all_scenes.get(tag)

        game_error("Corrupted data; could not load previous game.", False)
        return curr_scene


    def _quit(self):
        """Quit the game."""
        print("Exiting game...")
        exit(0)
