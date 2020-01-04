from chanimlib.imports import *
from .compounds import *

class FirstMolecule(Scene):
    def construct(self):
        ## Ethanoic Acid
        formula1 = Formula("H-C(-[2]H)(-[6]H)-C(=[7]O)(-[1]OH)")
        name1 = TextMobject("Ethanoic Acid").next_to(formula1,DOWN)
        
        item1 = VGroup(formula1,name1).set_color_by_gradient(ORANGE,BLUE)
        item1.to_edge(LEFT)

        ## Fisher Projection of α-D-Glucose

        x = "(-[4]H)(-[0]OH)"
        y = "(-[0]H)(-[4]OH)"
        formula2 = Formula(f"[2]CH_2OH-{x}-{x}-{y}-{x}-C(-[3]H)(=[1]O)").scale(0.75)
        name2 = TextMobject("$\\alpha$-D(+) Glucose").next_to(formula2,DOWN)

        item2 = VGroup(formula2,name2).set_color_by_gradient(GREEN,BLUE)

        ## Benzene Diazonium Chloride

        formula3 = Formula(
            "*6(-=-=(-\\chemabove{N_2}{\quad\scriptstyle+}\\chemabove{Cl}{\quad\scriptstyle-})-=-)"
        )
        name3 = TextMobject(
            "Benzene \\\\",
            "Diazonium Chloride"
        ).next_to(formula3,DOWN)

        item3 = VGroup(formula3,name3).to_edge(RIGHT)
        item3.set_color_by_gradient(RED,YELLOW)
        # elements = self.show_index(formula[0])
        # self.add(elements)
        
        self.play(FadeInFromDown(item1[1]),Write(item1[0]))
        self.play(FadeInFromDown(item2[1]),Write(item2[0]))
        self.play(FadeInFromDown(item3[1]),Write(item3[0]))
        
        self.wait(5)


# class Compounds(Scene):
#     def con