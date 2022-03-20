from random import choice

def getUserChoice(options):
    validInputs=""
    for opt in options:
        validInputs+=opt[0]
        print(opt[0], "-", opt[1])
        prompt="What do you want to do? [" + validInputs + "]: "
    firstChoice=""
    done=False
    while not done:
        userInput=input(prompt).strip().upper()
        if len(userInput) > 1:
            firstChoice=userInput[0]
        if len(userInput) == 1 and userInput in validInputs:
            done = True
    return userInput