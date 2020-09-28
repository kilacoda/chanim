"""A few TexTemplate subclasses used internally by chanim but can be used by a user if they want to as well.
Note that setting the TeX template for a scene will affect all subsequent TexMobjects until another change in template.
"""

from manim.utils.tex import TexTemplate


class ChemTemplate(TexTemplate):
    def rebuild_cache(self):
        """Basically a modified version of the original method."""

        self.common_packages.append("chemfig")

        tpl = self.generate_tex_command(
            "documentclass",
            required_params=[self.documentclass[0]],
            optional_params=self.documentclass[1],
        )
        for pkg in self.common_packages:
            tpl += self.generate_usepackage(pkg)

        if self.use_ctex:
            for pkg in self.ctex_packages:
                tpl += self.generate_usepackage(pkg)
        else:
            for pkg in self.tex_packages:
                tpl += self.generate_usepackage(pkg)

        tpl += self.common_preamble_text
        if self.use_ctex:
            tpl += self.ctex_preamble_text
        else:
            tpl += self.tex_preamble_text

        tpl += "\n" r"\begin{document}" "\n"
        tpl += f"\n{self.text_to_replace}\n"
        tpl += "\n" r"\end{document}"

        self.body = tpl

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
        set_chemfig = "\\setchemfig{atom sep=%s,chemfig style=%s, atom style=%s,angle increment=%d,bond offset=%s,double bond sep=%s, node style=%s, bond_style=%s}" % (atom_sep,chemfig_style,atom_style,angle_increment,bond_offset,double_bond_sep,node_style,bond_style)

        self.append_to_preamble(set_chemfig)


class ChemReactionTemplate(ChemTemplate):
    def rebuild_cache(self):
        """Basically a modified version of the modified original method."""

        self.common_packages.append("chemfig")

        tpl = self.generate_tex_command(
            "documentclass",
            required_params=[self.documentclass[0]],
            optional_params=self.documentclass[1],
        )
        for pkg in self.common_packages:
            tpl += self.generate_usepackage(pkg)

        if self.use_ctex:
            for pkg in self.ctex_packages:
                tpl += self.generate_usepackage(pkg)
        else:
            for pkg in self.tex_packages:
                tpl += self.generate_usepackage(pkg)

        tpl += self.common_preamble_text
        if self.use_ctex:
            tpl += self.ctex_preamble_text
        else:
            tpl += self.tex_preamble_text

        tpl += "\n" r"\begin{document}" "\n"
        tpl += f"\n{self.text_to_replace}\n"
        tpl += "\n" r"\end{document}"

        self.body = tpl

    def set_chemfig(
        self,

        ##Individual molecule params
        atom_sep: str = "2em", ## all of these are the defaults in chemfig
        chemfig_style="",
        atom_style="",
        angle_increment=45,
        bond_offset="2pt",
        double_bond_sep="2pt",
        node_style="",
        bond_style="",

        ## Reaction scheme params
        arrow_type="forward",
        arrow_length=1,
        arrow_angle=0,
        arrow_style="",
        debug="false",
    ):
        set_chemfig = "\\setchemfig{atom sep=%s,chemfig style=%s, atom style=%s,angle increment=%d,bond offset=%s,double bond sep=%s, node style=%s, bond_style=%s,scheme debug=%s, atom sep=2em, arrow angle={%d}, arrow coeff={%s}, arrow style={%s}}" % (atom_sep,chemfig_style,atom_style,angle_increment,bond_offset,double_bond_sep,node_style,bond_style,debug, arrow_angle, arrow_length, arrow_style)

        self.append_to_preamble(set_chemfig)
        
    
    def get_text_for_env(self, environment, expression):
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
        begin = r"\begin{" + environment + "}" + "\n\\schemestart"
        end = "\\schemestop\n" + r"\end{" + environment + "}"
        return self.body.replace(
            self.text_to_replace, "{0}\n{1}\n{2}".format(begin,expression, end)
        )
