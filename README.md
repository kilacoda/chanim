# Chanim
This is an extension to 3BlueBrown's [Manim](https://www.github.com/ManimCommunity/manim) library,
for making videos regarding chemistry.

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

~~Also, at the moment chanim won't work with the [community version of manim](https://github.com/ManimCommunity/manim) due to the changes in how the TeX templates are used and modified, which I haven't really figured out how to incorporate with chanim. It may become an addon at some point, but not anytime in the near future unfortunately. Thus consider using the 3b1b/manim version instead.~~

**Chanim is compatible with ManimCE now, but unforunately it is not backward compatible with the 3b1b version.** Also, it isn't an "addon" for the time being, so you'll still have to clone it and use it like earlier.
