<<<<<<< HEAD
"""Exemple itertools."""

from itertools import *

a = [0, 1, 2, 3, 4]
b = ["zéro", "un", "deux", "trois", "quatre"]
c = ["a", "b", "c", "d"]
'''function chain()'''
for i in chain(a, b, c):
    print(i)

print(list(chain(a, b, c)))
=======
#itertools 

from itertools import *

a = [0, 1, 2, 3, 4];
b = ["zéro", "un", "deux", "trois", "quatre"];
c = ["a", "b", "c", "d"];

'''function chain()'''
for i in chain(a, b, c):
    print(i);
    
print(list(chain(a, b, c)));
>>>>>>> Ajout du fichier de base UseItertools
