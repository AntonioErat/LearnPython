import random

length = input("How long should your password be? ")
length = int(length)
if length < 8:
    print("Please enter a number greater than 8.")
characters = input("What kind of charcters do you want? letters, numbers, symbols, or all? ").upper().strip()
password11 = 0
while password11 < length:
    if characters == "ALL":
        password11 + 1
        password1=random.choice("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!@#$%^&*()><?/:;]}[{")
        print(password1)
    elif characters == "LETTERS":
        password2=random.choice("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")
        print(password2)
    elif characters == "NUMBERS":
        password3=random.choice("0123456789")
        print(password3)
    elif characters == "SYMBOLS":
        password4=random.choice("!@#$%^&*()><?/:;]}[{")
        print(password4)
    else:
        print("Please enter letters, numbers, symbols, or all")
    password11+=1