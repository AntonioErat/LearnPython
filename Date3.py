#Imports
import datetime

#Get todays date
today=datetime.datetime.now()

#Display the right message for different days of the week
if today.weekday() == 5 or today.weekday() == 6:
    #Display this if it is saturday or sunday
    print("Its the weekend, no school today!")
    print("We can code all day long!")
elif today.weekday() == 4:
    #Display this if it's friday
    print("It's Friday, tomorrow we'll have tons of time to code!")

    #Display this every other day
else:
        print("It's a school day.")