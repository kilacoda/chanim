# Chanim
This is an extension to [Manim](https://www.github.com/ManimCommunity/manim) library (initially created by [3Blue1Brown](https://github.com/3b1b/manim)),
for making videos regarding chemistry.

## Installation (pip)
`pip install chanim`

## Installation (Source)
1. Install the external dependencies for manim as described [here](https://docs.manim.community/en/latest/installation.html) according to your OS.
2. Clone the contents of this repository.
3. Open a terminal in the cloned directory and run `pip install -e .`, or if you prefer to use [poetry](https://python-poetry.org) instead, `poetry install`. This'll install `manim` for you as well if you don't already have it installed. (you'll still need to setup the external dependencies though)

That's about it. You can now do `from chanim import <*|object_name>` like any regular Python package. 

## Usage

Here's a little example of it working.

```py
from chanim import *

class ChanimScene(Scene):
    def construct(self):
        ## ChemWithName creates a chemical diagram with a name label
        chem = ChemWithName("*6((=O)-N(-CH_3)-*5(-N=-N(-CH_3)-=)--(=O)-N(-H_3C)-)", "Caffeine")

        self.play(chem.creation_anim())
        self.wait()
```

Type this into a python (`.py`) file. I'll assume you named it `chem.py`

In your command prompt/terminal write this (assuming you're in your project directory):

```sh
manim -p -qm chem.py ChanimScene
```
This'll render your Scene and `p`review it in your default player (in `m`edium `q`uality).

![output](https://raw.githubusercontent.com/raghavg123/chanim/master/ChanimScene.mp4)
Congrats! You've written and played your first animation with chanim (or "chanimation" should I say)

Explore the code and docs (coming soon!) for more on how to use chanim.

## Abilities
Currently chanim only supports drawing compounds and reactions along with a few chemfig commands (such as coordinate bonds and complexes etc.) but more is to come! If you have a suggestion, file an issue with a proper tag.

## A Quick Note
There may be some faulty code and a lot of this may not be well made/documented. Feel free to file an issue if something doesn't work properly.
