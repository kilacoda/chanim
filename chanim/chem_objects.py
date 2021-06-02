"""chem_objects.py
This file contains most of the classes provided by chanim. Includes ChemObject, Reaction, BondBreak etc.
"""

from typing import List, Union

import numpy as np

from .templates import ChemReactionTemplate, ChemTemplate
from .utils import Arrows

from manim.mobject.types.vectorized_mobject import VGroup, VMobject
from manim.mobject.svg.tex_mobject import *
from manim.animation.fading import FadeInFrom
from manim.animation.animation import Animation
from manim.animation.creation import Write
from manim.animation.composition import AnimationGroup
from manim.mobject.geometry import DashedLine
from manim.constants import *
from manim.mobject.geometry import Dot
from manim.utils.color import YELLOW
from manim.opengl import OpenGLMathTex
from manim._config import logger


def check_if_instance_change_if_not(obj, instance_of):
    if not isinstance(obj, instance_of):
        obj = instance_of(obj)


class ChemObject(MathTex):
    """
    `chanimlib.chem_objects.ChemObject`

    Chemical Object
    ===============

    Uses `chemfig` to create two-dimensional molecular/atomic structures.
    Only accepts `chemfig` commands.\n
    Example:\n
    >>> water = ChemObject("H_2O")    ## Linear Structure

    or

    >>> water = ChemObject("H[5]-O-H[-1]")      ## After repulsion

    You can also set various prperties of the molecule using keyword arguments. See
    `__init__` and page 7 of the manual (http://ctan.imsc.res.in/macros/generic/chemfig/chemfig-en.pdf)
    """

    # CONFIG = {"stroke_width": 2, "tex_template": ChemTemplate()}

    def __init__(
        self,
        chem_code: str,
        atom_sep: str = "2em",  ## all of these are the defaults in chemfig
        chemfig_style: str = "",
        atom_style: str = "",
        angle_increment: int = 45,
        bond_offset: str = "2pt",
        double_bond_sep: str = "2pt",
        node_style: str = "",
        bond_style: str = "",
        stroke_width: str = 2,
        tex_template=ChemTemplate,
        **kwargs,
    ):
        # digest_config(self, kwargs)
        self.template: ChemTemplate = tex_template()
        self.template.set_chemfig(
            atom_sep=atom_sep,
            chemfig_style=chemfig_style,
            atom_style=atom_style,
            angle_increment=angle_increment,
            bond_offset=bond_offset,
            double_bond_sep=double_bond_sep,
            node_style=node_style,
            bond_style=bond_style,
        )
        super().__init__(
            "\\chemfig{%s}" % chem_code,
            stroke_width=stroke_width,
            tex_template=self.template,
            **kwargs,
        )

    def set_ion_position(
        self, string_number=0, e_index=0, final_atom_index=1, direction=LEFT
    ):
        """
        This is to facilitate shifting of ionic and lewis electrons,
        by `.move_to`'ing them to the direction you provide.
        """

        self[string_number][e_index].move_to(
            self[final_atom_index].get_edge_center(direction) + direction * 0.2
        )


class OpenGLChemObject(OpenGLMathTex):
    """
    `chanimlib.chem_objects.ChemObject`

    Chemical Object
    ===============

    Uses `chemfig` to create two-dimensional molecular/atomic structures.
    Only accepts `chemfig` commands.\n
    Example:\n
    >>> water = ChemObject("H_2O")    ## Linear Structure

    or

    >>> water = ChemObject("H[5]-O-H[-1]")      ## After repulsion

    You can also set various prperties of the molecule using keyword arguments. See
    `__init__` and page 7 of the manual (http://ctan.imsc.res.in/macros/generic/chemfig/chemfig-en.pdf)
    """

    # CONFIG = {"stroke_width": 2, "tex_template": ChemTemplate()}

    def __init__(
        self,
        chem_code: str,
        atom_sep: str = "2em",  ## all of these are the defaults in chemfig
        chemfig_style: str = "",
        atom_style: str = "",
        angle_increment: int = 45,
        bond_offset: str = "2pt",
        double_bond_sep: str = "2pt",
        node_style: str = "",
        bond_style: str = "",
        stroke_width: str = 5,
        tex_template=ChemTemplate,
        **kwargs,
    ):
        # digest_config(self, kwargs)
        self.template: ChemTemplate = tex_template()
        self.template.set_chemfig(
            atom_sep=atom_sep,
            chemfig_style=chemfig_style,
            atom_style=atom_style,
            angle_increment=angle_increment,
            bond_offset=bond_offset,
            double_bond_sep=double_bond_sep,
            node_style=node_style,
            bond_style=bond_style,
        )
        super().__init__(
            "\\chemfig{%s}" % chem_code,
            stroke_width=stroke_width,
            tex_template=self.template,
            **kwargs,
        )

    def set_ion_position(
        self, string_number=0, e_index=0, final_atom_index=1, direction=LEFT
    ):
        """
        This is to facilitate shifting of ionic and lewis electrons,
        by `.move_to`'ing them to the direction you provide.
        """

        self[string_number][e_index].move_to(
            self[final_atom_index].get_edge_center(direction) + direction * 0.2
        )


class ComplexChemIon(MathTex):
    """
    Mono-ionic Complexes
    """

    # CONFIG = {"stroke_width": 2, "charge": ""}

    def __init__(
        self,
        chem_code,
        stroke_width=2,
        charge="",
        tex_template=ChemTemplate(),
        **kwargs,
    ):
        # digest_config(self, kwargs)
        self.comp = "\chemleft[\chemfig{" + chem_code + "}\chemright]^{%s}" % charge
        MathTex.__init__(
            self,
            self.comp,
            stroke_width=stroke_width,
            tex_template=tex_template,
            **kwargs,
        )


class ComplexChemCompound(MathTex):
    """
    Di-ionic Complexes
    """

    # CONFIG = {"stroke_width": 2}

    def __init__(
        self,
        cation: Union[str, ChemObject, ComplexChemIon],
        anion: Union[str, ChemObject, ComplexChemIon],
        stroke_width=2,
        **kwargs,
    ):

        if isinstance(cation, ComplexChemIon):
            cation = cation.comp
        elif isinstance(cation, ChemObject):
            cation = cation.tex_strings[0]

        if isinstance(anion, ComplexChemIon):
            anion = anion.comp
        elif isinstance(anion, ChemObject):
            anion = anion.tex_strings[0]

        MathTex.__init__(self, cation, anion, stroke_width=stroke_width, **kwargs)


## IT'S BWOKEN!! *sob*
## UPDATE 21/04/20: This... works again for some reason?
## UPDATE 07/05/20: Use Something like FadeIn for this instead of Write; because Write is fokken broken.
class Reaction(Tex):
    """
    `chanimlib.chem_objects.Reaction`
    Reaction
    ========
    Writes out a traditional chem formula

    It is recommended to use a list and not a tuple, especially if you are having only one
    reactant or product. It causes errors as python treats single items inside
    tuples as an argument of its own. So ("O=H") becomes "O","=","H".
    If you really want to use a tuple for some reason,
    add a comma at the end of the 0th item,e.g. ("O=H",)

    Arrow types:
    ============

    "forward": "->",

    "backward": "<-",

    "eq": "<=>",

    "eq_fw": "<->>",

    "eq_bw": "<<->",

    "double": "<->",

    "space": "0",

    "split": "-U"
    """

    # CONFIG = {
    #     "stroke_width": 2,
    #     # "use_hbox":false,
    #     "excluded_strings": ["\\schemestart", "\\schemestop", "\\\\"],
    #     "alignment": "",
    #     "tex_template": ChemReactionTemplate(),
    # }

    def __init__(
        self,
        reactants: List[str] = None,
        products: List[str] = None,
        arrow_type: Arrows = Arrows.forward,
        arrow_length=1,
        arrow_angle=0,
        arrow_style="",
        arrow_text_up="",
        arrow_text_down="",
        arrow_align_params="",
        debug="false",
        # use_hbox=False, idk why this is here, probably not needed now
        ## styling params from ChemObject, just keeping them here in case anyone wants to get funky with their molecule designs.
        atom_sep: str = "2em",  ## all of these are the defaults in chemfig
        chemfig_style="",
        atom_style="",
        angle_increment=45,
        bond_offset="2pt",
        double_bond_sep="2pt",
        node_style="",
        bond_style="",
        stroke_width=2,
        tex_template=ChemReactionTemplate,
        **kwargs,
    ):

        # digest_config(self, kwargs)

        # old code
        # if use_hbox:
        #     self.template_tex_file_body = TEMPLATE_CHEM_REACTION_FILE_BODY_WITH_HBOX

        self.template: ChemReactionTemplate = tex_template()
        self.template.set_chemfig(
            atom_sep=atom_sep,
            chemfig_style=chemfig_style,
            atom_style=atom_style,
            angle_increment=angle_increment,
            bond_offset=bond_offset,
            double_bond_sep=double_bond_sep,
            node_style=node_style,
            bond_style=bond_style,
            arrow_length=arrow_length,
            arrow_angle=arrow_angle,
            arrow_style=arrow_style,
            debug=debug,
        )

        if reactants is None:
            logger.warning("No reactants provided, defaulting to empty list.")
            self.reactants = []

        if products is None:
            logger.warning("No products provided, defaulting to empty list.")
            self.products = []

        if all([hasattr(reactants, "__iter__"), hasattr(reactants, "__iter__")]):
            self.reactants = reactants
            self.products = products
        else:
            raise TypeError("Reaction reactants and products must be None or iterable.")

        ## Arrow stuff
        if type(arrow_type) == Arrows:
            self.arrow_type = arrow_type.value
        elif arrow_type in Arrows.__members__.keys():  # handles old strings
            self.arrow_type = Arrows[arrow_type].value
        else:
            logger.warning(
                "Arrow type not recognised. Defaulting to Arrows.forward (->)"
            )
            self.arrow_type = Arrows.forward.value

        self.arrow_text_up = arrow_text_up
        self.arrow_text_down = arrow_text_down
        self.arrow_align_params = arrow_align_params

        self.equation = self.get_equation()
        # print(repr(self.equation))

        super().__init__(
            *self.equation,
            stroke_width=stroke_width,
            tex_template=self.template,
            **kwargs,
        )

        ##Convenience aliases.
        self.arrow = self[2 * len(self.reactants) - 1]
        self.reactants = self[: 2 * len(self.reactants) - 1 : 2]
        self.products = self[2 * len(self.reactants) :: 2]

    def get_equation(self):
        if self.arrow_align_params != "":
            arrow = "\\arrow(%s){%s[%s][%s]}" % (
                self.arrow_align_params,
                self.arrow_type,
                self.arrow_text_up,
                self.arrow_text_down,
            )
        else:
            arrow = "\\arrow{%s[%s][%s]}" % (
                self.arrow_type,
                self.arrow_text_up,
                self.arrow_text_down,
            )

        # ## To prevent manim from writing the arrow to a separate file.
        # self.excluded_strings.append(arrow)
        # print(self.excluded_strings) ##for debugging
        r = [
            "\\chemfig{" + R + "}"
            # if R != self.reactants[-1] and len(self.reactants) != 1
            # else "\\chemfig{" + R + "}"
            if "chemfig" not in R else R
            for R in self.reactants
        ]

        self.insert_in_odd_places("\+", r)

        p = [
            "\\chemfig{" + P + "}"
            # if P != self.products[-1] and len(self.products) != 1
            # else "\\chemfig{" + P + "}"
            if "chemfig" not in P else P
            for P in self.products
        ]

        self.insert_in_odd_places("\+", p)

        eq = [*r, arrow, *p]

        return eq

    def insert_in_odd_places(self, obj, iterable: list):
        """
        No pun intended.
        """

        n = len(iterable)
        # print(n)

        if n != 1:
            indexes_to_insert_at = np.array(range(1, n))
            print(indexes_to_insert_at)

            for i in indexes_to_insert_at:
                iterable.insert(-i, obj)
                print(iterable)
                indexes_to_insert_at += 1

    # I think this was intended to give a dict or something of all reactants and products. IDK
    def get_breakdown_dict(self):
        pass

    # can't really think of a better name for this atm, and show will overwrite Mobject.show
    def creation_anim(
        self,
        text_anim: Animation = Write,
        arrow_anim: Animation = FadeInFrom,
        reactant_product_simultaneity=False,
        **kwargs,
    ) -> AnimationGroup:
        """Workaround and shortcut method to overcome the bugs in `Write`.

        Args:
            text_anim (Animation, optional): The animation on the reactants and products. Defaults to Write.
            arrow_anim (Animation, optional): The animation on the arrow. Defaults to FadeInFrom.
            reactant_product_simultaneity (bool, optional): Whether to animate the reactants and products together or not.
        Returns:
            AnimationGroup: The group of animations on the text and arrow.
        """
        text = VGroup(
            self[0 : 2 * len(self.reactants) - 1], self[2 * len(self.reactants) :]
        )
        arrow = self[2 * len(self.reactants) - 1]

        if "text_kwargs" not in kwargs.keys():
            kwargs["text_kwargs"] = dict()

        if "arrow_kwargs" not in kwargs.keys():
            kwargs["arrow_kwargs"] = dict()

        if "group_kwargs" not in kwargs.keys():
            kwargs["group_kwargs"] = dict()

        print(kwargs["group_kwargs"])

        anim_group = (
            AnimationGroup(
                text_anim(text[0]), text_anim(text[1]), arrow_anim(arrow), **kwargs
            )
            if reactant_product_simultaneity
            else AnimationGroup(text_anim(text), arrow_anim(arrow), **kwargs)
        )

        try:
            print(anim_group.run_time)
        except Exception:
            pass
        return anim_group


class ChemArrow(MathTex):
    """
    `chanimlib.chem_objects.ChemArrow`
    Chemical Reaction Arrow
    =======================
    Basically a Reaction without any reactants/products.

    May change later.
    """

    # CONFIG = {
    #     "stroke_width": 2,
    # }

    arrows = {
        "forward": "->",
        "backward": "<-",
        "eq": "<=>",
        "eq_fw": "<->>",
        "eq_bw": "<<->",
        "double": "<->",
        "space": "0",
        "split": "-U>",
    }

    def __init__(
        self,
        _type="forward",
        length=1,
        angle=0,
        style="{}",
        text_up="",
        text_down="",
        stroke_width=2,
        **kwargs,
    ):
        # digest_config(self, kwargs)
        set_chemfig = """\\setchemfig{atom sep=2em,
                                      arrow angle={%d},
                                      arrow coeff={%s},
                                      arrow style=%s }""" % (
            angle,
            length,
            style,
        )
        self.template_tex_file_body = self.template_tex_file_body.replace(
            "\\setchemfig{atom sep=2em}", f"{set_chemfig}"
        )

        arrow = "\\arrow{%s[%s][%s]}" % (self.arrows[_type], text_up, text_down)
        MathTex.__init__(self, arrow, stroke_width=stroke_width, **kwargs)


class ChemName(MathTex):
    """`chanimlib.chem_objects.ChemName`

    An attempt to use chemfig's \\chemname{} macro.

    This will only be written in one go, so if you'd like
    animations for both parts see `ChemWithName`.

    NOTE: To be deprecated. Use `ChemWithName` instead
    """

    # CONFIG = {"stroke_width": 2}

    def __init__(self, chem, name, buff=1, stroke_width=2, **kwargs):
        # digest_config(self, kwargs)

        chem_with_name = "\\chemname[%sem]{\\chemfig{%s}}{%s}" % (buff, chem, name)
        # self.template_tex_file_body = TEMPLATE_CHEM_FILE_BODY.replace(
        #     "\\chemfig{",
        #     chem_with_name)

        MathTex.__init__(self, chem_with_name, stroke_width=stroke_width, **kwargs)


class ChemWithName(VMobject):
    """
    `chanimlib.chem_objects.ChemWithName`
    Chemical With Name
    ==================
    A better version of `ChemName` that allows you to animate
    either part.

    To animate:
    -----------
    ```py
    ChemWithName.creation_anim(chem_anim,name_anim)
    ```


    inspired by `BraceLabel`
    """

    CONFIG = {"label_constructor": Tex, "buff": 1}

    def __init__(
        self, chem, name, name_direction=DOWN, label_constructor=Tex, buff=1, **kwargs
    ):

        super().__init__(self, **kwargs)

        if isinstance(
            chem, (ChemObject, ComplexChemIon, ComplexChemCompound, ChemAbove)
        ):
            self.chem = chem
        else:
            self.chem = ChemObject(chem, **kwargs)

        if isinstance(name, label_constructor):
            self.name = name
        else:
            self.name: Tex = label_constructor(name, **kwargs)

        self.name.next_to(self.chem, name_direction, buff=buff)

        self.submobjects = [self.chem, self.name]

    def creation_anim(
        self, chem_anim: Animation = Write, name_anim: Animation = FadeInFrom
    ):
        return AnimationGroup(chem_anim(self.chem), name_anim(self.name))


class ChemAbove(ChemObject):
    def __init__(self, chem, above_chem, hspace="3mm", vspace="1mm", **kwargs):
        ChemObject.__init__(
            self,
            "\\chemabove{%s}{\\hspace{%s} \\vspace{%s} %s}"
            % (chem, hspace, vspace, above_chem),
            **kwargs,
        )


# Doesn't work, somebody fix this or I'll say it's deprecated.


class ReactionVGroup(VGroup):
    CONFIG = {
        "_type": "forward",
        "length": 1,
        "angle": 0,
        "style": "{}",
        "text_up": "",
        "text_down": "",
    }

    def __init__(
        self,
        reactants: List[ChemObject] = [],
        products: List[ChemObject] = [],
        **arrow_kwargs,
    ):
        raise DeprecationWarning(
            "ReactionVGroup doesn't work, and will probably be removed in the future"
        )
        digest_config(self, arrow_kwargs)
        arrow = ChemArrow(
            self._type,
            self.length,
            self.angle,
            self.style,
            self.text_up,
            self.text_down,
        )

        r = self.get_side_of_equation(reactants)
        p = self.get_side_of_equation(products)

        self.set_same_height_for_all_mobjects(r)
        self.set_same_height_for_all_mobjects(p)
        self.set_same_height_for_all_mobjects([VGroup(*r), arrow, VGroup(*p)])

        VGroup.__init__(*[*r, arrow, *p])

    def get_side_of_equation(self, iterableable):
        # A = [
        #     *(Participant, MathTex("+")) if Participant != iterableable[-1]
        #     else Participant
        #     for Participant in iterableable
        # ]

        A = []
        for Part in iterableable:
            if Part != iterableable[-1]:
                A.extend([ChemObject(Part), MathTex("+")])
            else:
                A.append(ChemObject(Part))
        return A

    def set_same_height_for_all_mobjects(self, iterableable):
        for index in range(len(iterableable)):
            if index != 0:
                iterableable[index].set_y(iterableable[index - 1].get_y())


class BondBreak(DashedLine):
    """
    `chanimlib.chem_objects.BondBreak`

    Bond Break
    ----------

    A line that splits a given ``bond``.
    """

    # CONFIG = {
    #     "length": 0.7,
    # }

    def __init__(self, bond: TexSymbol, length=0.7, **kwargs):
        # digest_config(self, kwargs)
        start = bond.get_center() + (length / 2) * DOWN
        end = start + length * UP

        DashedLine.__init__(self, start=start, end=end)


class ElectronPair(VGroup):
    """Electron Pair: Two electrons (Dots) in a VGroup

    Arguments:
        None -- Just use this as it is and change the kwargs if you want
    """

    # CONFIG = dict(color=YELLOW, pair_buff=0.15)

    def __init__(self, color=YELLOW, pair_buff=0.15, **kwargs):
        super().__init__(
            Dot(radius=DEFAULT_SMALL_DOT_RADIUS),
            Dot(RADIUS=DEFAULT_SMALL_DOT_RADIUS),
            **kwargs,
        )
        self.arrange(RIGHT, buff=pair_buff).set_color(color)


## Aliases
Formula = ChemObject
CArrow = ChemArrow
React = Reaction
