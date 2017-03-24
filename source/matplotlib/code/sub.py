# source: stackoverflow
"""exemple subplot."""
import matplotlib.pyplot as plt
fig = plt.figure()

# subplot(taille_x, taille_y, position)
fig.add_subplot(221)  # haut gauche
fig.add_subplot(222)  # haut droite
fig.add_subplot(223)  # bas gauche
fig.add_subplot(224)  # bas droit

plt.show()
