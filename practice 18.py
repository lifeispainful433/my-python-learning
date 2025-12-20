lower = int(input())
upper = int(input())

# 确保从2开始，因为1不是质数
for num in range(lower, upper + 1):
    if num < 2:  # 排除小于2的数
        continue
        
    is_prime = True  # 假设num是质数
    for i in range(2, num):  # 从2开始试除，不用试1
        if num % i == 0:     # 如果能整除
            is_prime = False # 标记为不是质数
            break            # 立刻刹车，不用再试了
            
    # 只有当循环结束且is_prime还是True时，才打印
    if is_prime:
        print(num)
