import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

d = {
    0:{1:{'weight' : 0.4}
       ,3 :{'weight':0.1},
       2 :{'weight':0.5}
       },
       1:{2:{'weight' : 0.7}
          },
        2:{3:{'weight' : 0.9}
           }
        }
G = nx.DiGraph(d)
pos = nx.spring_layout(G)
nx.draw(
G,
with_labels=True,
pos = pos
)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()
#2
p = nx.get_edge_attributes(G, 'weight' )
print(p)
#3
for edge in p:
    print("Edge:", edge, "Weight:", p[edge])