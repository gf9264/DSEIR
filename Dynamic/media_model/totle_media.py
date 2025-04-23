import matplotlib.pyplot as plt

import IC_media, SIR_media, SEIR_media

plt.plot(IC_media.list_sum, 'm.-', label='IC')
plt.plot(SIR_media.infect, 'b.-', label='SIR')
plt.plot(SEIR_media.list_infect, 'g.-', label='SBRPM')
# plt.plot(LT_impove_sport.seed_nodes,'y.-',label='LT')

plt.legend(loc='center right')  # 显示图例


# 添加x，y轴描述信息及标题

plt.ylabel('Number of infected', fontsize=14)
plt.xlabel('Transmission times', fontsize=14)
plt.legend(fontsize=14, markerscale=1, scatterpoints=1)

plt.title('Media_model', fontsize=14)
plt.savefig("media_model.png")
plt.savefig("media_model.pdf")
plt.show()