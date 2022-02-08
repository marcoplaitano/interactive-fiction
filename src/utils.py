"""
File:   utils.py
Brief:  This file contains the definition of functions needed to handle the player interaction with
        the program.
Author: Marco Plaitano
Date:   01 Feb 2022

INTERACTIVE FICTION
A choice-based interactive fiction game implemented in Python.
"""

from os import system, name as os_name



def next_scene(all_scenes, new_tag, current_scene):
    """Jump to the next scene given its tag.

    Params:
        `list`      all_scenes: all of the game's scenes.
        `int`       new_tag: tag of the next scene.
        `GameScene` curr_scene: current scene.
    Return:
        `GameScene` new scene to jump to (or current one if tag is invalid)."""
    if all_scenes.get(new_tag) is not None:
        return all_scenes.get(new_tag)
    game_error(f"Tag {new_tag} leads nowhere.", False)
    return current_scene



def clear_screen():
    """Clear console screen."""
    if os_name == "posix":
        system("clear")
    else:
        system("cls")



def game_error(err_msg, do_exit=True):
    """Print error message and exit/continue the program.

    Params:
        `str` err_msg: message to print.
        `bool` do_exit: if `True` exit the program."""
    print("ERROR!\n ", err_msg)
    if do_exit:
        print("Exiting game...")
        exit(1)
    else:
        input("Press ENTER to continue...")



def get_input(prompt):
    """Get a string in input.

    Params:
        `str` prompt: to prompt the user with.
    Return:
        `str` user input."""
    string = ""
    while len(string) == 0:
        string = input(prompt).strip()
    return string.lower()



def ask_choice(range_min, range_max):
    """Ask the player for an integer in input in the range `[range_min; range_max]`.

    Params:
        `int` range_min: minimum value accepted.
        `int` range_max: maximum value accepted.
    Return:
        `int` user input."""
    string = get_input("? ")
    try:
        num = int(string)
        if num < range_min or num > range_max:
            raise ValueError
    except ValueError:
        print(f"Invalid input. Choose an integer between {range_min} and {range_max}")
        return ask_choice(range_min, range_max)
    return num



def correct_password(password):
    """
    Ask for a string in input and check whether it matches the given password.

    Params:
        `str` password: the password's string.
    Return
        `bool` `True` if user input and password match; `False` otherwise.
    """
    string = get_input("> ")
    # The following check only applies to the template story presented in the repository.
    if not string.isnumeric():
        print("The keypad only accepts digits.")
        return correct_password(password)
    return string == password
