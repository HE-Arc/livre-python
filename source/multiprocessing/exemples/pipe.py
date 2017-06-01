"""Exemple de la classe Pipe."""
from multiprocessing import Pipe, Process


def f(conn):
    """Fonction qui envoie 42 None hello."""
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == '__main__':

    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()
