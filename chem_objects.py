from manimlib.mobject.types.vectorized_mobject import VGroup, VMobject
from manimlib.mobject.svg.tex_mobject import *
from typing import List, Tuple, Union
from manimlib.animation.fading import FadeInFromDown
from manimlib.animation.animation import Animation
from manimlib.animation.creation import Write
from manimlib.animation.composition import AnimationGroup
from manimlib.mobject.geometry import DashedLine
from manimlib.constants import *
from manimlib.utils.config_ops import digest_locals
from manimlib.mobject.geometry import SmallDot


def check_if_instance_change_if_not(obj, instance_of):
    if not isinstance(obj, instance_of):
        obj = instance_of(obj)


class ChemObject(TexMobject):
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
    """

    CONFIG = {"stroke_width": 2, "template_tex_file_body": TEMPLATE_CHEM_FILE_BODY}

    def set_ion_position(
        self, string_number=0, e_index=0, final_atom_index=1, direction=LEFT
    ):
        """
        This is to facilitate shifting of ionic and lewis electrons,
        by '.move_to''ing them to the direction you provide.
        """

        self[string_number][e_index].move_to(
            self[final_atom_index].get_edge_center(direction) + direction * 0.2
        )


class ComplexChemIon(TexMobject):
    """
    Mono-ionic Complexes
    """

    CONFIG = {"stroke_width": 2, "charge": ""}

    def __init__(self, chem_code, **kwargs):
        digest_config(self, kwargs)
        self.comp = (
            "\chemleft[\chemfig{" + chem_code + "}\chemright]^{%s}" % self.charge
        )
        TexMobject.__init__(self, self.comp, **kwargs)


class ComplexChemCompound(TexMobject):
    """
    Di-ionic Complexes
    """

    CONFIG = {"stroke_width": 2}

    def __init__(
        self,
        cation: Union[str, ChemObject, ComplexChemIon],
        anion: Union[str, ChemObject, ComplexChemIon],
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

        TexMobject.__init__(self, cation, anion, **kwargs)


## IT'S BWOKEN!! *sob*
## UPDATE 21/04/20: This... works again for some reason?
## UPDATE 07/05/20: Use Something like FadeIn for this instead of Write; because Write is fokken broken.
class Reaction(TexMobject):
    """
    `chanimlib.chem_objects.Reaction`
    Reaction
    ========
    Writes out a traditional chem formula

    Always use a list and not a tuple, especially if you are having only one
    reactant or product. It causes errors as python treats single items inside
    tuples as arguments. So "O=H" becomes "O","=","H"\n
    Trust me, this gave me a headache for a while.

    TODO: Fix this entire thing. It's fucking messed up. Also, check what happens \\
    when you change the [index] element and if it works like a TexMobject.

    I also kind of hate the current implementation of this because it forces one to\\
    use chemfig strings instead of ChemObjects, which basically renders them useless,\\
    while creating additional problems while indexing the atoms.


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

    CONFIG = {
        "stroke_width": 2,
        # "use_hbox":false,
        "template_tex_file_body": TEMPLATE_CHEM_REACTION_FILE_BODY,
        "excluded_strings": ["\\+"],
    }

    arrows = {
        "forward": "->",
        "backward": "<-",
        "eq": "<=>",
        "eq_fw": "<->>",
        "eq_bw": "<<->",
        "double": "<->",
        "space": "0",
        "split": "-U",
    }

    def __init__(
        self,
        reactants: List[str] = [],
        products: List[str] = [],
        arrow_type="forward",
        arrow_length=1,
        arrow_angle=0,
        arrow_style="",
        arrow_text_up="",
        arrow_text_down="",
        arrow_align_params="",
        debug="false",
        use_hbox=False,
        **kwargs,
    ):

        digest_config(self, kwargs)

        if use_hbox:
            self.template_tex_file_body = TEMPLATE_CHEM_REACTION_FILE_BODY_WITH_HBOX

        set_chemfig = (
            "\\setchemfig{scheme debug=%s, atom sep=2em, arrow angle={%d}, arrow coeff={%s}, arrow style={%s}}"
            % (debug, arrow_angle, arrow_length, arrow_style)
        )
        self.template_tex_file_body = self.template_tex_file_body.replace(
            "\\setchemfig{atom sep=2em}", f"{set_chemfig}"
        )

        self.reactants = reactants
        self.products = products
        # print(self.reactants,self.products)
        self.arrow_type = arrow_type
        self.arrow_text_up = arrow_text_up
        self.arrow_text_down = arrow_text_down
        self.arrow_align_params = arrow_align_params

        self.equation = self.get_equation()
        print(repr(self.equation))

        TexMobject.__init__(self, *self.equation)

        ##Convenience aliases.
        self.arrow = self[2 * len(self.reactants) - 1]
        self.reactants = self[:2 * len(self.reactants) - 1:2]
        self.products = self[2 * len(self.reactants)::2]

    def get_equation(self):
        if self.arrow_align_params != "":
            arrow = "\\arrow(%s){%s[%s][%s]}" % (
                self.arrow_align_params,
                self.arrows[self.arrow_type],
                self.arrow_text_up,
                self.arrow_text_down,
            )
        else:
            arrow = "\\arrow{%s[%s][%s]}" % (
                self.arrows[self.arrow_type],
                self.arrow_text_up,
                self.arrow_text_down,
            )

        # ## To prevent manim from writing the arrow to a separate file.
        self.excluded_strings.append(arrow)
        print(self.excluded_strings)
        print()
        r = [
            "\\chemfig{" + R + "}"
            if R != self.reactants[-1] and len(self.reactants) != 1
            else "\\chemfig{" + R + "}"
            for R in self.reactants
        ]

        self.insert_in_odd_places("\+", r)

        p = [
            "\\chemfig{" + P + "}"
            if P != self.products[-1] and len(self.products) != 1
            else "\\chemfig{" + P + "}"
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
        accumulator = 0

        if n % 2 == 0:
            indexes_to_insert_at = range(n - 1, 0, -1)
            print(list(indexes_to_insert_at))
            for i in indexes_to_insert_at:
                iterable.insert(i, obj)
                print(iterable)
                accumulator += 1
            # iterable.insert(-1, obj)
        elif n % 2 != 0 and n != 1:
            indexes_to_insert_at = [1, *range(n - 1, 0, -1)] if n != 3 else (2, 1)
            print(list(indexes_to_insert_at))
            for i in indexes_to_insert_at:
                iterable.insert(i, obj)
                print(iterable)
                accumulator += 1
                # print(iterable)

    def get_breakdown_dict(self):
        pass

    def show(
        self,
        text_anim: Animation = Write,
        arrow_anim: Animation = FadeInFromDown,
        **kwargs,
    ) -> AnimationGroup:
        """Workaround and shortcut method to overcome the bugs in `Write`.

        Args:
            text_anim (Animation, optional): The animation on the reactants and products. Defaults to Write.
            arrow_anim (Animation, optional): The animation on the arrow. Defaults to FadeInFromDown.

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
        
        anim_group = AnimationGroup(
            text_anim(text),
            arrow_anim(arrow),
            **kwargs
        )
        
        try:
            print(anim_group.run_time)
        except Exception:
            pass
        return anim_group


class ChemArrow(TexMobject):
    """
    `chanimlib.chem_objects.ChemArrow`
    Chemical Reaction Arrow
    =======================
    Basically a Reaction without any reactants/products.

    May change later.
    """

    CONFIG = {
        "stroke_width": 2,
        "template_tex_file_body": TEMPLATE_CHEM_REACTION_FILE_BODY,
    }

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
        **kwargs,
    ):
        digest_config(self, kwargs)
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
        TexMobject.__init__(self, arrow)


class ChemName(TexMobject):

    """
    `chanimlib.chem_objects.ChemName`

    An attempt to use chemfig's \\chemname{} macro.

    This will only be written in one go, so if you'd like
    animations for both parts see `ChemWithName`.
    """

    CONFIG = {"template_tex_file_body": TEMPLATE_CHEMNAME_FILE_BODY, "stroke_width": 2}

    def __init__(self, chem, name, buff=1, **kwargs):
        digest_config(self, kwargs)

        chem_with_name = "\\chemname[%sem]{\\chemfig{%s}}{%s}" % (buff, chem, name)
        # self.template_tex_file_body = TEMPLATE_CHEM_FILE_BODY.replace(
        #     "\\chemfig{",
        #     chem_with_name)

        TexMobject.__init__(self, chem_with_name)


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
    """

    CONFIG = {"label_constructor": TextMobject, "buff": 1}

    def __init__(self, chem, name, name_direction=DOWN, **kwargs):

        VMobject.__init__(self, **kwargs)

        if isinstance(chem, ChemObject):
            self.chem = chem
        else:
            self.chem = ChemObject(chem, **kwargs)

        if isinstance(name, self.label_constructor):
            self.name = name
        else:
            self.name = self.label_constructor(name, **kwargs)

        self.name.next_to(self.chem, name_direction, buff=self.buff)

        self.submobjects = [self.chem, self.name]

    def creation_anim(self, chem_anim=Write, name_anim=FadeInFromDown):
        return AnimationGroup(chem_anim(self.chem), name_anim(self.name))


class ChemAbove(ChemObject):
    def __init__(self, chem, above_chem, hspace="3mm", vspace="1mm"):
        ChemObject.__init__(
            self,
            "\\chemabove{%s}{\\hspace{%s} \\vspace{%s} %s}"
            % (chem, hspace, vspace, above_chem),
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
        #     *(Participant, TexMobject("+")) if Participant != iterableable[-1]
        #     else Participant
        #     for Participant in iterableable
        # ]

        A = []
        for Part in iterableable:
            if Part != iterableable[-1]:
                A.extend([ChemObject(Part), TexMobject("+")])
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

    CONFIG = {
        "length": 0.7,
    }

    def __init__(self, bond, **kwargs):
        digest_config(self, kwargs)
        start = bond.get_center() + (self.length / 2) * DOWN
        end = start + self.length * UP

        DashedLine.__init__(self, start=start, end=end)


class ElectronPair(VGroup):
    """Electron Pair: Two electrons (SmallDots) in a VGroup

    Arguments:
        None -- Just use this as it is and change the CONFIG stuff if you want
    """

    CONFIG = dict(color=YELLOW, pair_buff=0.15)

    def __init__(self, **kwargs):
        super().__init__(SmallDot(), SmallDot(), **kwargs)
        self.arrange(RIGHT, buff=self.pair_buff).set_color(self.color)


Formula = ChemObject
CArrow = ChemArrow
React = Reaction
