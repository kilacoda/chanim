from chanimlib.mobject.svg.tex_mobject import ChemObject

"""
Lazy Classes to create useful organic compounds.
"""

class PrimaryAlcohol(ChemObject):
    """
    Returns a straight chain alcohol.
    chain_length >= 1

    TODO: Isn't working currently for some reason.
          Will fix later.
    """
    def __init__(self, chain_length=1):

        compound = methyl + (chain_length-1)*methylene + "-OH"
        print(compound)

        ChemObject.__init__(self,
                            compound)


class SecondaryAlcohol(ChemObject):
    """
    Use pos >= 2  and chain_length >= 3 for desired results.
    """

    def __init__(self, pos=2, chain_length=3):
        ChemObject.__init__(self,
                            methyl + (pos-1)*methylene +
                            methine + "(-OH)" +
                            (chain_length-pos-1)*methylene + methyl)


class PrimaryAcid(ChemObject):
    """
    Returns a straight chain carboxylic acid.
    chain_length >= 1
    """
    def __init__(self, chain_length=1):
        if chain_length == 1:
            ChemObject.__init__(self,
                                "H[3]-C(-OH[5])=O")
        else:
            compound = methyl + (chain_length-2)*methylene + "-COOH"
            print(compound)
            ChemObject.__init__(self,
                                compound)


"""
These are a few compounds that are very frequently used and 
so can be called directly, without having to write the long chemfig code
again and again. Saves time, really.
"""

methyl = "H[4]-C(-H[2])(-H[6])"

methylene = "-C(-H[2])(-H[6])"

methine = "-C(-H[2])"

Phenol = "*6(-=-=(-OH)-=)"

Water = "H[5]-\lewis{1:2:,O}-H[-1]"

Ethanol = PrimaryAlcohol(2)

Acetic_Acid = Ethanoic_Acid = PrimaryAcid(2)

Benzene = "*6(-=-=-=)"


Benzene_Diazonium_Chloride = BDC = "*6(-=-=(-\\chemabove{N_2}{\quad\scriptstyle+}\\chemabove{Cl}{\quad\scriptstyle-})-=-)"

Aniline ="*6(-=-=(-NH2)-=-)"

Carbon_Dioxide = CO2 = "O[4]=C=O"



