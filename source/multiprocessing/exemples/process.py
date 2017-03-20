"""Fichier test processus."""
from multiprocessing import os
import Process


def info(title):
    """Fonction info."""
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    """Fonction demo."""
    info('function f')
    print('hello', name)


if __name__ == '__main__':

    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
