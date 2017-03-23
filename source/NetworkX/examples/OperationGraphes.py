"""Opération sur les graphes avec NetworkX"""

import NetworkX as nwx

G1 = nwx.Graph()
G1.add_nodes_from([1, 2, 3])
G2 = nwx.Graph()
G1.add_nodes_from([4, 5, 6])

# operations classiques sur les graphes :

nb = subgraph(G1, nbunch)  # induit un subgraphe de G en noeuds d'un nBrunch
G3 = union(G1, G2)  # union de deux graphes
G3 = disjoint_union(G1, G2)  # union sans doublure
G3 = cartesian_product(G1, G2)  # produit cartésien
G3 = compose(G1, G2)  # combine les graphes en détectant les mêmes noeuds
G3 = complement(G1)  # complements de G1
G3 = create_empty_copy(G1)  # crée une copie vide de G1
G3 = convert_to_directed(G1)  # convertis un graphe dirigé
G1 = convert_to_undirected(G3)  # convertis un graphe dirigé

# création de graphe classique prédéfinis

K_5 = nx.complete_graph(5)
K_3_5 = nx.complete_bipartite_graph(3, 5)
barbell = nx.barbell_graph(10, 10)
lollipop = nx.lollipop_graph(10, 20)

# untilisation des générateurs de graphes stockastiques

er = nx.erdos_renyi_graph(100, 0.15)
ws = nx.watts_strogatz_graph(30, 3, 0.1)
ba = nx.barabasi_albert_graph(100, 5)
red = nx.random_lobster(100, 0.9, 0.9)

# enregistrement d'un graphe dans un fichier

nx.write_gml(red, "path.to.file")
mygraph = nx.read_gml("path.to.file")

# code pris sur :
# https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html
