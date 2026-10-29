import networkx as nx

#Undirected Graphs
G_undirected = nx.Graph()

G_undirected.add_nodes_from(["a", "b", "c", "d"])
G_undirected.add_edges_from([
    ("b", "a"), ("c", "b"), ("a", "d"),
    ("b", "c"), ("d", "c")
])

def is_complete_undirected(G):
    n = G.number_of_nodes()
    m = G.number_of_edges()
    
    
    return m == n * (n - 1) / 2


# Directed Graph 
G_directed = nx.DiGraph()

G_directed.add_nodes_from(["a", "b", "c", "d"])
G_directed.add_edges_from([
    ("b", "a"), ("c", "b"), ("a", "d"),
    ("b", "c"), ("d", "c")
])

def is_complete_directed(G):
    n = G.number_of_nodes()
    m = G.number_of_edges()
    
    
    return m == n * (n - 1)



print("Undirected Graph:")
if is_complete_undirected(G_undirected):
    print("  The undirected graph is complete.")
else:
    print("  The undirected graph is not complete.")

print("\nDirected Graph:")
if is_complete_directed(G_directed):
    print("  The directed graph is complete.")
else:
    print("  The directed graph is not complete.")