"""Exemple calculs mathématiques en utilisant des nombres complexes."""
from cmath import phase

a = complex(2, 3)
z = complex(4, 3)

print(a+z)
print(a-z)
print(a*z)
print(a/z)

"""Affichage de la partie réelle et imaginaire de z."""
print(z.real)
print(z.imag)

"""Affichage de la du conjugé z."""
print(z.conjugate())

"""Affichage du module et de l'argument de z."""
print(abs(z))
print(phase(z))
