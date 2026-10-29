import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

# Zero n'est pas un diviseur de zéro
M = np.array([
    [0, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1]
])

G = nx.DiGraph(M)

nx.draw(
    G,
    with_labels=True,
    edge_color="red",
    arrows=True
)

plt.show()