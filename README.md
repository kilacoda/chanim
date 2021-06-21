# Chanim
This is an extension to 3BlueBrown's [Manim](https://www.github.com/ManimCommunity/manim) library,
for making videos regarding chemistry.

## Installation (pip)
`pip install chanim`

## Installation (Source)
1. Get manim as described [here](https://docs.manim.community/en/latest/installation.html) according to your OS,  or `pip install manim`. You'll have to download other required modules as explained at the manim docs page.
2. Clone the contents of this repository.
3. Open a terminal in the cloned directory and run `pip install -e .` (note: requires `pip` to be installed, see how to install for your OS), or if you prefer to use [poetry](https://python-poetry.org) instead, `poetry install`.

That's about it. You can now do `from chanim import <*|object_name>` like any regular Python package. 

## Usage
```py
from chanim import *

class MoleculeOrReaction(Scene):
    <name> = ChemObject(<chemfig code>)
    self.play(Write(<name>))
```

Type this into a python (`.py`) file (changing whatever's necessary, i.e. stuff inside the angle brackets). I'll assume you named it `chem.py`

In your command prompt/terminal write this (assuming you're in your project directory):

```sh
manim chem.py MoleculeOrReaction -pl
```
This'll render your Scene and preview it in your default player (in 'l'ow quality).

Here's a little example of it working.

```py
from chanim import *

class ChanimScene(Scene):
    def construct(self):
        chem = ChemWithName("*6((=O)-N(-CH_3)-*5(-N=-N(-CH_3)-=)--(=O)-N(-H_3C)-)")

        self.play(chem.creation_anim())
        self.wait()
```
![output](https://raw.githubusercontent.com/raghavg123/chanim/master/ChanimScene.gif)
Congrats! You've written and played your first animation (or "chanimation" should I say)

Explore the code and docs (not written yet) for more on how to use chanim.

## Abilities
Currently chanim only supports drawing compounds and reactions along with a few chemfig commands (such as coordinate bonds and complexes etc.) but more is to come! If you have a suggestion, file an issue with a proper tag.

## A Quick Note
There may be some faulty code and a lot of this may not be well made/documented. Feel free to file an issue if something doesn't work properly.
