# Chanim
This is an extension to 3BlueBrown's [Manim](https://www.github.com/3b1b/manim) library,
for making videos regarding chemistry.

# NOTE
This branch (`master`) will not work with ManimCE. Checkout the ManimCE-TexTemplate-Working branch if you want to do that. Read the note below for more info.

## Installation
1. Get manim from the above link or `pip install manimlib`. You'll have to download other 
required modules as explained at the manim page.
2. Clone the contents of this repository to where you'll keep your animation projects.
3. Replace the `constants.py` file in your installed manim location with the one provided here
or just replace this:
```py
with open(TEMPLATE_TEX_FILE, "r") as infile:
    TEMPLATE_TEXT_FILE_BODY = infile.read()

    TEMPLATE_TEX_FILE_BODY = TEMPLATE_TEXT_FILE_BODY.replace(
        TEX_TEXT_TO_REPLACE,
        "\\begin{align*}\n" + TEX_TEXT_TO_REPLACE + "\n\\end{align*}",
    )
```
with this:
```py
with open(TEMPLATE_TEX_FILE, "r") as infile:
    TEMPLATE_TEXT_FILE_BODY = infile.read()
    
    TEMPLATE_CHEM_FILE_BODY = TEMPLATE_TEXT_FILE_BODY.replace(
        TEX_TEXT_TO_REPLACE,
        "\\begin{align*}\n" + "\\setchemfig{atom sep = 2em}\n\\chemfig{" +
        TEX_TEXT_TO_REPLACE+"}" + "\n\\end{align*}",
    )
    TEMPLATE_CHEM_REACTION_FILE_BODY = TEMPLATE_TEXT_FILE_BODY.replace(
        TEX_TEXT_TO_REPLACE,
        "\\begin{align*}\n" +"\\setchemfig{atom sep=2em}\n"+"\\schemestart\n"+
        TEX_TEXT_TO_REPLACE +"\n\\schemestop"+"\n\\end{align*}" 
    )
    TEMPLATE_TEX_FILE_BODY = TEMPLATE_TEXT_FILE_BODY.replace(
        TEX_TEXT_TO_REPLACE,
        "\\begin{align*}\n" + TEX_TEXT_TO_REPLACE + "\n\\end{align*}",
    )

```

4. Add `\usepackage{chemfig}` to the `manimlib\tex_template.tex` and `manimlib\ctex_template.tex`
files, like all the other packages listed there.

That's about it.

## Usage
```py
from chanim.imports import *

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

Congrats! You've written and played your first animation (or "chanimation" should I say)

Explore the code and docs (not written yet) for more on how to use chanim.

## Abilities
Currently chanim only supports drawing compounds and reactions along with a few chemfig commands (such as coordinate bonds and complexes etc.) but more is to come! If you have a suggestion, file an issue with a proper tag.

## A Quick Note
There may be some faulty code and a lot of this may not be well made/documented. Feel free to file an issue if something doesn't work properly.

Also, at the moment chanim won't work with the [community version of manim](https://github.com/ManimCommunity/manim) due to the changes in how the TeX templates are used and modified, though only on he master branch. See the [ManimCE-TexTemplate-Working](https://github.com/raghavg123/chanim/tree/ManimCE-TexTemplate-Working) branch for a ManimCE compatible version.
