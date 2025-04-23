import matplotlib.pyplot as plt

import IC_sport, SIR_sport, SEIR_sport

plt.plot(IC_sport.list_sum, 'm.-', label='IC')
plt.plot(SIR_sport.infect, 'b.-', label='SIR')
plt.plot(SEIR_sport.list_infect, 'g.-', label='SBRPM')
# plt.plot(LT_impove_sport.seed_nodes,'y.-',label='LT')

plt.legend(loc='center right')  # 显示图例



# 添加x，y轴描述信息及标题
# plt.ylabel('Number of infected')
# plt.xlabel('Transmission times')

plt.ylabel('Number of infected', fontsize=14)
plt.xlabel('Transmission times', fontsize=14)
plt.legend(fontsize=14, markerscale=1, scatterpoints=1)
plt.title('Sport_model', fontsize=14)
plt.savefig("sport_media.png")
plt.savefig("sport_media.pdf")
plt.show()