"""A few TexTemplate subclasses used internally by chanim but can be used by a user if they want to as well.
Note that setting the TeX template for a scene will affect all subsequent TexMobjects until another change in template.
"""

from typing import overload
from manim.utils.tex import TexTemplate, TexTemplateFromFile


class ChemTemplate(TexTemplate):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.add_to_preamble("\\usepackage{chemfig}")


    def set_chemfig(
        self,
        atom_sep: str = "2em", ## all of these are the defaults in chemfig
        chemfig_style="",
        atom_style="",
        angle_increment=45,
        bond_offset="2pt",
        double_bond_sep="2pt",
        node_style="",
        bond_style="",
    ):
        set_chemfig = "\\setchemfig{atom sep=%s,chemfig style=%s, atom style=%s,angle increment=%d,bond offset=%s,double bond sep=%s, node style=%s, bond style=%s}" % (atom_sep,chemfig_style,atom_style,angle_increment,bond_offset,double_bond_sep,node_style,bond_style)

        self.add_to_preamble(set_chemfig)


class ChemReactionTemplate(TexTemplate):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.add_to_preamble("\\usepackage{chemfig}")

    def set_chemfig(
        self,

        ##Individual molecule params
        atom_sep: str = "2em", ## all of these are the defaults in chemfig
        chemfig_style:str="",
        atom_style:str="",
        angle_increment:int=45,
        bond_offset:str="2pt",
        double_bond_sep:str="2pt",
        node_style:str="",
        bond_style:str="",

        ## Reaction scheme params
        arrow_length:int=1,
        arrow_angle:int=0,
        arrow_style:int="",
        debug:str="false",
    ):
        set_chemfig = "\\setchemfig{atom sep=%s,chemfig style=%s, atom style=%s,angle increment=%d,bond offset=%s,double bond sep=%s, node style=%s, bond style=%s,scheme debug=%s, atom sep=2em, arrow angle={%d}, arrow coeff={%s}, arrow style={%s}}" % (atom_sep,chemfig_style,atom_style,angle_increment,bond_offset,double_bond_sep,node_style,bond_style,debug, arrow_angle, arrow_length, arrow_style)

        self.add_to_preamble(set_chemfig)
    
    def get_texcode_for_expression(self, expression):
        """Inserts expression verbatim into TeX template.

        Parameters
        ----------
        expression : :class:`str`
            The string containing the expression to be typeset, e.g. ``$\\sqrt{2}$``

        Returns
        -------
        :class:`str`
            LaTeX code based on current template, containing the given ``expression`` and ready for typesetting
        """
        return self.body.replace(self.placeholder_text, "\n\\schemestart\n"+expression+"\n\\schemestop\n\n")

    def get_texcode_for_expression_in_env(self,expression,environment):
        """Inserts an expression wrapped in a given environment into the TeX template.

        Parameters
        ----------
        environment : :class:`str`
            The environment in which we should wrap the expression.
        expression : :class:`str`
            The string containing the expression to be typeset, e.g. ``"$\\sqrt{2}$"``

        Returns
        -------
        :class:`str`
            LaTeX code based on template, containing the given expression and ready for typesetting
        """
        print(environment)
        begin = r"\begin{" + environment + "}" + "\n\\schemestart"
        end = "\\schemestop\n" + r"\end{" + environment + "}"
        print(begin,end)
        return self.body.replace(
            self.placeholder_text, "{0}\n{1}\n{2}".format(begin,expression, end)
        )
