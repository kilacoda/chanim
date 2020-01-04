from chanimlib.imports import *

class ReactionTest(Scene):
    CONFIG = {}
    def construct(self):
        ch4 = "CH_4"
        cl2 = "Cl_2"
        ch3cl = "CH_3Cl"
        hcl = "HCl"
        react1 = Reaction("forward","$h\\nu$","",reactants = [ch4,cl2],products=[ch3cl,hcl])
        name1 = Text("Haloalkane Substitution").next_to(react1,DOWN)
        
        ha_subs = VGroup(
            react1.set_color_by_gradient(BLUE,GREEN),
            name1.set_color_by_gradient(BLUE, GREEN)
        ) 
        self.play(Write(react1))
        self.play(FadeInFromDown(name1))
        self.wait(2)


        self.play(ha_subs.move_to, 4*UL,buff=1.5)

        h2 = "H_2"
        o2 = "O_2"
        h2o = "H_2O"

        react2 = Reaction("forward","dil. \\chemfig{H_2SO_4}","",[h2,o2],[h2o])

        self.play(Write(react2))
        self.wait(5)


class OnlyArrow(Scene):
    CONFIG = {}
    def construct(self):
        bdc = ""
        arrow = ChemArrow(length=2)

class FriedelCraftsAlkylation(Scene):
    def construct(self):
        chlorobenzene = "*6(-=-=(-Cl)-=)"
        two_chloro_acetophenone = "*6(-=-(-Cl)=(-COCH_3)-=)"

        reaction = Reaction(
            [chlorobenzene],
            [two_chloro_acetophenone],
            arrow_align_params = ".-30--.210",
            arrow_length=4,
            arrow_text_up="\\chemfig{CH_3COCl}/anhyd. \\chemfig{AlCl_3}",
            arrow_text_down="Friedel-Crafts Alkylation",
            debug="false"
        ).set_color_by_gradient(ORANGE,BLUE).scale(0.6)

        self.play(Write(reaction))
        self.wait(3)

class Wurtz(Scene):
    def construct(self):
        heading = TextMobject("Wurtz Reaction:").to_corner(UL).set_color_by_gradient(GREEN,RED)

        di_haloalkane = ChemObject("2R-X")
        haloalkane = ChemObject("R-X")

        di_sodium = ChemObject("2Na")
        
        arrow = ChemArrow(length=2,
                          text_up="dry ether"
                          ).shift(0.5*UP)

        longer_haloalkane = ChemObject("R-R")
        
        di_sodium_halide = ChemObject("2NaX")
        
        plus1 = TexMobject("+")
        plus2 = TexMobject("+")

        equation = VGroup(
            di_haloalkane,
            plus1,
            di_sodium,
            arrow,
            longer_haloalkane,
            plus2,
            di_sodium_halide
        ).set_color_by_gradient(BLUE,ORANGE).arrange(RIGHT)

        self.play(Write(heading))
        
        self.wait()

        self.play( Write(equation[0:4]) )
        
        self.wait(2)
        
        self.play(ReplacementTransform(di_sodium.copy(),di_sodium_halide,path_arc=np.pi),
                  ReplacementTransform(di_haloalkane.copy(),longer_haloalkane),
                  Write(equation[5])
                  )
        # self.play(Write(equation[4:6]))

        self.wait(4)




