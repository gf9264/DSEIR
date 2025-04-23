import random
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import network
'''
1 易感人群（Susceptible）：指未得病者，但缺乏免疫能力，与感病者接触后容易受到感染。
2 潜伏人群（Exposed)：指接收消息对消息持有怀疑或者离线暂时不传播谣言
2 感染人群（Infective）：指染上传染病的人，他可以传播给易感人群。
3 移除人群（Removed）：被移出系统的人。因病愈（具有免疫力）或死亡的人。这部分人不再参与感染和被感染过程。
N(t) = S(t) + E(t) + I(t) + R(t)

S(t+1) = - βS(t) - αS(t)
E(t+1) = βS(t) - ηE(t) - δE(t)
I(t+1) = ηE(t) - γI(t)
R(t+1) = αS(t) + δE(t) + γI(t)
'''
max_iter_num = 50  # 模拟的次数
# G = nx.random_graphs.barabasi_albert_graph(200,3)    #生成一个BA无标度网络G
# # res = G.number_of_nodes()
# nodes = G.number_of_nodes()  # 足球数据节点 -> 115
# print('总节点数', nodes)
#
# nx.draw_networkx(G)
# plt.show()
# α直接变为免疫状态的概率
alter3 = random.uniform(0.4, 0.6)
# β转化为潜伏人员的概率
beta = random.uniform(0.1,0.3)
# η为传染概率
ita = random.uniform(0.5,0.7)
# δ变为免疫的概率
deta = random.uniform(0,0.6)
# γ为恢复率系数
gamma = random.uniform(0,0.5)

for edge in network.G.edges:
    network.G.add_edge(edge[0], edge[1], weight=random.uniform(0, 1))  # 可不可以作为权值 病毒的感染能力
for node in network.G:
    network.G.add_node(node, state=0)  # 用state标识状态 state=0 易感 ，state=1 潜伏 ， state=2 感染 ， state=3 免疫

seed = 53  # 选定Arkansas作为传染源
network.G.nodes[seed]['state'] = 2  # 表示Arkansas是感染的
seed1 = 33
network.G.nodes[seed1]['state'] = 2

seed2 = 47
network.G.nodes[seed2]['state'] = 1


all_exposed_nodes = []  # 所有潜伏的节点放在这里
all_exposed_nodes.append(seed2)

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

list_infect_sum = []
l = len(all_infect_nodes)

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

    plt.xticks(range(0, max_iter_num, 5))  # 修改x的刻度
    plt.yticks(range(0, nums, 10))  # 修改y的刻度

    # 添加x，y轴描述信息及标题
    plt.ylabel('数量')
    plt.xlabel('次数')

    # plt.title('对比')

    plt.show()

for i in range(max_iter_num):
    new_exposed = list()  # 新进入潜伏状态的
    new_infect = list()  # 新被感染的
    new_remove = list()  # 新被治愈的


    exposed.append(len(all_exposed_nodes))
    infect.append(len(all_infect_nodes))
    recover.append(len(all_remove_nodes))


    # p = random.uniform(0, 1)
    # 感染的机会不止一次
    # 治愈后不会被感染
    for v in all_infect_nodes:
        for nbr in network.G.neighbors(v):  # v的邻居
            if network.G.nodes[nbr]['state'] == 2:  # 如果这个邻居节点被感染
                edge_data = network.G.get_edge_data(v, nbr)  # 得到边的权值
                if gamma < edge_data['weight']:  # 治愈概率
                    network.G.nodes[nbr]['state'] = 3
                    new_remove.append(nbr)
                    if nbr not in all_remove_nodes:
                        new_remove.append(nbr)
            elif network.G.nodes[nbr]['state'] == 1:  # 潜伏状态的节点
                edge_data = network.G.get_edge_data(v, nbr)  # 得到边的权值
                if ita < edge_data['weight']:  # 传染概率
                    network.G.nodes[nbr]['state'] = 2
                    new_infect.append(nbr)
                elif deta > edge_data['weight']:
                    network.G.nodes[nbr]['state'] = 3
                    new_remove.append(nbr)
            elif network.G.nodes[nbr]['state'] == 0:  # 如果这个邻居节点没被感染且没有被治愈
                edge_data = network.G.get_edge_data(v, nbr)
                if beta < edge_data['weight']:
                    network.G.nodes[nbr]['state'] = 1
                    new_exposed.append(nbr)
                elif alter3 > edge_data['weight']:
                    network.G.nodes[nbr]['state'] = 3
                    new_remove.append(nbr)
                elif ita < edge_data['weight']:  # 传染概率
                    network.G.nodes[nbr]['state'] = 2
                    new_infect.append(nbr)

    for i in all_exposed_nodes:
        p = np.random.rand()
        if p < ita:
            network.G.nodes[i]['state'] = 2
            new_infect.append(i)
        elif p < deta:
            network.G.nodes[i]['state'] = 3
            new_remove.append(i)

    for j in all_infect_nodes:
        p = np.random.rand()
        if p < gamma:
            network.G.nodes[j]['state'] = 3
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

    infect_sum2 = len(new_infect)
    list_infect.append(infect_sum2)

    all_exposed_nodes = list(set(all_exposed_nodes))
    all_infect_nodes = list(set(all_infect_nodes))  # 去重
    all_remove_nodes = list(set(all_remove_nodes))

for i in range(30):
    w = list_infect[i]
    l = l + w
    list_infect_sum.append(l)

# matplotlib中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']  # aaaaa.py 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）

draw_picture(network.nums, max_iter_num, exposed, infect, recover)


# plt.plot(list_infect_sum, 'b.-', label='感染数')  # 可以修改颜色、线条风格、图例
#
# plt.legend(loc='upper right')  # 显示图例
#
#
#
# # 添加x，y轴描述信息及标题
# plt.ylabel('数量')
# plt.xlabel('次数')
#
# # plt.title('对比')
#
# plt.show()