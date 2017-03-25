"""
Fréquences cumulées et médiane.

# Made by Florian Fasmeyer 27.02.2017
"""
import matplotlib.pyplot as plt
import numpy as np


def cf(ni, n):
    """Cumule une liste de fréquences par addition."""
    cumulFreq = 0
    for i in ni:
        cumulFreq += (i / n)
        yield cumulFreq


def f(ni, n):
    """Prend une liste d'occurence et calcule la fréquence."""
    for i in ni:
        yield i / n


# Variables
ni = (4, 21, 104, 163, 121, 57, 22, 10)
i = len(ni)
n = sum(ni)
cash = np.arange(27, 51, 3)
frequence = list(f(ni, n))
frequence_cumule = list(cf(ni, n))

major_ticksX = np.arange(24, 51, 3)
major_ticksY = np.arange(0, 163, 10)
major_ticksX2 = np.arange(27, 51, 3)
major_ticksY2 = np.arange(0, 1.1, 0.1)

# Mod
mod = (cash[2] + (cash[3] - cash[2]) * (ni[3] - ni[2]) /
       ((ni[3] - ni[2]) + (ni[3] - ni[4])))

# Médiane
ccf = list(cf(ni, n))
med = (0.5 - ccf[2]) * (cash[3] - cash[2]) / (ccf[3] - ccf[2]) + cash[2]
print(f"médiane = {med:.3f}")
print(f"mod     = {mod:.3f}")

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
plt.plot(np.arange(27, 51, 3), ccf)
plt.plot(np.arange(27, 51, 3), ccf, "ro")

a = np.empty(8)
a.fill(0.5)
plt.plot(np.arange(27, 51, 3), a)
a.fill(0.75)
plt.plot(np.arange(27, 51, 3), a)
a.fill(0.25)
plt.plot(np.arange(27, 51, 3), a)

plt.show()
