from .chem_objects import ChemObject

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

methyl = "[4]H-C(-[2]H)(-[6]H)"

methylene = "-C(-[2]H)(-[6]H)"

methine = "-C(-[2]H)"

Phenol = "*6(-=-=(-OH)-=)"

Water = "[5]H-\charge{135 = \:, 225 = \:}{O}-[-1]H"

# Ethanol = PrimaryAlcohol(2)

# Acetic_Acid = Ethanoic_Acid = PrimaryAcid(2)

Benzene = "*6(-=-=-=)"


Benzene_Diazonium_Chloride = BDC = "*6(-=-=(-\\chemabove{N_2}{\quad\scriptstyle+}\\chemabove{Cl}{\quad\scriptstyle-})-=-)"

Aniline ="*6(-=-=(-NH2)-=-)"

Carbon_Dioxide = CO2 = "[4]O=C=O"


## Bonds that can be a pain in the arse

def cbond(
          _dir="->",
          angle=0,
          coeff=1.2,
          n1="",
          n2=""
        ) -> str:
    """func cbond

    Return the code for a coordinate/dative bond

    Args:
        _dir : Direction of the arrow
        angle: Angle from baseline
        coeff: Bond length multiplier
        n1/n2: Atom identifiers

    Returns:
        A string with the list of all this stuff.
    """
    # bond = []
    # for param in params:
    #     if param
    # arrow = "->"
    return f"[{angle},{coeff},{n1},{n2},{_dir}]"

CBL=C_BOND_LEFT = COORDINATE_BOND_LEFT = cbond("<-")
CBR=C_BOND_RIGHT = COORDINATE_BOND_RIGHT = cbond("->")
