def inputNumber(prompt):
    inp = ""
    while not inp.isnumeric():
        inp = input(prompt).strip()
    return int(inp)

num=inputNumber("Enter a number: ")
print(num)