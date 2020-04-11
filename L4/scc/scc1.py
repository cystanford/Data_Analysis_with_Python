# 计算强连通图
import networkx as nx
import matplotlib.pyplot as plt

# 创建有向图
G = nx.DiGraph() 
# 在图中添加点
G.add_nodes_from(['a','b','c','d','e','f','g','h'])
G.add_edges_from([('a','b'),('b','c'),('b','c'),('c','d'),('d','c'),\
				 ('e','a'),('b','e'),('b','f'),('e','f'),('f','g'),('g','f'),\
				 ('c','g'),('h','g'),('d','h'),('h','d')])

# 有向图可视化
layout = nx.spring_layout(G)
nx.draw(G, pos=layout, with_labels=True, hold=False)
plt.show()
for c in nx.strongly_connected_components(G):
    print(c)


