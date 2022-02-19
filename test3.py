guessedLetters = ["aeiou"]

if len(guessedLetters) > 0:
    youTried=""
    for letter in guessedLetters:
        youTried += letter
    print("You tried:", youTried)