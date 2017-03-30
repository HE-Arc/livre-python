"""Exemple d'instanciation d'un graphe avec NetworkX."""

import networkx as nwx

# création du graphe vide avec un attribu (laisser les parenthèses vides
# si on ne veut psa d'attributs)
G = nwx.Graph(day="Friday")
G.graph['day'] = 'Monday'
G.add_node(1, time='5pm')  # ajout d'un noeud avec un attribu de temps (5pm)
G.add_nodes_from([2, 3])  # ajout de plusieurs noeuds

Ns = nwx.path_graph(10)  # création d'un groupe de noeud
G.add_nodes_from(Ns)  # ajour de chaque noeud dans le graphe

Ng = nwx.path_graph(10)
G.add_node(Ng)  # ajout de Ng comme un noeud de G.

G.add_edge(1, 2)  # création d'un pont dans le graphe
e = (2, 3)
G.add_edge(*e)  # ajout d'un pont déjà existant
G.add_edges_from([(1, 2), (1, 3)])  # ajout de plusieurs edges
G.remove_edge(1, 2)
# suppression du pont (1,2) on peut aussi supprimer des
# groupes de ponts et des noeuds de la même façon avec
# Graph.remove_node(), Graph.remove_nodes_from(),
# Graph.remove_edges_from()

G.clear()  # supprime tout les noeuds et ponts du graphe

G.add_node([1, 2, 3])

G.add_edges_from([(1, 2), (1, 3)])

G.nodes()  # affiche les noeuds

G.edges()  # affiche les ponts

nwx.connected_components(G)  # affiche les groupes de noeuds interconnectés

nwx.degree(G)  # affiche les noeuds avec leurs nombre de connexions

nwx.degree(G).values()  # affiche le nombre de connexion des noeuds

G.node[1]  # affiche le noeud 1

# Directed graphs / graphes dirigés
# ces graphes permettent différences opérations supplémentaires comme :
# DiGraph.out_edges(), DiGraph.in_degree(), DiGraph.predecessors(),
# DiGraph.successors().

DG = nwx.DiGraph()

# ajout de ponts ayant différents poids

DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])

# Multigraph
# Les multigraph permettent d'avoir plusieurs ponts entre deux mêmes points.

MG = nwx.DiGraph()

# ajout de ponts ayant différents poids

MG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])

# code pris sur :
# https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html
