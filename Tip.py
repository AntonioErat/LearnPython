from unicodedata import numeric


billAmount = input("Please enter the bill amount. ")
billAmount = float(billAmount)
tipPercentage = input("Please enter the percent for the tip. ")
tipPercentage = float(tipPercentage)

if billAmount or tipPercentage is numeric:
    tipAmount = billAmount / tipPercentage
    total = billAmount + tipAmount
    print(billAmount, "divided by", tipPercentage, "=", tipAmount, "+", billAmount, "=", total)
    print("The total cost of the bill is", total)
else:
    print("Please enter a number")