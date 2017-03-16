from itertools import *

#COUNT(), iSlice()
#fonction très pratique si l'on veut remplir des listes rapidement
# de nombre ou de caractère
#la fonction count() prend deux paramètre un début et un step
#mais ne prend pas de fin donc attention le code ci-dessous créer une boucle infini

##############  BOUCLE INIFINI  #####################
# on comment de zéro et on a avance par pas de 0.4

'''for i in count(0, 0.4):
    print(i);'''

##############  BOUCLE INIFINI   #####################


#pour créer un compteur simple avec un début et une FIN 
#il va nous falloir utiliser la fonction iSlice(count(), start, end, step);
#comme parametre notre fonction count 

#va générer une liste de nombre allant de 0..100 par step de 1
for i in islice(count(), 0, 101, 1):
    print(i);
    
    
    
