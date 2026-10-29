import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

G = nx.DiGraph()
G.add_nodes_from([1,2,3,4,5,6,7,8,9,10])
position = nx.circular_layout(G)
nx.draw(G,
        with_labels=True,
        pos=position)
plt.show()