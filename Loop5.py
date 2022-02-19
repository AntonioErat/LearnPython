animals =[]

userInput = " "

print("I can sort animals for you.")
print("Enteryour animals, one at a time.")
print("When you are done just press enter.")

while userInput != "":
    userInput=input("Enter an animal, leave empty to end: ").strip()
    if len(userInput) > 0:
        animals.append(userInput)

animals.sort()

print(animals)

#For the challenge make it so the animals print out 1 per line, and checks if an animals is repeated, check chap. 6 for help