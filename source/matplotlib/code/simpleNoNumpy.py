# Florian Fasmeyer 23.03.2017
"""De la statistique fait rapidement :-)."""
import matplotlib.pyplot as plt

centreClasse = [44, 46, 48, 50, 52, 54, 56]
effectifs = [2, 3, 7, 11, 8, 6, 3]

x = centreClasse
y = effectifs
plt.bar(x, y, align='center', facecolor='green', alpha=0.75)  # histograme
plt.plot(x, y, 'r--', linewidth=1)

plt.show()
