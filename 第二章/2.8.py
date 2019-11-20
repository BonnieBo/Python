# 计算能量
water_kilo = eval(input("Enter the amount of water in kilograms: "))
init_temp = eval(input("Enter the initial temperature: "))
final_temp = eval(input("Enter the final temperature: "))

Q = water_kilo * (final_temp - init_temp) * 4184

print("The energy needed is", Q)
