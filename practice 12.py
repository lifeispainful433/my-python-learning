#random.random() * (b - a) + a 
# # 随机数生成方法

import random

# 妹妹的武器大小 (随机生成，0到100之间)
mei_mei_weapon = random.uniform(0, 100)

# 哥哥的武器大小 (哥哥，快填上你的自信！)
# 提示：用 input 获取输入，记得转成 float
# ge_ge_weapon = ??? 
ge_ge_weapon = float(input())

print(f"妹妹的武器大小: {mei_mei_weapon:.2f}")
print(f"哥哥的武器大小: {ge_ge_weapon:.2f}")

# 裁判判决
if ge_ge_weapon > mei_mei_weapon:
    print("哥哥赢了！哥哥的自信果然是真的！")
    print("妹妹任凭哥哥处置～")
elif ge_ge_weapon < mei_mei_weapon:
    print("妹妹赢了！哥哥是不是吹牛了？")
    print("哥哥要被妹妹嘲笑啦！")
else:
    print("平局！看来哥哥和妹妹是天造地设的一对～")