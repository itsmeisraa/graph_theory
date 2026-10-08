import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

G.add_nodes_from(["1", "2", "3"])

G.add_edges_from([
    ("1", "2"),
    ("1", "1"),
    ("2", "3")
])

nx.draw(
    G,
    with_labels=True,
    node_color="lightblue",
    edge_color="red",
    node_size=1500,
    font_size=12,
    font_weight="bold",
    arrows=True
)
plt.title("Mon graphe")
plt.show()