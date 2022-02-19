import datetime
today = datetime.datetime.now()
curentMonth = datetime.datetime.now().month
currentDay = datetime.datetime.now().day


month = input("What month is your birthday in?")
month = int(month)
day = input("What day is you birthday?")
day = int(day)

currentYear = datetime.datetime.now().year
if ((curentMonth >= month) and (currentDay >= day)) :
    targetYear = currentYear + 1
else :
    targetYear = currentYear

bday = datetime.datetime(targetYear, month, day)

daysUntilBirthday = bday - today

print(daysUntilBirthday)