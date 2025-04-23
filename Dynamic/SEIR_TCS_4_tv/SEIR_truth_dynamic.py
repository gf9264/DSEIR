import random
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


datasets = []
nodes = []
edge = []
f = open("fb-pages-tvshow.txt")
data = f.read()
rows = data.split('\n')
max_iter_num = 50  # 模拟的次数
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
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(datasets)
nums = G.number_of_nodes()  # 足球数据节点 -> 115
print('总节点数', nums)


nx.draw_networkx(G)
plt.show()

list_node = []
list_node1 = []
truth_node = []     # 所有传播真相运动的节点
for node in list(G):
    s = G.degree(node)
    # if s > 10:
    #     G.remove_node(node)
    list_node.append(s)
    list_node1.append(s)
list_node1.sort()
list_node_1 = list_node1[::-1]
degree_node = zip(G.nodes, list_node)
degreeDict = dict((nodes, degree) for nodes, degree in degree_node)


# α直接变为免疫状态的概率
alter = random.uniform(0, 0.2)
# β转化为潜伏人员的概率
beta = random.uniform(0.1, 0.3)
# η为传染概率
ita = random.uniform(0.5, 0.7)
# δ变为免疫的概率
deta = random.uniform(0, 0.6)
# γ为恢复率系数
gamma = random.uniform(0, 0.5)
# true_p 为相信真相的概率
true_p = random.uniform(0.3, 0.4)

for edge in G.edges:
    G.add_edge(edge[0], edge[1], weight=random.uniform(0, 1))  # 可不可以作为权值 病毒的感染能力
for node in G:
    G.add_node(node, state=0)  # 用state标识状态 state=0 易感 ，state=1 潜伏 ， state=2 感染 ， state=3 免疫

seed = 53  # 选定Arkansas作为传染源
G.nodes[seed]['state'] = 2  # 表示Arkansas是感染的
seed1 = 33
G.nodes[seed1]['state'] = 2

seed2 = 47
G.nodes[seed2]['state'] = 1


all_exposed_nodes = []  # 所有潜伏的节点放在这里
all_exposed_nodes.append(seed2)
list_exposed = []
exposed_sum1 = len(all_exposed_nodes)
list_exposed.append(exposed_sum1)


all_infect_nodes = []  # 所有被感染的节点放在这里
all_infect_nodes.append(seed)
all_infect_nodes.append(seed1)
list_infect = []
infect_sum1 = len(all_infect_nodes)
list_infect.append(infect_sum1)

all_remove_nodes = []  # 所有被治愈的节点放在这里
list_remove = []
exposed = []  # 随着迭代次数的增加的潜伏总人数
infect = []  # 随着迭代次数的增加的感染总人数
recover = []  # 随着迭代次数的增加的治愈总人数



list_infect1 = []
list_exposed_sum = []
list_infect_sum = []
list_remove_sum = []
k = len(all_exposed_nodes)
l = len(all_infect_nodes)
m = len(all_remove_nodes)
def draw_picture(nums, max_iter_num, exposed, infect, recover):
    x = range(max_iter_num)
    susceptible = []
    for i in range(max_iter_num):
        susceptible.append(nums - exposed[i] - infect[i] - recover[i])

    # plt.figure(figsize=(4, 3), dpi=200)  # 图片大小，清晰度

    plt.plot(x, susceptible, 'm.-', label='易感数')
    plt.plot(x, exposed, 'g.-', label='潜伏数')
    plt.plot(x, infect, 'r.-', label='感染数')
    plt.plot(x, recover, 'b.-', label='治愈数')  # 可以修改颜色、线条风格、图例

    plt.legend(loc='upper right')  # 显示图例

    # plt.xticks(range(0, max_iter_num, 5))  # 修改x的刻度
    # plt.yticks(range(0, nums, 10))  # 修改y的刻度

    # 添加x，y轴描述信息及标题
    plt.ylabel('数量')
    plt.xlabel('次数')

    plt.title('DRITCS')

    plt.show()

new_exposed = list()  # 新进入潜伏状态的
new_infect = list()  # 新被感染的
new_remove = list()  # 新被治愈的
n = 200


for i in range(max_iter_num):

    exposed.append(len(all_exposed_nodes))
    infect.append(len(all_infect_nodes))
    recover.append(len(all_remove_nodes))
    if i < 4:
        # 治愈后不会被感染
        for v in all_infect_nodes:
            for nbr in G.neighbors(v):  # v的邻居
                if G.nodes[nbr]['state'] == 2:  # 如果这个邻居节点被感染
                    edge_data = G.get_edge_data(v, nbr)  # 得到边的权值
                    if gamma < edge_data['weight']:  # 治愈概率
                        G.nodes[nbr]['state'] = 3
                        new_remove.append(nbr)
                        if nbr not in all_remove_nodes:
                            new_remove.append(nbr)
                elif G.nodes[nbr]['state'] == 1:  # 潜伏状态的节点
                    edge_data = G.get_edge_data(v, nbr)  # 得到边的权值
                    if ita < edge_data['weight']:  # 传染概率
                        G.nodes[nbr]['state'] = 2
                        new_infect.append(nbr)
                    elif deta > edge_data['weight']:
                        G.nodes[nbr]['state'] = 3
                        new_remove.append(nbr)
                elif G.nodes[nbr]['state'] == 0:  # 如果这个邻居节点没被感染且没有被治愈
                    edge_data = G.get_edge_data(v, nbr)
                    if beta < edge_data['weight']:
                        G.nodes[nbr]['state'] = 1
                        new_exposed.append(nbr)
                    elif alter > edge_data['weight']:
                        G.nodes[nbr]['state'] = 3
                        new_remove.append(nbr)
                    elif ita < edge_data['weight']:  # 传染概率
                        G.nodes[nbr]['state'] = 2
                        new_infect.append(nbr)
    elif i == 4:
        for f in list_node_1[:n]:
            h = list(degreeDict.keys())[list(degreeDict.values()).index(f)]
            # 选择节点度数最大的节点判断其状态，如果是未感染或者是已经痊愈的状态，就将其作为真相运动的传播者
            if G.nodes[h]['state'] == 0 or G.nodes[h]['state'] == 3:
                truth_node.append(h)

            elif G.nodes[h]['state'] == 1:
                G.nodes[h]['state'] = 3
                new_remove.append(h)

            elif G.nodes[h]['state'] == 2:
                G.remove_node(h)
                G.add_node(h)

        truth_node = list(set(truth_node))



        for v in truth_node:
            for nbr in G.neighbors(v):
                if G.nodes[nbr]['state'] == 2:  # 如果这个邻居节点被感染
                    edge_data = G.get_edge_data(v, nbr)  # 得到边的权值
                    if gamma < edge_data['weight']:  # 治愈概率
                        G.nodes[nbr]['state'] = 3
                        new_remove.append(nbr)

                    elif gamma < true_p:
                        G.nodes[nbr]['state'] = 3
                        new_remove.append(nbr)
                        if nbr not in all_remove_nodes:
                            new_remove.append(nbr)

                elif G.nodes[nbr]['state'] == 1:  # 潜伏状态的节点
                    edge_data = G.get_edge_data(v, nbr)
                    if ita > true_p:  # 传染概率
                        G.nodes[nbr]['state'] = 2
                        new_infect.append(nbr)

                    elif ita < true_p:
                        G.nodes[nbr]['state'] = 3
                        new_remove.append(nbr)

                    elif deta > edge_data['weight']:
                        G.nodes[nbr]['state'] = 3
                        new_remove.append(nbr)

                    elif true_p > edge_data['weight']:
                        G.nodes[nbr]['state'] = 3
                        new_remove.append(nbr)

                elif G.nodes[nbr]['state'] == 0:  # 如果这个邻居节点没被感染且没有被治愈
                    edge_data = G.get_edge_data(v, nbr)
                    if beta > true_p:
                        G.nodes[nbr]['state'] = 1
                        new_exposed.append(nbr)

                    elif beta < true_p:
                        G.nodes[nbr]['state'] = 3
                        new_remove.append(nbr)

                    elif alter > edge_data['weight']:
                        G.nodes[nbr]['state'] = 3
                        new_remove.append(nbr)

                    elif true_p > edge_data['weight']:
                        G.nodes[nbr]['state'] = 3
                        new_remove.append(nbr)

                    elif ita > true_p:  # 传染概率
                        G.nodes[nbr]['state'] = 2
                        new_infect.append(nbr)

                    elif ita < true_p:
                        G.nodes[nbr]['state'] = 3
                        new_remove.append(nbr)


        # 感染的机会不止一次
        # 治愈后不会被感染
        for v in all_infect_nodes:
            for nbr in G.neighbors(v):  # v的邻居
                if G.nodes[nbr]['state'] == 2:  # 如果这个邻居节点被感染
                    edge_data = G.get_edge_data(v, nbr)  # 得到边的权值
                    if gamma < edge_data['weight']:  # 治愈概率
                        G.nodes[nbr]['state'] = 3
                        new_remove.append(nbr)
                        if nbr not in all_remove_nodes:
                            new_remove.append(nbr)
                elif G.nodes[nbr]['state'] == 1:  # 潜伏状态的节点
                    edge_data = G.get_edge_data(v, nbr)  # 得到边的权值
                    if ita < edge_data['weight']:  # 传染概率
                        G.nodes[nbr]['state'] = 2
                        new_infect.append(nbr)
                    elif deta > edge_data['weight']:
                        G.nodes[nbr]['state'] = 3
                        new_remove.append(nbr)
                elif G.nodes[nbr]['state'] == 0:  # 如果这个邻居节点没被感染且没有被治愈
                    edge_data = G.get_edge_data(v, nbr)
                    if beta < edge_data['weight']:
                        G.nodes[nbr]['state'] = 1
                        new_exposed.append(nbr)
                    elif alter > edge_data['weight']:
                        G.nodes[nbr]['state'] = 3
                        new_remove.append(nbr)
                    elif ita < edge_data['weight']:  # 传染概率
                        G.nodes[nbr]['state'] = 2
                        new_infect.append(nbr)


    for i in all_exposed_nodes:
        p = np.random.rand()
        if p < ita:
            G.nodes[i]['state'] = 2
            new_infect.append(i)
        elif p < deta:
            G.nodes[i]['state'] = 3
            new_remove.append(i)

    for j in all_infect_nodes:
        p = np.random.rand()
        if p < gamma:
            G.nodes[j]['state'] = 3
            new_remove.append(j)

    for i in new_remove:
        if i in new_exposed:
            new_exposed.remove(i)
        if i in all_exposed_nodes:
            all_exposed_nodes.remove(i)
        if i in new_infect:
            new_infect.remove(i)
        if i in all_infect_nodes:
            all_infect_nodes.remove(i)
    for i in new_infect:
        if i in new_exposed:
            new_exposed.remove(i)
        if i in all_exposed_nodes:
            all_exposed_nodes.remove(i)

    all_exposed_nodes.extend(new_exposed)
    all_infect_nodes.extend(new_infect)
    all_remove_nodes.extend(new_remove)

    exposed_sum2 = len(new_exposed)
    list_exposed.append(exposed_sum2)
    infect_sum2 = len(new_infect)
    list_infect.append(infect_sum2)
    remove_sum = len(new_remove)
    list_remove.append(remove_sum)

    all_exposed_nodes = list(set(all_exposed_nodes))
    all_infect_nodes = list(set(all_infect_nodes))  # 去重
    all_remove_nodes = list(set(all_remove_nodes))
    truth_node = list(set(truth_node))

# matplotlib中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']  # aaaaa.py 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）

draw_picture(nums, max_iter_num, exposed, infect, recover)

# print(truth_node)

for i in range(max_iter_num):
    q = exposed[i]
    k = k + q
    list_exposed_sum.append(k)

for i in range(max_iter_num):
    w = infect[i]
    l = l + w
    list_infect_sum.append(l)


# plt.plot(list_exposed, 'm.-', label='质疑的人')
# plt.plot(list_infect, 'g.-', label='相信的人')
# plt.plot(exposed, 'y.-', label='质疑的人')
# plt.plot(infect, 'r.-', label='相信的人')
#
# plt.legend(loc='upper right')  # 显示图例
#
#
# # 添加x，y轴描述信息及标题
# plt.ylabel('数量')
# plt.xlabel('次数')
#
# # plt.title('对比')
#
# plt.show()
#
# plt.plot(list_exposed_sum, 'm.-', label='质疑的人')
# plt.plot(list_infect_sum, 'g.-', label='相信的人')
# # plt.plot(list_remove_sum, 'r.-', label='恢复的人')
#
# plt.legend(loc='upper right')  # 显示图例
#
#
# # 添加x，y轴描述信息及标题
# plt.ylabel('数量')
# plt.xlabel('次数')
#
# # plt.title('对比')
#
# plt.show()