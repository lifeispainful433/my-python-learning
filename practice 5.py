
# 字典嵌套+列表 
information = {
    "Lucy" :{"灵气" : 100, "武器" : ["木棍"], "宠物" : "哮天犬", "境界" : "结丹期"},
    "Alice" : {"灵气" : 90, "武器" : ["铁铲"], "宠物" : "鲲鹏", "境界" : "元婴期"}  
}

# 函数与lambda函数
def add_weapons(name, weapon):
    if name in information:
        information[name]["武器"].append(weapon)
    else:
        print("你还不行")

add_weapons("Lucy", "gun")

print(information["Lucy"]["武器"])