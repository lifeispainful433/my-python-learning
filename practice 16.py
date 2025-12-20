# 判断正负

num = input()
if not num.lstrip('-').isdigit():
    print("错误")
else:
    num = int(num)
    
    if (num % 2) == 0:
        print("是偶数")
    elif (num % 2) != 0:
        print("是奇数")