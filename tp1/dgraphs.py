import networkx as nx
import matplotlib.pyplot as plt


G1 = nx.DiGraph()

G1.add_nodes_from(["A", "B", "C", "D", "E"])

G1.add_edges_from([
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
    ("D", "E"),
    ("E", "A")
])



G2 = nx.Graph()

G2.add_nodes_from(["1", "2", "3", "4", "5"])

G2.add_edges_from([
    ("1", "2"),
    ("1", "3"),
    ("2", "4"),
    ("3", "4"),
    ("4", "5"),
    ("2", "5")
])



plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)

pos1 = nx.spring_layout(G1, seed=10)

nx.draw(
    G1,
    pos=pos1,
    with_labels=True,
    node_color="lightblue",
    edge_color="royalblue",
    node_size=1800,
    font_size=13,
    font_weight="bold",
    arrows=True,
    arrowsize=20,
    width=2
)

plt.title(
    "Graph 1 — Directed Graph",
    fontsize=15,
    fontweight="bold"
)


plt.subplot(1, 2, 2)

pos2 = nx.circular_layout(G2)

nx.draw(
    G2,
    pos=pos2,
    with_labels=True,
    node_color="lightgreen",
    edge_color="darkgreen",
    node_size=1800,
    font_size=13,
    font_weight="bold",
    width=2
)

plt.title(
    "Graph 2 — Undirected Graph",
    fontsize=15,
    fontweight="bold"
)



plt.suptitle(
    "Comparison of Two Graphs",
    fontsize=20,
    fontweight="bold"
)

plt.tight_layout()

plt.show()