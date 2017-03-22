"""Exemple de mémoire partagé."""
from multiprocessing import Array, Process, Value


def f(n, a):
    """Fonction qui assigne n, rend negatif les valeurs de a[]."""
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]


if __name__ == '__main__':

    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
