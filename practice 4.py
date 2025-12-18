import random

def count_down(shots = 100):

    for i in range(shots):
        result = random.choice([0, 1])
        yield result  # 暂停，返回结果，下次继续
    print("✅ 测量结束！")

generator = count_down(50)
List1 = list(generator)

for bit in List1:
    print(bit)

answer = [bit for bit in List1 if bit == 1]
print(f"{len(answer)}")

