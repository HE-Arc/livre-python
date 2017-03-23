# Florian Fasmeyer 22.03.2017

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
axeX = np.arange(5, 10, 1)      # de 5 à 10, par saut de 1 [5,6,7,8,9]
axeXmineur = np.arange(5, 10, 0.1)

ax = fig.add_subplot(111)
ax.set_xticks(axeX)
ax.set_xticks(axeXmineur, minor=True)

plt.plot(axeX, [1, 2, 3, 1, 2], "ro")       # pour axeX, donner var Y

plt.show()
