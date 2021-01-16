from manim.animation.transform import Transform, ReplacementTransform

class BondToElectronPair(Transform):
    def __init__(self,mob,bond_pos):
        bond_with_atoms = mob[0][bond_pos-2:band_pos+1]
        
        atom_2 = mob[0][bond_pos-1]
        atom_1 = mob[0][bond_pos-2]

        # e_pair = self.get_pair_as_per_bond_orientation(bond)
        e_pair = "\\lewis"
        Transform.__init__(bond,e_pair)

    def get_pair_as_per_bond_orientation(self,bond):
        pass