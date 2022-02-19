gameWord = "apocalypse"
guessedLetters = ['a','e']
maskChar = "*"
displayWord = ""
for letter in gameWord:
    print(letter)
    if letter in guessedLetters:
        print("This one has been guessed")
        displayWord += letter
    else:
        print("This one is not guessed")
        displayWord += maskChar
    print("displayWord is", displayWord)


print("Original word:", gameWord)
print("Masked word: ", displayWord)