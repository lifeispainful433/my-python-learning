# 使用三引号实现多行字符串。
project_description = """
这是一个量子计算基础练习程序。
它演示了：
1. 量子比特的叠加态概率计算。
2. 量子门操作的基本数学。
3. 常用量子计算术语说明。
"""
print("项目描述：",project_description)
print("-" * 40)
#定义术语字典。
quantum_terms = {
    "Qubit": "量子比特，是量子计算的基本单位，可以同时处于|0>和|1>的叠加态。",
    "Superposition": "叠加态，一个量子系统可以同时处于多种状态的线性组合。",
    "Entanglement": "纠缠态，两个或多个量子比特之间强大的关联。"
}
#遍历字典并格式化输出。
for item, explanation in quantum_terms.items():
    print(f"- {item}: {explanation}")
print("-" * 40)

#运算符练习。
prob_1 = 0.7
prob_2 = 0.3

print(f"prob_1 = {prob_1}")
print(f"prob_2 = {prob_2}")
print(f"prob_1 + prob_2 是否等于1？")
print(f"{prob_1 + prob_2 == 1}")
print("-" * 40)

#二进制转换。
decimal_number = 5
binary_string = bin(decimal_number)[2:]

print(f"十进制数 {decimal_number} 的二进制表示是： {binary_string}")
print(f"二进制数 {binary_string} 的十进制表示是： {int(binary_string, 2)}")


print(f"THE END")
