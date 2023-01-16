import time
# Morning Time : 04:00:00 to 11:59:59
# Afternoon Time : 12:00:00 to 16:59:59
# Evening Time : 17:00:00 to 20:59:59
# Night Time : 21:00:00 to 03:59:59

name = input("Enter Your Name:- ").title()
# currentTime = time.strftime('%H:%M:%S')
# print(currentTime)
hour = int(time.strftime('%H'))
if 4 <= hour < 12:
  print("Good Morning", name)
elif 12 <= hour < 17:
  print("Good Afternoon", name)
elif 17 <= hour < 21:
  print("Good Evening", name)
else:
  print("Good Night", name)