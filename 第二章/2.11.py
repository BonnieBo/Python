# 计算投资额

final_value = eval(input("Enter final account value: "))

interest_rate = eval(input("Enter annual interest rate in percent:"))

years = eval(input("Enter numver of years:"))

deposit_value = final_value/(1+interest_rate*0.01/12)**(years*12)  # 复利 按月利率算
print("Initial deposit value is ", deposit_value)

deposit_value = final_value/(1+interest_rate*0.01)**years # 复利 按年利率算
print("Initial deposit value is ", deposit_value)

deposit_value = final_value / (1+interest_rate*0.01*years)  # 不复利
print("Initial deposit value is ", deposit_value)


