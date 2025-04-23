import matplotlib.pyplot as plt
# import IC_tv, SIR_tv, SEIR_tv
import IC_tv, SIR_tv, SEIR_tv

plt.plot(IC_tv.list_sum, 'm.-', label='IC')
plt.plot(SIR_tv.infect, 'b.-', label='SIR')
plt.plot(SEIR_tv.list_infect, 'g.-', label='SBRPM')
# plt.plot(LT_impove_tv.seed_nodes,'y.-',label='LT')

plt.legend(loc='center right')  # 显示图例


# 添加x，y轴描述信息及标题
# plt.ylabel('Number of infected')
# plt.xlabel('Transmission times')

plt.ylabel('Number of infected', fontsize=14)
plt.xlabel('Transmission times', fontsize=14)
plt.legend(fontsize=14, markerscale=1, scatterpoints=1)
plt.title('TV_model',fontsize=14)
plt.savefig("tv_food.png")
plt.savefig("tv_food.pdf")
plt.show()