"""Dessine cos(x) entre 0 et 2 PI."""
import matplotlib.pyplot as plt
import numpy as np

# [0, 0.1, 0.2, ..., pi*2)
xs = np.arange(0, 2 * np.pi, 0.1)
# calcule chaque y pour chaque x dans xs.
ys = np.cos(xs)
# dessine
plt.plot(xs, ys)

# affiche le graphe
plt.show()
