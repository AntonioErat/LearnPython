#Import
import datetime

#Get user input
year = input("What year were you born?")
year = int(year)
month = input("What month were you born?")
month = int(month)
day = input("What day were you born?")
day = int(day)

#Build the date object
bday = datetime.datetime(year, month, day)

#Display the results
if bday.weekday() == 6:
    print("You were born on Sunday")
elif bday.weekday() == 0:
    print("You were born on Monday")
elif bday.weekday() == 1:
    print("You were born on Tuesday")
elif bday.weekday() == 2:
    print("You were born on Wednesday")
elif bday.weekday() == 3:
    print("You were born on Thursday")
elif bday.weekday() == 4:
    print("You were born on Friday")
elif bday.weekday() == 5:
    print("You were born on Saturday")
