import requests

# 注意这里：直接把 ID 拼在 URL 里，比用 params 更直接，更不容易出错
url = "https://rickandmortyapi.com/api/character/2" 

response = requests.get(url)

if response.status_code == 200:
    # 直接打印原始文本，不进行任何 .json() 转换
    print("服务器原话：")
    print(response.text)
else:
    print(f"请求失败，状态码：{response.status_code}")