"""Exemple de synchronisation."""
from multiprocessing import Lock, Process


def f(l, i):
    """Fonction qui acquire le lock, affiche hello i, puis relâche le lock."""
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()


if __name__ == '__main__':

    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()
