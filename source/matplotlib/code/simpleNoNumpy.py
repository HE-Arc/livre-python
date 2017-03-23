# Florian Fasmeyer 23.03.2017
# La statistique :-)

# conseil, regardez le fonctions suivantes en détail.
#plot(*args, **kwargs)
#triplot(*args, **kwargs)
#bar(left, height, width=0.8, bottom=None, hold=None, data=None, **kwargs)
# hist(x, bins=None, range=None, normed=False, weights=None, cumulative=False,
# bottom=None, histtype='bar', align='mid', orientation='vertical',
# rwidth=None, log=False, color=None, label=None, stacked=False,
# hold=None, data=None, **kwargs)


import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

centreClasse = [44, 46, 48, 50, 52, 54, 56]
effectifs = [2, 3, 7, 11, 8, 6, 3]

x = centreClasse
y = effectifs
plt.bar(x, y, align='center', facecolor='green', alpha=0.75)  # histograme
plt.plot(x, y, 'r--', linewidth=1)

plt.show()
