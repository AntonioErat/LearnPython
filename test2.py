guessedLetters = []

for i in range(0,5):
    currGuess = input("Guess a letter: ").strip().lower()
    guessedLetters.append(currGuess)

guessedLetters.sort()

print(guessedLetters)