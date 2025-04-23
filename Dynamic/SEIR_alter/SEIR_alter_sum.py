import SEIR_alter1, SEIR_alter2, SEIR_alter3, SEIR_alter4, SEIR_alter5

import matplotlib.pyplot as plt


plt.plot(SEIR_alter2.infect, 'b.-', label='α=[0.2,0.4]')
plt.plot(SEIR_alter3.infect, 'g.-', label='α=[0.4,0.6]')
plt.plot(SEIR_alter4.infect, 'y.-', label='α=[0.6,0.8]')
plt.plot(SEIR_alter5.infect, 'r.-', label='α=[0.8,1.0]')
plt.plot(SEIR_alter1.infect, 'm.-', label='α=[1.0,1.2]')

plt.legend(loc='upper right')  # 显示图例


# 添加x，y轴描述信息及标题
plt.ylabel('Number')
plt.xlabel('Transmission times')

# plt.title('对比')

plt.title('Compared  α')
plt.savefig("1.png")
plt.savefig("1.pdf")
plt.show()


plt.plot(SEIR_alter2.list_infect_sum, 'b.-', label='α=[0.2,0.4]')
plt.plot(SEIR_alter3.list_infect_sum, 'g.-', label='α=[0.4,0.6]')
plt.plot(SEIR_alter4.list_infect_sum, 'y.-', label='α=[0.6,0.8]')
plt.plot(SEIR_alter5.list_infect_sum, 'r.-', label='α=[0.8,1.0]')
plt.plot(SEIR_alter1.list_infect_sum, 'm.-', label='α=[1.0,1.2]')

plt.legend(loc='upper left')  # 显示图例


# 添加x，y轴描述信息及标题
plt.ylabel('Number ')
plt.xlabel('Transmission times')

plt.title('Compared  α')
plt.savefig("3.png")
plt.savefig("3.pdf")

plt.show()