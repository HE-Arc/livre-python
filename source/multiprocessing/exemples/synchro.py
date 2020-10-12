"""Exemple de synchronisation."""
from multiprocessing import Lock, Process


def task(lock, i):
    """Acquire le lock, affiche hello i, puis relâche le lock."""
    lock.acquire()
    try:
        print('hello world', i)
    finally:
        lock.release()


def main():
    """Main program."""
    lock = Lock()

    for num in range(10):
        Process(target=task, args=(lock, num)).start()


if __name__ == '__main__':
    main()
