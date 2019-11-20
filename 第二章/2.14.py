# 已知 三角形的 三个点的坐标 求三角形的面积
import math
first_dot_x, first_dot_y = eval(input("Enter the first point for a triangle:"))
second_dot_x, second_dot_y = eval(input("Enter the second point for a triangle:"))
third_dot_x, third_dot_y = eval(input("Enter the third point for a triangle:"))


side1 = math.sqrt((first_dot_x-second_dot_x)**2 + (first_dot_y-second_dot_y)**2)
print(side1)

side2 = math.sqrt((first_dot_x-third_dot_x)**2 + (first_dot_y-third_dot_y)**2)
print(side2)

side3 = math.sqrt((third_dot_x-second_dot_x)**2 + (third_dot_y-second_dot_y)**2)
print(side3)


s = (side1 + side2 + side3)/2
print(s)


area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))

print("The area of the triangle is", area)
