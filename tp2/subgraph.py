import networkx as nx
import matplotlib.pyplot as plt 

fig, (ax1, ax2) = plt.subplots(1,2,figsize=(12,5))

G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (2, 4)])

sub_nodes = [1, 2, 4]

sub_G = nx.Graph()  
sub_G.add_nodes_from(sub_nodes)

for u, v in G.edges(sub_nodes):
    if v in sub_nodes:
        sub_G.add_edge(u, v)

print("Nodes of the graph:", G.nodes())  
print("Edges of the graph :", G.edges())  
print("Nodes of the subgraph :", sub_G.nodes())  
print("Edges of the subgraph :", sub_G.edges())  
nx.draw(G,ax =ax1 ,with_labels=True, node_color="skyblue", 
        node_size=800, font_size=12, font_weight="bold", edge_color="gray")
nx.draw(sub_G,ax=ax2 ,with_labels=True, node_color="skyblue", 
        node_size=800, font_size=12, font_weight="bold", edge_color="gray")
plt.show()