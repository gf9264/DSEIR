import SEIR_beta1, SEIR_beta2, SEIR_beta3, SEIR_beta4

import matplotlib.pyplot as plt

plt.plot(SEIR_beta1.infect, 'm.-', label='β=[0,0.25]')
plt.plot(SEIR_beta2.infect, 'b.-', label='β=[0.25,0.5]')
plt.plot(SEIR_beta3.infect, 'g.-', label='β=[0.5,0.75]')
plt.plot(SEIR_beta4.infect, 'y.-', label='β=[0.75,1]')
# plt.plot(SEIR_beta5.infect, 'r.-', label='β=[0.8,1.0]')


plt.legend(loc='upper right')  # 显示图例


# 添加x，y轴描述信息及标题
plt.ylabel('Number')
plt.xlabel('Transmission times')

# plt.title('对比')

plt.title('Compared  β')
plt.savefig("1.png")
plt.savefig("1.pdf")
plt.show()


plt.plot(SEIR_beta1.list_infect_sum, 'm.-', label='β=[0,0.25]')
plt.plot(SEIR_beta2.list_infect_sum, 'b.-', label='β=[0.25,0.5]')
plt.plot(SEIR_beta3.list_infect_sum, 'g.-', label='β=[0.5,0.75]')
plt.plot(SEIR_beta4.list_infect_sum, 'y.-', label='β=[0.75,1]')
# plt.plot(SEIR_beta5.list_infect_sum, 'r.-', label='β=[0.8,1.0]')


plt.legend(loc='upper left')  # 显示图例


# 添加x，y轴描述信息及标题
plt.ylabel('Number')
plt.xlabel('Transmission times')

# plt.title('对比')

plt.title('Compared  β')
plt.savefig("3.png")
plt.savefig("3.pdf")
plt.show()
