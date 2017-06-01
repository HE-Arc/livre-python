"""Module d'exemple d'une memoryview."""


# mybuf = ...  un grand buffer de bytes.
mv_mybuf = memoryview(mybuf)  # une memoryview de mybuf.
func(mv_mybuf[:len(mv_mybuf)//2])
# passe la première moitié de mybuf dans func comme une "sous-view"
# créé par le découpage de la memoryview.
# Aucune copie n'est faite ici!
