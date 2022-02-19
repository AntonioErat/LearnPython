from random import choice


def getUserChoice(options):
    validInputs=""
    for opt in options:
        validInputs+=opt[0]
        print(opt[0], "-", opt[1])
        prompt="What do you want to do? [" + validInputs + "]: "
        choice=""
        done=False
        while not done:
            choice=input(prompt).strip().upper()
            if len(choice) > 1:
                choice=choice[0]
            if len(choice) == 1 and choice in validInputs:
                done = True
        return choice