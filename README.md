# INTERACTIVE FICTION

A choice-based interactive fiction game implemented in Python.

In [this type] of game, the player is presented with a situation, a "scene", and
the only way to progress is by choosing the next move from a list of possible
actions related to that particular scene.  
Each action results in a different outcome, leading to a new situation.

![demo image]

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

## Usage

Clone this repository and run the main script:

```shell
python3 main.py
```

### How to play

Every scene is presented with a **title**, a **description** and a numbered list of
all the possible **actions**.  
To choose from the list, simply type in the number corresponding to the action
you want to perform.

#### Passwords

When you choose an action you might be asked to input a string to actually
perform it.  
Only if the string given in input matches a certain value the action will be
considered successful.  
An example of this might be choosing actions similar to "*Answer the question*"
or "*Type the password*".

#### Menu

Type `0` at any time during the game to access the menu and perform actions
like saving/loading the progress or quitting the game.

#### Save & Load

You can save & load the progress to/from a text file via the game's menu.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

## Write a new story

The source code is completely oblivious of the game's story.  
It is really easy to tweak the example presented or write a completely different
story.  
To do so, edit the given [JSON file].

The entirety of the game data can be represented with 3 simple abstractions:

### Scene

The JSON object representing a **Scene** has the following elements:

+ `title`
+ `description`
+ `tag`  
A non-negative, <u>unique</u> integer to identify the scene with.
+ `gameOver`  
Boolean value; if `true` the game ends when the player reaches the scene.
+ `actions`  
An array of **Action** objects.  

### Action

The JSON object representing an **Action** has the following elements:

+ `prompt`  
A string that describes the action.
+ `result`  
A non-negative integer; it represents the `tag` of the **Scene** that will
follow the performing of this action.

Optionally, an **Action** may contain a **Password** object.

### Password

The JSON object representing a **Password** has the following elements:

+ `value`  
String that will be compared to the user input.
+ `fail`  
A non-negative integer; it represents the `tag` of the **Scene** that will
follow the performing of this action if the user input does not match the
password's `value`.

### Example:

```yaml
[
  {
    "title": "Scene 0",
    # --- Description can be multiple lines of text, it must be an array.
    # --- Each line is an entry in the array of strings.
    "description": ["This is the beginning of the game."],
    # --- The first scene must have tag = 0
    "tag": 0,
    "gameOver": false,
    "actions": [
      { "prompt": "Go to scene 1", "result": 1 },
      { "prompt": "Go to scene 2", "result": 2 }
    ]
  },

  {
    "title": "Scene 1",
    "description": ["A new scene of the game."],
    "tag": 1,
    "gameOver": false,
    "actions": [
      { "prompt": "Go back", "result": 0 },
      # --- Go to scene 2 if user answers "hello", scene 0 otherwise
      { "prompt": "What does 'ciao' mean?", "result": 2,
            "password": { "value": "hello", "fail": 0 }
      }
    ]
  },

  {
    "title": "Scene 2",
    "description": ["End of the Game."],
    "tag": 2,
    # --- The game ends in this scene. The array of actions is empty.
    "gameOver": true,
    "actions": []
  }
]
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

## Author

Marco Plaitano

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

## License

Distributed under the [MIT] license.

<!-- LINKS -->

[this type]:
https://www.ifwiki.org/Choice-based_interactive_fiction
"Wiki Article"

[demo image]:
https://github.com/marcoplaitano/images/blob/main/interactive_fiction_demo.png
"Demo image"

[JSON file]:
data/story.json
"Repository file"

[MIT]:
LICENSE
"Repository file"
