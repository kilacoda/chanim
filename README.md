# Chanim
This is an extension to 3BlueBrown's [Manim](https://www.github.com/3b1b/manim) library,
for making videos regarding chemistry.

# NOTE
This branch (`master`) will not work with [ManimCE](https://github.com/ManimCommunity/manim). Checkout the ManimCE-TexTemplate-Working branch if you want to do that. Read the note below for more info.

**This branch will be merged with the ManimCE-TexTemplate-Working branch on January 15, 2021, and chanim will henceforth cease to work with 3b1b/manim. In case you're using chanim for any purposes at the moment, I would advise that you migrate to ManimCE before said date. Read the last section for more info.**

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

Also, at the moment chanim's master branch (the one you're on) won't work with the [community version of manim](https://github.com/ManimCommunity/manim) due to the changes in how the TeX templates are used and modified, though only on he master branch. See the [ManimCE-TexTemplate-Working](https://github.com/raghavg123/chanim/tree/ManimCE-TexTemplate-Working) branch for a ManimCE compatible version.

## Why deprecate this branch?
When I started writing chanim back at the start of 2020, the state of manim was quite different to what it is now. Back then, I had to do hacky things like making custom `constants.py` files and thus held off on releasing chanim to PyPI, since I didn't know how to replicate such things as a package.

However, now with ManimCE, and the `TexTemplate` functionality that comes alongwith it, I can (and already have) do the same things via normal code, and less hacks. Thus, I can package chanim for PyPI to make it more easier for people to use. I do believe this tool could be useful to other people as well, and the first step is to move onwards from 3b1b/manim and becoming a plugin for ManimCE that is published and updated on PyPI.

Another reason is that I personally never use the master branch, nor am I updating it anymore, due to my priorities as of late being getting chanim up and running with ManimCE, since it makes (at least mine) life easier. Easier to maintain, scene caching reduces render times drastically, better CLI interface, lots of bugfixes, the list goes on. The 3b1b/manim repo on the other hand is practically never updated except (even for fixing bugs) for the shaders branch, which although a really cool development, I can't see myself using anytime soon.

TL;DR I don't see the benefit of keeping `3b1b/manim`-compatible while keeping the `ManimCE` version in a separate branch and asking people to `git checkout` to that branch if they want to use the new features. Hence, branch merge on **January 15th, 2021**

If you have any objections or feel you have a better solution, feel free to contact me or file an issue.