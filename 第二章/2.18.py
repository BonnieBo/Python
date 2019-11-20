# 计算时间
import time
currentTime = time.time()
print(currentTime)

totalSeconds = int(currentTime)

currentSeconds = totalSeconds % 60
totalMinutes = totalSeconds // 60

currentMinute = totalMinutes % 60
totalHours = totalMinutes // 60

currentHours = totalHours % 24

print("Current time is", currentHours, ":", currentMinute, ":", currentSeconds, "GMT")

print(time.asctime(time.localtime(time.time())))
