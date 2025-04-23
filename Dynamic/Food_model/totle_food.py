import IC_food, SIR_food, SEIR_food
import matplotlib.pyplot as plt
# import IC_food, SIR_food, SEIR_food
plt.plot(IC_food.list_sum, 'm.-', label='IC')
plt.plot(SIR_food.infect, 'b.-', label='SIR')
plt.plot(SEIR_food.list_infect, 'g.-', label='SBRPM')
# plt.plot(LT_impove_food.seed_nodes,'y.-',label='LT')

plt.legend(loc='center right')  # 显示图例


# 添加x，y轴描述信息及标题
# plt.ylabel('Number of infected')
# plt.xlabel('Transmission times')

plt.ylabel('Number of infected', fontsize=14)
plt.xlabel('Transmission times', fontsize=14)
plt.legend(fontsize=14, markerscale=1, scatterpoints=1)

plt.title('Food_model',fontsize=14)
plt.savefig("food_model.png")
plt.savefig("food_model.pdf")
plt.show()