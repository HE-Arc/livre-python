"""Fichier test processus."""
from multiprocessing import os
import Process


def info(title, name):
    """Affiche les informations liées au processus, id et parent id."""
    print(title)
    print('hello', name)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


if __name__ == '__main__':

    p = Process(target=info, args=('main line', 'bob', ))
    p.start()
    p.join()
