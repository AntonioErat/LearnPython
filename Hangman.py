import random
maxLives = 7
maskChar = "*"
livesUsed = 0
guessedLetters = []

gameWords = ["anvil", "boutique", "cookie", "fluff", "jazz", "pneumonia", "sleigh", "society", "topaz", "tsunami", "yummy", "zombie", 
"mansion", "hangman", "auction"]

gameWord = random.choice(gameWords)

displayWord = maskChar * len(gameWord)

while gameWord != displayWord and livesUsed < maxLives:
    
    print(displayWord)

    if len(guessedLetters) > 0:
        youTried=""
        for letter in guessedLetters:
            youTried += letter
        print("You tried", youTried)

    print(maxLives-livesUsed, "tries left")

    print()

    currGuess = input("Guess a letter ").lower()
    if len(currGuess) > 1:
        currGuess = currGuess[0]

    if currGuess in guessedLetters:
        print("You already guessed", currGuess)
    else:
        guessedLetters.append(currGuess)
        guessedLetters.sort()

        displayWord = ""
        for letter in gameWord:
            if letter in guessedLetters:
                displayWord += letter
            else:
                displayWord += maskChar

        if currGuess in gameWord:
            print("Correct!")
        else:
            print("Nope")
            livesUsed = livesUsed + 1

    print()

if displayWord == gameWord:
    print("You win,", gameWord, "is correct!!!")
else:
    print("You lose, the answer was:", gameWord)

    #challenge 9.1 is check if user put anything and if not tell them to put something
    #challenge 9.2 is to make hangman picture 