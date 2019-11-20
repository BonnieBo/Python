# 输入 分钟数  得出是多少年多啊少小时(理想情况下, 一年365天)

minute = eval(input("Enter the number of minutes:"))

years = minute / 60 / 24 // 365
days = minute / 60 / 24 % 365

print(minute, "minutes is approximately", years, "years and", days,"days")