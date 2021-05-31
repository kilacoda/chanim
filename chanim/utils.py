from enum import Enum

__all__ = ["Arrows"]


class Arrows(Enum):
    """
    An enum of chemfig-recognised arrow types.
    See p. 49 of http://ctan.imsc.res.in/macros/generic/chemfig/chemfig-en.pdf for
    visual examples.
    """

    forward = "->"
    backward = "<-"
    eq = "<=>"
    eq_fw = "<->>"
    eq_bw = "<<->"
    double = "<->"
    space = "0"
    split = "-U"
