import random
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import network3

list_node = []
for node in list(network3.G):
    s = network3.G.degree(node)
    # if s > 10:
    #     G.remove_node(node)
    list_node.append(s)
print(list_node)
print(network3.G.nodes)
x = max(list_node)
print(x)
degree_node = zip(network3.G.nodes, list_node)
degreeDict = dict((nodes,degree) for nodes,degree in degree_node)
for i in degreeDict.values():
    if i == x:
        print(i)
        h = list(degreeDict.keys())[list(degreeDict.values()).index(i)]
        print(h)
        network3.G.remove_node(h)
        network3.G.add_node(h)

nx.draw_networkx(network3.G)
plt.show()

# α直接变为免疫状态的概率
alter = random.uniform(0,0.2)
# β转化为潜伏人员的概率
beta = random.uniform(0.1,0.3)
# η为传染概率
ita = random.uniform(0.5,0.7)
# δ变为免疫的概率
deta = random.uniform(0,0.6)
# γ为恢复率系数
gamma = random.uniform(0,0.5)

for edge in network3.G.edges:
    network3.G.add_edge(edge[0], edge[1], weight=random.uniform(0, 1))  # 可不可以作为权值 病毒的感染能力
for node in network3.G:
    network3.G.add_node(node, state=0)  # 用state标识状态 state=0 易感 ，state=1 潜伏 ， state=2 感染 ， state=3 免疫

seed = 53  # 选定Arkansas作为传染源
network3.G.nodes[seed]['state'] = 2  # 表示Arkansas是感染的
seed1 = 33
network3.G.nodes[seed1]['state'] = 2

seed2 = 47
network3.G.nodes[seed2]['state'] = 1


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


    plt.plot(x, susceptible, 'm.-', label='易感数')
    plt.plot(x, exposed, 'g.-', label='潜伏数')
    plt.plot(x, infect, 'r.-', label='感染数')
    plt.plot(x, recover, 'b.-', label='治愈数')  # 可以修改颜色、线条风格、图例

    plt.legend(loc='upper right')  # 显示图例

    plt.xticks(range(0, max_iter_num, 5))  # 修改x的刻度
    plt.yticks(range(0, nums, 10))  # 修改y的刻度

    # 添加x，y轴描述信息及标题
    plt.ylabel('数量')
    plt.xlabel('次数')

    # plt.title('对比')

    plt.show()

for i in range(network3.max_iter_num):
    new_exposed = list()  # 新进入潜伏状态的
    new_infect = list()  # 新被感染的
    new_remove = list()  # 新被治愈的
    # t3 = '%s time' % i + ' %s nodes' % len(all_exposed_nodes)
    # print('潜伏节点数：', t3)
    # t1 = '%s time' % i + ' %s nodes' % len(all_infect_nodes)
    # print('当前感染节点数：', t1)  # 当前有多少个节点被感染
    # t2 = '%s time' % i + ' %s nodes' % len(all_remove_nodes)
    # print('治愈节点数：', t2)


    exposed.append(len(all_exposed_nodes))
    infect.append(len(all_infect_nodes))
    recover.append(len(all_remove_nodes))

    # list_node = []
    # for node in list(network3.G):
    #     s = network3.G.degree(node)
    #     # if s > 10:
    #     #     G.remove_node(node)
    #     list_node.append(s)
    # print(list_node)
    #
    # for i in range(len(list_node)):
    #     if list_node[i] > 10:
    #         network3.G.remove_node(i)
    #
    # nx.draw_networkx(network3.G)
    # plt.show()

    # p = random.uniform(0, 1)
    # 感染的机会不止一次
    # 治愈后不会被感染
    for v in all_infect_nodes:
        for nbr in network3.G.neighbors(v):  # v的邻居
            if network3.G.nodes[nbr]['state'] == 2:  # 如果这个邻居节点被感染
                edge_data = network3.G.get_edge_data(v, nbr)  # 得到边的权值
                if gamma < edge_data['weight']:  # 治愈概率
                    network3.G.nodes[nbr]['state'] = 3
                    new_remove.append(nbr)
                    if nbr not in all_remove_nodes:
                        new_remove.append(nbr)
            elif network3.G.nodes[nbr]['state'] == 1:  # 潜伏状态的节点
                edge_data = network3.G.get_edge_data(v, nbr)  # 得到边的权值
                if ita < edge_data['weight']:  # 传染概率
                    network3.G.nodes[nbr]['state'] = 2
                    new_infect.append(nbr)
                elif deta > edge_data['weight']:
                    network3.G.nodes[nbr]['state'] = 3
                    new_remove.append(nbr)
            elif network3.G.nodes[nbr]['state'] == 0:  # 如果这个邻居节点没被感染且没有被治愈
                edge_data = network3.G.get_edge_data(v, nbr)
                if beta < edge_data['weight']:
                    network3.G.nodes[nbr]['state'] = 1
                    new_exposed.append(nbr)
                elif alter > edge_data['weight']:
                    network3.G.nodes[nbr]['state'] = 3
                    new_remove.append(nbr)
                elif ita < edge_data['weight']:  # 传染概率
                    network3.G.nodes[nbr]['state'] = 2
                    new_infect.append(nbr)
                    infect_sum3 = len(new_infect)
                    list_infect1.append(infect_sum3)
                    print(list_infect1)

    for i in all_exposed_nodes:
        p = np.random.rand()
        if p < ita:
            network3.G.nodes[i]['state'] = 2
            new_infect.append(i)
        elif p < deta:
            network3.G.nodes[i]['state'] = 3
            new_remove.append(i)

    for j in all_infect_nodes:
        p = np.random.rand()
        if p < gamma:
            network3.G.nodes[j]['state'] = 3
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


# matplotlib中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']  # aaaaa.py 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）

draw_picture(network3.nums, network3.max_iter_num, exposed, infect, recover)


for i in range(30):
    q = list_exposed[i]
    k = k + q
    list_exposed_sum.append(k)

for i in range(30):
    w = list_infect[i]
    l = l + w
    list_infect_sum.append(l)


plt.plot(list_exposed, 'm.-', label='质疑的人')
plt.plot(list_infect, 'g.-', label='相信的人')


plt.legend(loc='upper right')  # 显示图例


# 添加x，y轴描述信息及标题
plt.ylabel('数量')
plt.xlabel('次数')

# plt.title('对比')

plt.show()

plt.plot(list_exposed_sum, 'm.-', label='质疑的人')
plt.plot(list_infect_sum, 'g.-', label='相信的人')
# plt.plot(list_remove_sum, 'r.-', label='恢复的人')

plt.legend(loc='upper right')  # 显示图例


# 添加x，y轴描述信息及标题
plt.ylabel('数量')
plt.xlabel('次数')


plt.show()