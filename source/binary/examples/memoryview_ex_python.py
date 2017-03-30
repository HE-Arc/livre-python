"""Module d'exemple d'une memoryview."""

with open('../../_static/json.png', 'rb') as f:
    mybuf = f.read()


def func(data):
    """Traite des données..."""


mv_mybuf = memoryview(mybuf)  # une memoryview de mybuf.
func(mv_mybuf[:len(mv_mybuf) // 2])
# passe la première moitié de mybuf dans func comme une "sous-view"
# créé par le découpage de la memoryview.
# Aucune copie n'est faite ici!
