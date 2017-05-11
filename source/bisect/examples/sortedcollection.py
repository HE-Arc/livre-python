"""
Exemple d'une collection triée.

Inspirée par: https://code.activestate.com/recipes/577197-sortedcollection/
"""
# start
from bisect import bisect_left, insort
from collections.abc import MutableSequence


class SortedCollection(MutableSequence):
    """Collection triée.

    >>> sc = SortedCollection()
    >>> sc.append(2)
    >>> sc.append(1)
    >>> sc
    [1, 2]
    >>> 2 in sc
    True
    >>> 3 in sc
    False
    >>> tuple(sc)
    (1, 2)
    >>> sc.reverse()  # reverse does nothing.
    >>> sc
    [1, 2]
    >>> del sc[1]
    >>> sc[0] = 3
    >>> sc
    [3]
    """

    def __init__(self):
        """Initialise la collection triée."""
        self._col = []

    def __repr__(self):
        """S'affiche comme une list."""
        return repr(self._col)

    def __contains__(self, value):
        """Contient la valeur cherchée."""
        try:
            self.index(value)
        except ValueError:
            return False
        return True

    def __iter__(self):
        """Retourne un itérateur sur la liste."""
        return iter(self._col)

    def __len__(self):
        """Retourne la taille de la collection."""
        return len(self._col)

    def __getitem__(self, index):
        """Obtient un élément selon sa position."""
        return self._col[index]

    def __setitem__(self, index, value):
        """Modifie l'élément à l'index donnée.

        Équivalent à supprimer un élément et en ajouter un (ailleurs).
        """
        del self[index]
        self.insert(index, value)

    def __delitem__(self, index):
        """Supprime l'élément à l'indice donné."""
        del self._col[index]

    def insert(self, index, value):
        """Ajoute la valeur à sa place.

        Indépendamment de la position donnée dans ``index``.
        """
        insort(self._col, value)

    def index(self, value):
        """Retourne la position dans la liste."""
        i = bisect_left(self._col, value)
        if i < len(self) and self[i] == value:
            return i
        raise ValueError

    def reverse(self):
        """Inverse ne fait rien."""
        pass  # end


# Exécute les doctests.
if __name__ == "__main__":
    import doctest
    doctest.testmod()
