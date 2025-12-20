

def fib(n):
    if n < 1:
        return n
    else:
        return(fib(n-1)+fib(n-2))
    

t = int(input())

for i in range(t):
    print(fib(i))

'''
# 这就是那个"中央冷库"
memo = {}

def fib(n):
    # 1. 先查冷库
    if n in memo:          # 如果冷库里面有 n 这道菜
        return memo[n]     # 直接把菜端出来，不干活了
    
    # 2. 冷库里没有，才开始干活
    if n < 1:
        result = n
    else:
        # 这里会去干活，可能会递归调用
        result = fib(n-1) + fib(n-2)
    
    # 3. 做好了一定要存进冷库，给未来的自己留口饭
    memo[n] = result
    return result
'''