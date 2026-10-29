import networkx as nx

G = nx.DiGraph()

G.add_nodes_from(["a", "b", "c"])

G.add_edges_from([
    ("a", "a"),
    ("a", "b"),
    ("b", "b"),
    ("b", "c"),
    ("c", "c")
])

def reflexive(G):
    for u in G.nodes():
        if not G.has_edge(u, u):
            return False
    return True

if reflexive(G):
    print("the graph is reflexive")
else:
    print("the graph is not reflexive")