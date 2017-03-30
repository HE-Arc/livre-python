"""Utilitaire pour l'index.rst."""

from itertools import count, islice

liste = ["I", "do", "love", "programming", "in", "Python"]
for i in liste:
    print(i)
"""Création d'un itérateur sur une chaine string."""
chaine = "Python"
iterateur = iter(chaine)  # va nous retourner un itérateur sur notre chaine
print(next(iterateur))  # va nous afficher la première lettre de notre string
for i in iterateur:  # va parcourir tous les caractère un à un
    print(i)

# iterateur_perso_begin


class itRevListe:
    """
    Nous retourne un itérateur.

    Ce qui nous permettra de parcourir notre liste de la fin jusqu'au début.
    """

    def __init__(self, liste):
        """On va se mettre à la fin de notre liste."""
        self.liste = liste
        self.position = len(liste)

    def __next__(self):
        """On renvoie l'élément suivant dans notre liste."""
        if self.position == 0:
            raise StopIteration
        self.position -= 1
        return self.liste[self.position]


# iterateur_perso_end
# revlist_begin


class revList(list):
    """
    On va reprendre les méthodes et attributs de la class list.

    Mais nous allons lui changer son itérateur par le notre.
    """

    def __iter__(self):
        """Renvoie notre iterateur perso."""
        return itRevListe(self)


# revlist_end

liste = revList(islice(count(), 0, 10))
for i in liste:
    print(i)


def sayHello(name):
    """SayHello(name)."""
    yield "Bienvenue, "
    yield  # return none
    yield name
