# 计算三角形面积
import math

try:
    a,b,c = map(float,input().split())

    if a + b > c and b + c > a and a + c > b:
        p = (a + b + c) / 2 

        under_sqrt = p * (p-a) * (p-b) * (p-c)
    
        if under_sqrt >= 0:
            print(f"{math.sqrt(under_sqrt):.2f}")
        else:
             print("0.0")

    else:
        print("错误")

except:
    print("0.00")
       


     




