import random

guesses = 0
numMin = 1
numMax = 100
userInput = ""
userGuess = 0

randNum = random.randrange(numMin, numMax+1)

print("I am thinking of a number between", numMin, "and", numMax)
print("Can you guess the number?")

while randNum != userGuess:
    userInput=input("Your guess: ").strip()
    if not userInput.isnumeric():
        print(userInput, "is not a valid number!")
    else:
        guesses=guesses+1
        userGuess=int(userInput)
        if userGuess < numMin or userGuess > numMax:
            print(userGuess, "is not between", numMin, "and", numMax)
        elif userGuess < randNum:
            print("Too low. Try again.")
        elif userGuess > randNum:
            print("Too high. Try again.")
        else:
            print("You got in,", guesses, "guesses!!!")

print("Thanks for playing!")