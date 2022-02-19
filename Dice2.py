#Imports
import random


#Roll both dice
die1=random.randrange(1, 13)
die2=random.randrange(1, 13)

#Display total and individual dies
print("You rolled ", die1, "and", die2, "-that's", die1+die2)