import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.DiGraph()
G.add_nodes_from(["a", "b", "c", "d"])
G.add_edges_from([
("b", "a"), ("c", "b"), ("a", "d"), ("b", "c"),
("d", "c")])
#Choose an edge u → v.
#Choose another edge x → w.
#Check whether v == x, meaning the edges connect into a path.
#If they do, check whether u → w exists.
#If that direct edge is missing, return False.
#If all pairs pass, return True.
def transitive(G):
    for u, v in G.edges():
        for x, w in G.edges():
            if v == x and not G.has_edge(u, w):
                return False
    return True

if transitive(G):
    print("the graph is  transitive")
else:
    print("the graph is not transitive")