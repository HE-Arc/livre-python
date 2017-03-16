from itertools import *
    
   
#compress est une fonction utile si l'on veut juste retourner certain
#éléments d'une liste avec un tableau qui contiendra true (=1) false(=0)
#Avec l'exemple suivant nous allons utiliser un tableau "binaire" qui va contenir
#les éléments que l'on souhaite voir aparaitre. 

a = ["Johnny", "Toto", "Tata", "Roger", "Steve"];
filter_binaire = [1, 0, 1, 0, 1];

for i in compress(a, filter_binaire):
    print(i);
    #va nous sortir seulement Johnny, tata et tata

#on peut très bien utiliser la fonction list pour qu'elle nous retourner
#une liste que l'on pourra sauver dans une variable et peut la réutiliser plus tard
b = list(compress(a, filter_binaire));
print(b);
