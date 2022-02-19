asciiMin = 32
asciiMax = 126

key = 314159
key = str(key)

message = input("Enter message to be decrypted: ")

messEncr = ""

for index in range(0, len(message)):
    char = ord(message[index])
    if char < asciiMin or char > asciiMax:
        messEncr += message[index]
    else:
        ascNum = char - int(key[index % len(key)])
        if ascNum < asciiMax:
            ascNum += (asciiMax - asciiMin)
        messEncr = messEncr + chr(ascNum)

print("Decrypted message:", messEncr)