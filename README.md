# Chanim
This is an extension to 3BlueBrown's [Manim](https://www.github.com/ManimCommunity/manim) library,
for making videos regarding chemistry.

# NOTE
This branch (`master`) will not work with [ManimCE](https://github.com/ManimCommunity/manim). Checkout the ManimCE-TexTemplate-Working branch if you want to do that. Read the note below for more info.

**This branch will be merged with the ManimCE-TexTemplate-Working branch on January 15, 2021, and chanim will henceforth cease to work with 3b1b/manim. In case you're using chanim for any purposes at the moment, I would advise that you migrate to ManimCE before said date. Read the last section for more info.**

## Installation
1. Get manim as described [here](https://manimce.readthedocs.io/en/latest/installation.html) according to your OS,  or `pip install manimce` (will be `pip install manim` [soon](https://github.com/pypa/pypi-support/issues/450)). You'll have to download other required modules as explained at the manim page.
2. Clone the contents of this repository.
3. Open a terminal in the cloned directory and run `pip install -e .` (note: requires `pip` to be installed, see how to install for your OS)

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
![output](ChanimScene.gif)
Congrats! You've written and played your first animation (or "chanimation" should I say)

Explore the code and docs (not written yet) for more on how to use chanim.

## Abilities
Currently chanim only supports drawing compounds and reactions along with a few chemfig commands (such as coordinate bonds and complexes etc.) but more is to come! If you have a suggestion, file an issue with a proper tag.

## A Quick Note
There may be some faulty code and a lot of this may not be well made/documented. Feel free to file an issue if something doesn't work properly.

