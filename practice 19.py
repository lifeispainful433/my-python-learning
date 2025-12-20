"""a = int(input())
num = 1

if a < 0:
    print("错误")
elif a == 0:
    print("1")
else:
    for i in range(1, a):
        num = num * i
    print(num)
"""
import math

a = int(input())

if a < 0:
    print("错误")
else:
    # 直接调用 C 语言级别的实现，速度极快！
    print(math.factorial(a))

