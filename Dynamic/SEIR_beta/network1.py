import networkx as nx
import matplotlib.pyplot as plt

# G = nx.random_graphs.barabasi_albert_graph(200,3)    #生成一个BA无标度网络G
# # res = G.number_of_nodes()
# nums = G.number_of_nodes()  # 足球数据节点 -> 115
# print('总节点数', nums)
#
# nx.draw_networkx(G)
# plt.show()

datasets = []
nodes = []
edge = []
f = open("fb-pages-tvshow.txt")
data = f.read()
rows = data.split('\n')

#生成社交网络图
G=nx.Graph()

for row in rows:
    split_row = row.split('\t')
    name = (int(split_row[0]), int(split_row[1]))
    node_1 = int(split_row[0])
    node_2 = int(split_row[1])
    datasets.append(name)
    nodes.append(node_1)
    nodes.append(node_2)
nodes = list(set(nodes))
print(datasets)
print(nodes)
nums = len(nodes)
print(nums)
# print(datasets)
# print(nodes)
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(datasets)

nx.circular_layout(G)##图的布局方式，圆形
pos=nx.spring_layout(G)

# plt.axis('off')
# plt.title("Facebook")
# plt.show()

nx.draw_networkx(G)
plt.show()