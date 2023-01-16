in_hour, in_minute, out_hour, out_minute = input().split()
in_hour = int(in_hour)
in_minute = int(in_minute)
out_hour = int(out_hour)
out_minute = int(out_minute)
hour = out_hour - in_hour
minute = out_minute - in_minute
if(minute < 0 ):
    hour -= 1
    minute = 60 -minute
minute += hour*60

if(minute <= 15):
    price = 0
elif(minute <= 180):
    price = (minute//60)*10
    if(minute%60 > 0):
        price += 10
elif(minute <= 360):
    minute -= 180
    price = 30
    price += (minute//60)*20
    if(minute%60 > 0):
        price += 20
elif(minute > 360):
    price = 200
print(price)