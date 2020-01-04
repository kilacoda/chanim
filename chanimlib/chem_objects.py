from manimlib.imports import *

## TODO: Add options for reaction mechanisms, like a Reaction Mobject or something
#        Keep params like *reactants,*products,arrow_type,arrow_text


class ChemObject(TexMobject):
    '''
    chanimlib.mobject.svg.tex_mobject.ChemObject

    Chemical Object
    ===============

    NOTE:This is a user defined class which may be expanded further as per need.

    Uses chemfig to create two-dimensional molecular/atomic structures.
    Only accepts chemfig commands.
    Example:
    >>> water = ChemObject("H_2O")    ## Linear Structure
    
    or
    
    >>> water = ChemObject("H[5]-O-H[-1]")      ## After repulsion
    '''

    CONFIG = {
        "stroke_width": 2,
        "template_tex_file_body": TEMPLATE_CHEM_FILE_BODY
    }


class Reaction(TexMobject):
    '''
    Writes out a traditional chem formula
    
    Always use a list and not a tuple, especially if you are having only one
    reactant or product. It causes errors as python treats single items inside 
    tuples as arguments. So "O=H" becomes "O","=","H"
    Trust me, this gave me a headache for a while.
    '''
    np
    CONFIG = {
        "stroke_width": 2,
        "template_tex_file_body": TEMPLATE_CHEM_REACTION_FILE_BODY
    }

    arrows = {"forward": "->",
              "backward": "<-",
              "eq": "<=>",
              "eq_fw": "<->>",
              "eq_bw": "<<->",
              "double": "<->",
              "space": "0",
              "split": "-U"
              }

    def __init__(self,
                 reactants: List[str] = [],
                 products: List[str] = [],
                 arrow_type="forward",
                 arrow_length=1,
                 arrow_angle=0,
                 arrow_style="{}",
                 arrow_text_up="",
                 arrow_text_down="",
                 arrow_align_params="",
                 debug="false",
                 **kwargs):

        digest_config(self, kwargs)

        set_chemfig = "\\setchemfig{scheme debug=%s, atom sep=2em, arrow angle={%d}, arrow coeff={%s}, arrow style=%s}" % (
            debug, arrow_angle,    arrow_length,   arrow_style
        )
        self.template_tex_file_body = self.template_tex_file_body.replace(
            "\\setchemfig{atom sep=2em}",
            f"{set_chemfig}"
        )

        self.reactants = reactants
        self.products = products
        # print(self.reactants,self.products)
        self.arrow_type = arrow_type
        self.arrow_text_up = arrow_text_up
        self.arrow_text_down = arrow_text_down
        self.arrow_align_params = arrow_align_params

        equation = self.get_equation()
        # print(repr(equation))
        TexMobject.__init__(self, *equation)

    def get_equation(self):

        arrow = "\\arrow(%s){%s[%s][%s]}" % (
            self.arrow_align_params,
            self.arrows[self.arrow_type],
            self.arrow_text_up,
            self.arrow_text_down)

        r = ["\\chemfig{ "+R+"} \+ " if R != self.reactants[-1] and len(
            self.reactants) != 1 else "\\chemfig{"+R+"}" for R in self.reactants]
        p = ["\\chemfig{ "+P+"} \+ " if P != self.products[-1]
             and len(self.products) != 1 else "\\chemfig{"+P+"}" for P in self.products]
        eq = [*r, arrow, *p]

        return eq


class ChemArrow(TexMobject):
    """
    Basically a Reaction without any reactants/products.
    
    May change later.
    """

    CONFIG = {
        "stroke_width": 2,
        "template_tex_file_body": TEMPLATE_CHEM_REACTION_FILE_BODY
    }

    arrows = {"forward": "->",
              "backward": "<-",
              "eq": "<=>",
              "eq_fw": "<->>",
              "eq_bw": "<<->",
              "double": "<->",
              "space": "0",
              "split": "-U>"
              }

    def __init__(self,
                 _type="forward",
                 length=1,
                 angle=0,
                 style="{}",
                 text_up="    ",
                 text_down="    ",
                 **kwargs):
        digest_config(self, kwargs)
        set_chemfig = """\\setchemfig{atom sep=2em, 
                                      arrow angle={%d}, 
                                      arrow coeff={%s}, 
                                      arrow style=%s }""" % (
            angle,    length,   style
        )
        self.template_tex_file_body = self.template_tex_file_body.replace(
            "\\setchemfig{atom sep=2em}",
            f"{set_chemfig}"
        )

        arrow = "\\arrow{%s[%s][%s]}" % (
            self.arrows[_type],
            text_up,
            text_down)
        TexMobject.__init__(self, arrow)


class ChemWithName(TexMobject):

    """
    An attempt to use chemfig's \\chemname{} function.

    Work in progress.
    """
    CONFIG = {
        "template_tex_file_body": TEMPLATE_CHEM_FILE_BODY,
        "stroke_width": 2
    }

    def __init__(self, chem, name, buff=1, **kwargs):
        digest_config(self, kwargs)

        chem_with_name = "\\chemname[%s]{%s}{%s" % (
            buff, chem, name
        )
        self.template_tex_file_body = TEMPLATE_CHEM_FILE_BODY.replace(
            "\\chemfig{",
            chem_with_name)

        TexMobject.__init__(self,)
