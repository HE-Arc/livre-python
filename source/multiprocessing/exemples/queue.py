"""Exemple de la classe Queue."""
from multiprocessing import Process, Queue


def f(q):
    """Fonction qui envoie 42 None hello."""
    q.put([42, None, 'hello'])


if __name__ == '__main__':

    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()
