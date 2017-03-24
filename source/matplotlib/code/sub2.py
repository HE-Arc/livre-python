# Florian Fasmeyer 22.03.2017
"""exemple subplot cas spécial."""
import matplotlib.pyplot as plt
fig = plt.figure()
# subplot(taille_x, taille_y, position)
fig.add_subplot(1, 2, 1)  # taille(1,2) position(1)
fig.add_subplot(222)
fig.add_subplot(224)

plt.show()
