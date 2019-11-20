# 风寒温度

temp = eval(input("Enter the temperature in Fahrenheit between -58 and 41:"))
wind_speed = eval(input("Enter the wind speed in miles per hour:"))

wind_chill = 35.74 + 0.6215*temp - 35.75*(wind_speed**0.16)+ 0.4275*temp*(wind_speed**0.16)

print("The wind chill index is", wind_chill)