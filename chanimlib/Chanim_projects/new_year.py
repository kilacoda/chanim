from chanimlib.imports import *

class HappyNewYear(Scene):
    CONFIG = {}
    def construct(self):
        twenty_nineteen = ChemObject("2019")
        arrow = ChemArrow(length=3,text_up="Happy New Year")
        twenty_twenty = ChemObject("2020")

        equation = VGroup(
            twenty_nineteen,
            arrow,
            twenty_twenty
        ).arrange(RIGHT).set_color_by_gradient(BLUE,GREEN)

        self.play(Write(equation))
        self.wait(3)