import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

graph = {
    1: [2, 3, 4],
    2: [1, 3, 4],
    3: [1, 2, 4],
    4: [1, 2, 3]
}

G = nx.DiGraph(graph)

nx.draw(
    G,
    with_labels=True,
    edge_color="red",
    arrows=True,
    arrowsize=20,
    node_color="lightblue",
    node_size=1000
)

plt.show()