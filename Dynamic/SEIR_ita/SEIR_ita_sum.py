import matplotlib.pyplot as plt

import SEIR_ita1, SEIR_ita2, SEIR_ita3, SEIR_ita4

plt.plot(SEIR_ita1.infect, 'm.-', label='η=[Π/3,Π/2]')
plt.plot(SEIR_ita2.infect, 'b.-', label='η=[Π/6,Π/3]')
plt.plot(SEIR_ita3.infect, 'g.-', label='η=[Π/12,Π/6]')
plt.plot(SEIR_ita4.infect, 'y.-', label='η=[Π/24,Π/12]')
# plt.plot(SEIR_beta5.infect, 'r.-', label='β=[0.8,1.0]')


plt.legend(loc='upper right')  # 显示图例


# 添加x，y轴描述信息及标题
plt.ylabel('Number')
plt.xlabel('Transmission times')

# plt.title('对比')

plt.title('Compared  η')
plt.savefig("1.png")
plt.savefig("1.pdf")
plt.show()


plt.plot(SEIR_ita1.list_infect_sum, 'm.-', label='η=[Π/3,Π/2]')
plt.plot(SEIR_ita2.list_infect_sum, 'b.-', label='η=[Π/6,Π/3]')
plt.plot(SEIR_ita3.list_infect_sum, 'g.-', label='η=[Π/12,Π/6]')
plt.plot(SEIR_ita4.list_infect_sum, 'y.-', label='η=[Π/24,Π/12]')
# plt.plot(SEIR_beta5.list_infect_sum, 'r.-', label='β=[0.8,1.0]')


plt.legend(loc='upper left')  # 显示图例


# 添加x，y轴描述信息及标题
plt.ylabel('Number')
plt.xlabel('Transmission times')

# plt.title('对比')

plt.title('Compared  η')
plt.savefig("3.png")
plt.savefig("3.pdf")
plt.show()
