# 项目目标 ：模拟对|0>, |1>量子态以及它们的叠加态进行多次“测量”，并统计结果，验证量子概率。

import random

zero_state = 0
one_state = 1
# 定义两个基础态。

def measure_quantum_state():
    if random.random() < 0.5:
        return zero_state
    else:
        return one_state
#编写测量量子态函数。

count_0 = 0
count_1 = 0
total_measurements = 1000

for i in range(total_measurements):
    result = measure_quantum_state()

    if result == 0:
        count_0 += 1
    else:
        count_1 += 1

#计算概率并输出。
prob_0 = float(count_0) / float(total_measurements)
prob_1 = float(count_1) / float(total_measurements)

print(f"对量子叠加态进行了 {total_measurements} 次模拟测量。")
print(f"测量结果为 |0> 的次数: {count_0}, 概率: {prob_0:.4f}")  
print(f"测量结果为 |1> 的次数: {count_1}, 概率: {prob_1:.4f}")


