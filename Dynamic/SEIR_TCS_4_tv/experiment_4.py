import matplotlib.pyplot as plt

import SEIR_np, SEIR_tanlan, SEIR_dongtai1, SEIR_zhenxiang, SEIR_truth_dynamic

plt.plot(SEIR_np.infect, 'm.-', label='NP')
plt.plot(SEIR_tanlan.infect, 'b.-', label='CGA')
plt.plot(SEIR_dongtai1.infect, 'g.-', label='DRIMUX')
plt.plot(SEIR_zhenxiang.infect, 'y.-', label='TCS')
plt.plot(SEIR_truth_dynamic.infect, 'r.-', label='DRITCS')


plt.legend(loc='upper right')  # 显示图例


# 添加x，y轴描述信息及标题
plt.ylabel('Number')
plt.xlabel('Transmission times')

plt.title('Changes in the number of infected')
plt.savefig("1.png")
plt.savefig("1.pdf")
plt.show()

plt.plot(SEIR_np.list_infect_sum, 'm.-', label='NP')
plt.plot(SEIR_tanlan.list_infect_sum, 'b.-', label='CGA')
plt.plot(SEIR_dongtai1.list_infect_sum, 'g.-', label='DRIMUX')
plt.plot(SEIR_zhenxiang.list_infect_sum, 'y.-', label='TCS')
plt.plot(SEIR_truth_dynamic.list_infect_sum, 'r.-', label='DRITCS')


plt.legend(loc='upper left')  # 显示图例



# 添加x，y轴描述信息及标题
plt.ylabel('Number')
plt.xlabel('Transmission times')

plt.title('Number of infect')
plt.savefig("2.png")
plt.savefig("2.pdf")
plt.show()
