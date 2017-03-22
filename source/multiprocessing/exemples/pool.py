"""Exemple de la classe Pool."""
from multiprocessing import Pool


def f(x):
    """Fonction qui retourne le carré de la valeur passé en argument."""
    return x*x


if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
