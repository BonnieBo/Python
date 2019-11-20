# 计算身体质量指数 BMI

your_weight = eval(input("Enter weight in pounds: "))
your_height = eval(input("Enter height in inches: "))

your_height_kg = your_weight * 0.45359237
your_weight_m = your_height * 0.0254

BMI = your_height_kg/your_weight_m**2

print("BMI is", BMI)
