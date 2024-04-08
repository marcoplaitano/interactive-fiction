"""
File:   main.py
Brief:  Main file containing the initialization logic and the game's main loop.
Author: Marco Plaitano
Date:   01 Feb 2022

INTERACTIVE FICTION
A choice-based interactive fiction game implemented in Python.
"""

import json
from action import GameAction
from menu import GameMenu
from password import GamePassword
from scene import GameScene
from utils import ask_choice, correct_password, game_error, next_scene


# File containing user's progress to save & load.
SAVE_FILE = "data/save.txt"

# File containing all the scenes to create the game's world with.
STORY_FILE = "data/story.json"



def init_game_data(input_file):
    """Load game scenes from a file.

    Params:
        `str` input_file: path to the file containing the data.
    Return:
        `list` list containing all of the game's Scenes."""
    # Read JSON data.
    try:
        with open(input_file, encoding="UTF-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        game_error(f"Story file {input_file} not found.")

    scenes = {}

    # Objects are Scenes.
    for obj in data:

        # Create list of actions for current scene.
        actions = []
        for action in obj['actions']:
            a_prompt = action["prompt"]
            a_result = action["result"]
            # Not all actions have passwords.
            a_password = None
            if "password" in action:
                p_value = action["password"]["value"]
                p_fail = action["password"]["fail"]
                a_password = GamePassword(p_value, p_fail)

            actions.append(GameAction(a_prompt, a_result, a_password))

        # Create scene.
        tag = obj["tag"]
        title = obj["title"]
        # For the scene's description, accept both a string and an array of strings.
        if type(obj["description"]) == str:
            description = obj["description"]
        else:
            description = "\n".join([line for line in obj["description"]])
        game_over = obj["gameOver"]
        scene = GameScene(tag, title, description, game_over, actions)
        # Check that each tag is unique and map it to the corresponding scene.
        if scenes.get(int(tag)) is not None:
            game_error(f"Tag {tag} is not unique.")
        scenes[int(tag)] = scene

    if len(scenes) == 0:
        game_error("No data has been loaded from the file.")
    return scenes



def main():
    """Game's main function and loop."""
    # Initialize the data.
    all_scenes = init_game_data(STORY_FILE)
    tag_first_scene = 0
    current_scene = next_scene(all_scenes, tag_first_scene, None)
    if current_scene is None:
        exit(1)
    # Create Menu instance.
    menu = GameMenu(SAVE_FILE, all_scenes)

    while True:
        current_scene.show()
        if current_scene.is_over():
            break
        choice = ask_choice(0, current_scene.num_actions())
        if choice == 0:
            current_scene = menu.open(current_scene)
        else:
            # Action is found at index (choice - 1) in the scene's list; this is because 0 is input
            # value reserved to open menu.
            action = current_scene.get_action(choice - 1)
            new_tag = action.result()
            # Change destination tag to fail if input does not match the required password.
            if action.needs_password():
                if not correct_password(action.password().string()):
                    new_tag = action.password().fail()
            current_scene = next_scene(all_scenes, new_tag, current_scene)

    print("THE END\n")


if __name__ == "__main__":
    main()
