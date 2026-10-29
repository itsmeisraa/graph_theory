import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.DiGraph()
G.add_nodes_from(["a", "b", "c", "d"])
G.add_edges_from([
("b", "a"), ("c", "b"), ("a", "d"), ("b", "c"),
("d", "c")])
G_complement = nx.complement(G)
print(G_complement.edges())
nx.draw(G_complement, with_labels=True, node_color="pink")
plt.show()