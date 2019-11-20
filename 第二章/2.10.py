# 计算跑道长度
v, a = eval(input("Enter speed and acceleration: "))

length = v * v / (a*2)
print("The minimum runway length for this airplane is", length, "meters")