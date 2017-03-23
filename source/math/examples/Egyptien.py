from fractions import Fraction
from math import *


def egypt(f):
    e = int(f)
    f -= e
    liste = [e]
    while(f.numerator > 1):
        e = Fraction(1, int(ceil(1/f)))
        liste.append(e)
        f -= e
    liste.append(f)
    return liste


a = Fraction(21, 13)

print(egypt(a))
