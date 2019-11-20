# 输入 金额 酬金率 计算 小费及总额

subtotal, gratuity_rate = eval(input("Enter the subtotal and a gratuity rate: "))

gratuity = subtotal * gratuity_rate/100
total = subtotal + gratuity

print("The gratuity is ", gratuity, "and the total is", total)