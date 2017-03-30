"""Exemple d'opérations sur les graphes avec NetworkX."""

import NetworkX as nwx

G1 = nwx.Graph()
G1.add_nodes_from([1, 2, 3])
G2 = nwx.Graph()
G1.add_nodes_from([4, 5, 6])

# operations classiques sur les graphes :

# FIXME: nb = nwx.subgraph(G1, nbunch)
# induit un subgraphe de G en noeuds d'un nBrunch
G3 = nwx.union(G1, G2)  # union de deux graphes
G3 = nwx.disjoint_union(G1, G2)  # union sans doublure
G3 = nwx.cartesian_product(G1, G2)  # produit cartésien
G3 = nwx.compose(G1, G2)
# combine les graphes en détectant les mêmes noeuds
G3 = nwx.complement(G1)  # complements de G1
G3 = nwx.create_empty_copy(G1)  # crée une copie vide de G1
G3 = nwx.convert_to_directed(G1)  # convertis un graphe dirigé
G1 = nwx.convert_to_undirected(G3)  # convertis un graphe dirigé

# création de graphe classique prédéfinis

K_5 = nwx.complete_graph(5)
K_3_5 = nwx.complete_bipartite_graph(3, 5)
barbell = nwx.barbell_graph(10, 10)
lollipop = nwx.lollipop_graph(10, 20)

# untilisation des générateurs de graphes stockastiques

er = nwx.erdos_renyi_graph(100, 0.15)
ws = nwx.watts_strogatz_graph(30, 3, 0.1)
ba = nwx.barabasi_albert_graph(100, 5)
red = nwx.random_lobster(100, 0.9, 0.9)

# enregistrement d'un graphe dans un fichier

nwx.write_gml(red, "path.to.file")
mygraph = nwx.read_gml("path.to.file")

# code pris sur :
# https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html
