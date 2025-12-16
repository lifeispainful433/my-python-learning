# ==================== 项目：抛体运动模拟与数据分析器 ====================
import math
import time
import matplotlib.pyplot as plt


#定义输出函数。
def print_results(angle, results):
    print(f"\n--- 发射角度: {math.degrees(angle):.0f}° ---")
    print(f"横向速度与纵向速度：{results[angle]['Vx']:.2f}, {results[angle]['Vy']:.2f}")
    print(f"飞行时间：{results[angle]['flight_time']:.2f}")
    print(f"飞行距离：{results[angle]['range']:.2f}")
        
#利用元组去存储不变量。
constants = (9.8,)
g = constants[0]

#定义核心变量。
parameters = {"initial_velocity" : 20.0}

#利用集合储存多个角度。
launch_angles = {30, 45, 60}

#创建结果容器。
results = {}

#遍历起始角度。
for launch_angle in launch_angles:
    angle = math.radians(launch_angle)

#计算起始角度。
    V0 = parameters["initial_velocity"]
    Vx = math.cos(angle) * V0
    Vy = math.sin(angle) * V0

#计算飞行时间,水平射程。
    total_t = 2 * (Vy / g)
    range_x = Vx * total_t

#计算轨迹并储存。
    trajectory = []
    num = 20

    for i in range(num + 1):
        t = i * (total_t / num)

        X = Vx * t
        Y = Vy * t - 0.5 * g * t ** 2

        if Y < 0:
            Y = 0

        trajectory.append([X,Y]) 
     
#储存单次角度的数据。
    results[angle] = {
        "Vx" : Vx,
        "Vy" : Vy,
        "flight_time" : total_t,
        "range" : range_x,
        "trajectory": trajectory 
    }

    print_results(angle, results)

    x_coords = [p[0] for p in trajectory]
    y_coords = [p[1] for p in trajectory]

    plt.figure(figsize=(8, 5))
    plt.plot(x_coords,y_coords, 'ro-', linewidth=2, label='小球轨迹')

#找出最佳控制。
Best_angle = None
Best_range =  0

for a, b in results.items():
    if b["range"] > Best_range:
        Best_range = b["range"]
        Best_angle = a

#输出最佳控制。
print(f"\n{'='*30}")
print("---- 正在计算最佳控制 ----")
time.sleep(2) # 模拟计算延迟
print(f"最佳发射角度: {math.degrees(Best_angle):.2f}°")
print(f"最大飞行距离: {Best_range:.2f} 米")    

#打印轨迹图。
plt.show()


    
        
    

    

