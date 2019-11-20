import time

currentTime = 1203183068.328

totalSeconds = int(currentTime)
currentSeconds = totalSeconds % 60

totalMinutes = totalSeconds // 60
currentMinutes = totalMinutes % 60

totalHours = totalMinutes // 60
currentHours = totalHours % 24

print(currentHours)
print(currentMinutes)
print(currentSeconds)