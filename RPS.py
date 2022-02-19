#Imports
import random

#Ask the user for their name
name=input("What is your name?: ")

#Computer picks one
cChoice = random.choice("RPS")

#Get user choice
print("Hello", name, "let's play Rock, Paper, or Scissors")
uChoice=input("Enter R, P, S").upper().strip()

#Test it
print("You:", uChoice)
print("Computer:", cChoice)

#TOP SECRET CODE
if name == "AntonioHax":
    if uChoice == "R":
        cChoice = "S"
    elif uChoice == "P":
        cChoice = "R"
    elif uChoice == "S":
        cChoice = "P"


#Compare choices
if cChoice == uChoice:
    print("It's a tie!")
elif uChoice == "R"and cChoice == "P":
    print("You picked rock, computer picked paper. You lose.")
elif uChoice == "P"and cChoice == "R":
    print("You picked paper, computer picked rock. You win!")
elif uChoice == "R"and cChoice == "S":
    print("You picked rock, computer picked scissors. You win!.")
elif uChoice == "S"and cChoice == "R":
    print("You picked scissors, computer picked rock. You lose.")
elif uChoice == "P"and cChoice == "S":
    print("You picked paper, computer picked scissors. You lose.")
elif uChoice == "S"and cChoice == "P":
    print("You picked scissors, computer picked paper. You win!.")
else:
    print("Not very good at listening to instructions. Huh?")