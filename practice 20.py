for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}x{i}={i*j}\t', end='')
    print()

'''
# 1. 最外层：用 '\n' 把每一行拼起来。
# 2. 中间层：用 ' ' 把每一列的乘法式拼起来。
# 3. 最内层：用 f-string 生成每一个 "1x2=2"。
print('\n'.join([' '.join([f'{j}x{i}={i*j}' for j in range(1, i+1)]) for i in range(1, 10)]))
'''