"""Exemple de la classe Manager."""
from multiprocessing import Manager, Process


def f(d, l):
    """Fonction qui associe 3 valeurs à leurs clé et inverse l'ordre de l[]."""
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        e = manager.list(range(10))

        p = Process(target=f, args=(d, e))
        p.start()
        p.join()

        print(d)
        print(e)
