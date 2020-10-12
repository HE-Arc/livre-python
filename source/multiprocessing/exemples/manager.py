"""Exemple de la classe Manager."""
from multiprocessing import Manager, Process


def task(payload, lst):
    """Associe 3 valeurs à leurs clé et inverse l'ordre de lst[]."""
    payload[1] = '1'
    payload['2'] = 2
    payload[0.25] = None
    lst.reverse()


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        e = manager.list(range(10))

        p = Process(target=task, args=(d, e))
        p.start()
        p.join()

        print(d)
        print(e)
