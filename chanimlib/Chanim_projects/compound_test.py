from chanimlib.imports import *
from .compounds import *

class Compounds(Scene):
    CONFIG = {}
    def construct(self):
    #    propanol = PrimaryAlcohol(3)
       eth = ChemObject(Ethanol)
       self.play(Write(eth)) 
       self.wait(3)


# class Compounds1(Scene):
#     def construct(self):
