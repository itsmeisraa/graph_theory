import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.DiGraph()
G.add_nodes_from(["a", "b", "c", "d"])
G.add_edges_from([
("b", "a"), ("c", "b"), ("a", "d"), ("b", "c"),
("d", "c")])

def symetric(G):
    for u,v in G.edges():
    
        if not G.has_edge(v,u):
            return False
        else:
            return True

if symetric(G):
    print("the graph is symmetric")
else:
    print("the graph is not symmetric")