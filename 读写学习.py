import json
import os

keys = input().split()
values = input().split()

if len(keys) == len(values):
    data = dict(zip(keys, values))
else:
    print("哎呀，键和值的数量对不上！")

with open('my_data.json', 'w') as f:
    json.dump(data,f)

try:
    with open('my_data.json', 'r') as f:     
        loaded_data = json.load(f) 


    print(loaded_data)
    
except:
    print("文件不存在")

a = "my_way"
b = "save.json"

new_path = os.path.join(a,b) 

if not os.path.exists(a):
    os.makedirs(a)

with open(new_path, 'w') as f:
    json.dump(data, f)