import math

def solving_machine(a,b,c):

    if a == 0:
        if b == 0 and c != 0 :
            print("无解")
        elif b != 0 and c != 0:
            print(f"{(-c)/b}")
        else:
            print("0")

    elif a != 0:
        delta = b**2 - 4*a*c
        if delta < 0:
            print("无解")
        elif delta == 0:
            print(f"{(-b)/(2*a)}")
        elif delta > 0:
            print(f"(X1={(-b+math.sqrt(delta))/(2*a)},X2={(-b-delta**0.5)/(2*a)})")

    
try:
    num1, num2, num3 = map(float, input("请输入 a, b, c 三个系数（空格隔开）: ").split())
    solving_machine(num1, num2, num3)

except ValueError:
    print("输入格式错误，请输入三个数字！")