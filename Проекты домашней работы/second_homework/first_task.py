import time
from datetime import datetime
from math import ceil

print("Без использования datetime")

GMT = input("Введите часовой пояс\n")

timestamp = time.time()

date = ""

year = int(timestamp / 31556926)

months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
month_index = ceil((timestamp % 31556926)/2629743)

if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and months[month_index] == 2:
    day = ((timestamp % 2629743) / 86400)-29
else:
    day = int(((timestamp % 2629743) / 86400) - 28)

if day < 10:
    day = "0" + str(day)

date += str(year + 1970) + "-" + months[month_index] + "-" + str(day)

time = ""

hour = (timestamp % 86400) / 3600
minute = (timestamp % 3600) / 60
second = timestamp % 60
if hour < 10:
    hour = "0" + str(hour)
if minute < 10:
    minute = "0" + str(minute)
if second < 10:
    second = "0" + str(second)

time += str(int(hour + int(GMT))) + ":" + str(int(minute)) + ":" + str(int(second))

print(date)
print(time)

print("Использование datetime")
print(datetime.utcfromtimestamp(timestamp))

print("Дополнительная строка только для lab5")

print("Вторая ветка в задании 2.6")
