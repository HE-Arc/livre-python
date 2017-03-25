"""plot un axe tout mignon."""
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
# de 5 à 10, par saut de 1 [5,6,7,8,9]
axe_x = np.arange(5, 10, 1)
axe_x_mineur = np.arange(5, 10, 0.1)

ax = fig.add_subplot(111)
ax.set_xticks(axe_x)
ax.set_xticks(axe_x_mineur, minor=True)

# pour axe_x, donner var Y
plt.plot(axe_x, [1, 2, 3, 1, 2], "ro")

plt.show()
