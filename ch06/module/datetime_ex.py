import datetime

# today = datetime.datetime.today() #방법1
now = datetime.datetime.now() #방법2

# print(today)
print(now)

print("{}년{}월{}일".format(now.year,now.month,now.day))
print("{}시{}분{}초".format(now.hour,now.minute,now.second))


print(now.strftime("%Y년%m월%d일 %H:%M:%S"))

