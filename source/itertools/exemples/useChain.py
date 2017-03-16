#itertools 
# Chain, slice, ...
# Source : https://www.youtube.com/watch?v=xK7E2YmjyAc

#import de la librairie
from itertools import *

a = [0, 1, 2, 3, 4];
b = ["zero", "un", "deux", "trois", "quatre"];
c = ["a", "b", "c", "d"]

#CHAIN()
#permet de concaténer différent list ensemble
#ici le générateur va afficher les éléments un à un
for i in chain(a, b, c):
    print(i);

#Si l'on veut afficher notre liste d'un coup il suffit d'appeler la méhode
#list(chain(...)) qui va nous retourner en une seul fois la liste
print(list(chain(a, b, c)));
#on peut aussi selectionner des ranges
#par exemple le premier élément de chaque liste
print(list(chain(a[:1], b[:1], c[:1])));
#ou les deux premier element
print(list(chain(a[0:2], b[0:2], c[0:2])));
