import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

max_iter_num = 50  # 模拟的次数
datasets = []
nodes = []
edge = []
f = open("fb-pages-sport.txt")
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
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(datasets)

# nx.circular_layout(G)##图的布局方式，圆形
# pos=nx.spring_layout(G)
#
# plt.axis('off')
# plt.title("Facebook")
# plt.show()

nx.draw_networkx(G)
plt.show()

# α直接变为免疫状态的概率
alter = random.uniform(0,0.2)
# β转化为潜伏人员的概率
beta = random.uniform(0.1,0.3)
# η为传染概率
# d = math.pi/24
# f = math.pi/2
ita = random.uniform(0.5,0.7)
# δ变为免疫的概率
deta = random.uniform(0,0.6)
# γ为恢复率系数
gamma = random.uniform(0,0.5)

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


    plt.plot(x, susceptible, 'm.-', label='susceptible')
    plt.plot(x, exposed, 'g.-', label='exposed')
    plt.plot(x, infect, 'r.-', label='infect')
    plt.plot(x, recover, 'b.-', label='recover')  # 可以修改颜色、线条风格、图例

    plt.legend(loc='upper right')  # 显示图例

    # 添加x，y轴描述信息及标题
    # 添加x，y轴描述信息及标题
    # plt.ylabel('Number')
    # plt.xlabel('Transmission times')
    # plt.title('对比')

    plt.ylabel('Number', fontsize=16)
    plt.xlabel('Transmission times', fontsize=16)
    plt.title('fb-pages-sport', fontsize=16)
    plt.legend(fontsize=16, markerscale=1, scatterpoints=1)

    plt.savefig("1.png")
    plt.savefig("1.pdf")
    plt.show()


for i in range(max_iter_num):
    new_exposed = list()  # 新进入潜伏状态的
    new_infect = list()  # 新被感染的
    new_remove = list()  # 新被治愈的
    # t3 = '%s time' % i + ' %s nodes' % len(all_exposed_nodes)
    # print('潜伏节点数：', t3)
    # t1 = '%s time' % i + ' %s nodes' % len(all_infect_nodes)
    # print('当前感染节点数：', t1)  # 当前有多少个节点被感染
    # t2 = '%s time' % i + ' %s nodes' % len(all_remove_nodes)
    # print('治愈节点数：', t2)
    # exposed_sum2 = len(all_exposed_nodes)
    # list_exposed.append(exposed_sum2)



    exposed.append(len(all_exposed_nodes))
    infect.append(len(all_infect_nodes))
    recover.append(len(all_remove_nodes))


    # p = random.uniform(0, 1)
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
                    # infect_sum3 = len(new_infect)
                    # list_infect1.append(infect_sum3)
                    # print(list_infect1)

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


    # print(all_exposed_nodes)
    # print(all_infect_nodes)
    # print(all_remove_nodes)
    # exposed_sum3 = len(all_exposed_nodes)
    # list_exposed1.append(exposed_sum3)
    # print(list_exposed)
    #
    # infect_sum2 = len(all_infect_nodes)
    # list_infect.append(infect_sum2)
    # print(list_infect)

    # remove_sum = len(all_remove_nodes)
    # list_remove.append(remove_sum)
    # print(list_remove)

# matplotlib中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']  # aaaaa.py 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）

draw_picture(nums, max_iter_num, exposed, infect, recover)


for i in range(max_iter_num):
    q = list_exposed[i]
    k = k + q
    list_exposed_sum.append(k)

for i in range(max_iter_num):
    w = list_infect[i]
    l = l + w
    list_infect_sum.append(l)

# for i in range(30):
#     e = list_remove[i]
#     m = m + e
#     list_remove_sum.append(m)


# plt.figure(figsize=(4, 3), dpi=200)  # 图片大小，清晰度

plt.plot(list_exposed, 'm.-', label='exposed')
plt.plot(list_infect, 'g.-', label='infect')


plt.legend(loc='upper right')  # 显示图例


# 添加x，y轴描述信息及标题
# 添加x，y轴描述信息及标题
# plt.ylabel('Number')
# plt.xlabel('Transmission times')
# plt.title('对比')

plt.ylabel('Number', fontsize=16)
plt.xlabel('Transmission times', fontsize=16)
plt.title('fb-pages-sport', fontsize=16)
plt.legend(fontsize=16, markerscale=1, scatterpoints=1)
plt.savefig("2.png")
plt.savefig("2.pdf")
plt.show()

plt.plot(list_exposed_sum, 'b.-', label='exposed')
plt.plot(list_infect_sum, 'r.-', label='infect')
# plt.plot(list_remove_sum, 'r.-', label='恢复的人')

plt.legend(loc='upper left')  # 显示图例


# 添加x，y轴描述信息及标题
# plt.ylabel('Number ')
# plt.xlabel('Transmission times')
plt.ylabel('Number', fontsize=16)
plt.xlabel('Transmission times', fontsize=16)
plt.title('fb-pages-sport', fontsize=16)
plt.legend(fontsize=16, markerscale=1, scatterpoints=1)
# plt.title('对比')
plt.savefig("3.png")
plt.savefig("3.pdf")
plt.show()