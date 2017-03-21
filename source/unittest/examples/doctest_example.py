"""Exemple simple de test unitaire sur une fonction carré."""


# func:carré
def carré(x):
    """Élève au carré.

    >>> carré(-2)
    4
    >>> carré(0)
    0
    >>> carré(2)
    4
    """
    return x ** 2


# endfunc:carrée


# main
if __name__ == '__main__':
    import doctest

    doctest.testmod()

# endmain
