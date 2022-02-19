def displayWelcome(txt):
    borderChar = "*"
    print(borderChar * (len(txt) + 4))
    print(borderChar, txt, borderChar)
    print(borderChar * (len(txt) + 4))

displayWelcome("Welcome, O Great Coder Antonio!")