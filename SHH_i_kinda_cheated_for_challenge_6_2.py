# ASCII range of usable characters - anything out of this range could throw errors
asciiMin = 32   # Represents the space character - " "
asciiMax = 126  # Represents the tilde character - "~"
 
# Secret key
key = 314159    # Top secret! This is the encryption key!
key = str(key)  # Convert to string so can access individual digits
# Determine if encrypting or decrypting
action = input("Encrypt or decrypt? Enter E or D: ")
# Get input message (either encrypted message to decrypt or message to be encrypted)
if action == 'E':
    message = input("Enter message to be encrypted: ")
elif action == 'D':
    message = input("Enter message to be decrypted: ")
 
# Initialize variable for encrypted message
messEncr = ""
# Only run loop if entered E or D
if action in ['D', 'E']: 
    # Loop through message
    for index in range(0, len(message)):
        # Get the ASCII value for this character
        char = ord(message[index])
        # Is this character out of range?
        if char < asciiMin or char > asciiMax:
            # Yes, not safe to encrypt, leave as is
            messEncr += message[index]
        else:
            # Safe to encrypt or decrypt this character
            if action == 'E':
                # Encrypt and shift the value as per the key
                ascNum = ord(message[index]) + int(key[index % len(key)])
                # If shifted past range, cycle back to the beginning of the range
                if ascNum > asciiMax:
                    ascNum -= (asciiMax - asciiMin)


                    
            elif action == 'D':
                # Decrypt and shift the value as per the key
                ascNum = ord(message[index]) - int(key[index % len(key)])
                # If shifted past range, cycle back to the end of the range
                if ascNum < asciiMin:
                    ascNum += (asciiMax - asciiMin)
            # Convert to a character and add to output
            messEncr = messEncr + chr(ascNum)
    
    # Display result
    print("Encrypted message:", messEncr)
else:
    print("You must enter E or D only.")
