# Made by Florian Fasmeyer 27.02.2017
# Fréquences cumulés & médiane

import numpy as np
import matplotlib.pyplot as plt


def cf(ni, n):  # fréquence cumulée
    r = []
    cumulFreq = 0
    for i in ni:
        cumulFreq = (i / n) + cumulFreq
        r.append(cumulFreq)
    return(r)


def f(ni, n):  # fréquence
    r = []
    freq = 0
    for i in ni:
        freq = (i / n)
        r.append(freq)
    return(r)


# Variables
ni = ([4, 21, 104, 163, 121, 57, 22, 10])
i = float(len(ni))
n = sum(ni)
cash = np.arange(27, 51, 3)
frequence = f(ni, n)
frequenceCumule = cf(ni, n)

major_ticksX = np.arange(24, 51, 3)
major_ticksY = np.arange(0, 163, 10)
major_ticksX2 = np.arange(27, 51, 3)
major_ticksY2 = np.arange(0, 1.1, 0.1)

# Mod
mod = cash[2] + (cash[3] - cash[2]) * (ni[3] - ni[2]) / \
    ((ni[3] - ni[2]) + (ni[3] - ni[4]))

# Médiane
ccf = cf(ni, n)
med = (0.5 - ccf[2]) * (cash[3] - cash[2]) / (ccf[3] - ccf[2]) + cash[2]
print("médianne = {:f}".format(med))
print("mod = {:f}".format(mod))

# Plot Graphes
fig = plt.figure()

# fig1
ax = fig.add_subplot(1, 2, 1)
ax.set_xticks(major_ticksX)
ax.set_yticks(major_ticksY)
plt.subplot(121)
plt.grid(True)
a = np.empty(8)
bins = np.arange(24, 51, 3)
plt.hist(np.arange(24, 48, 3), bins, weights=ni)

# fig2
ax = fig.add_subplot(1, 2, 2)
ax.set_xticks(major_ticksX2)
ax.set_yticks(major_ticksY2)
plt.subplot(122)
plt.grid(True)
plt.plot(np.arange(27, 51, 3), cf(ni, n))
plt.plot(np.arange(27, 51, 3), cf(ni, n), "ro")

a = np.empty(8)
a.fill(0.5)
plt.plot(np.arange(27, 51, 3), a)
a.fill(0.75)
plt.plot(np.arange(27, 51, 3), a)
a.fill(0.25)
plt.plot(np.arange(27, 51, 3), a)


plt.show()
