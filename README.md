# INTERACTIVE FICTION

A choice-based interactive fiction game implemented in Python.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

## Description

In [this type] of game, the player is presented with a situation, a "scene", and
the only way to progress is by choosing the next move from a list of possible
actions related to that particular scene.  
Each action results in a different outcome, leading to a new situation.

![demo image]

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

## Usage

Clone or [download] this project and *cd* into its root directory.

Run the game with the following command:

```shell
python main.py
```

### How to play

Every scene is presented with a *title*, a *description* and a numbered list of
all the possible *actions*; to choose from the list, simply type in the number
corresponding to the action you want to perform.

### Passwords

When you choose an action, to actually perform it, you might be asked to input a
string.  
Only if the string given in input matches a certain value the action will be
considered successful.  
An example of this might be choosing actions similar to "Answer the question" or
"Type the password".

### Menu

Type **0** at any time during the game to access the menu and perform actions
like saving/loading the progress or quitting the game.

### Save & Load

You can save & load the progress to/from a text file via the game's menu.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

## Write a new story

The source code is completely oblivious of the game's story and contents. It is,
therefore, really easy to tweak the one presented or write a completely new one.  
To do so, one has to edit a single [JSON file].

The entirety of the game data can be represented with 3 simple abstractions:

### Scene

The JSON object representing a *Scene* has the following elements:

+ title
+ description
+ tag  
A non-negative, unique integer to identify the scene with.
+ gameOver  
Boolean value; if ```true``` the game ends when the player reaches the scene.
+ actions  
An array of [Action] objects.  

### Action

The JSON object representing an *Action* has the following elements:

+ prompt  
A string that describes the action.
+ result  
A non-negative integer; it represents the **tag** of the *Scene* that will
follow the performing of this action.

Optionally, an *Action* may contain a *Password* object.

### Password

The JSON object representing a *Password* has the following elements:

+ value  
String that will be compared to the user input.
+ fail  
A non-negative integer; it represents the **tag** of the *Scene* that will
follow the performing of this action if the user input does not match the
password's value.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

## Dependencies

+ Python 3.6+

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

[download]:
https://github.com/marcoplaitano/interactive-fiction/archive/refs/heads/master.zip
"Repository download"

[JSON file]:
data/story.json
"Repository file"

[Action]:
#action
"Anchor to header"

[MIT]:
LICENSE
"Repository file"
