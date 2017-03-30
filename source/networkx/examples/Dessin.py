"""Exemple de dessin d'un graphe de networkX."""

import matplotlib.pyplot as plt
import networkx as nwx

G1 = nwx.Graph()
G1.add_nodes_from([1, 2, 3])

# dessin avec Mathplotlib

nwx.draw(G1)  # on peut aussi essayer avec :
# nx.draw_random(G), nx.draw_circular(G), nx.draw_spectral(G)

plt.show()  # pour afficher ensuite

plt.savefig("path.png")  # pour enregistrer sur un fichier dans un format png

# voir aussi : nx.draw_graphviz(G) et nx.write_dot(G,'file.dot') avec
# PyGraphviz ou pydot

# code pris sur :
# https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html
