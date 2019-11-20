# 输入一个1~1000之间的数字 计算各个数位上的数 的 和

num = eval(input("Enter a number between 0 and 1000:"))
'''
if num // 10 == 0:
    sum1 = num
    print("The sum of the digits is " + num)

elif num // 100 == 0:
    sum2 = num % 10 + num // 10
    print(sum2)

else:
    sum3 = num%100%10 + num//100 + num//10%10
    print(num%100%10)
    print(num//100)
    print(num//10%10)
    print(sum3)

'''

sum3 = num%100%10 + num//100 + num//10%10
print("个位数是: ", num%100%10) # 求个位数
print("十位数", num//10%10) # 求十位数
print("百位数是:", num//100) # 求百位数

print("位数和:", sum3)