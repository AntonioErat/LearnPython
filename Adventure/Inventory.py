from colorama import Fore

inv = {
    "Knife": False,
    "Coins": 0
}

def takeStructureKey():
    inv["Knife"] = True

def loseStructureKey():
    inv["Knife"] = False

def hasStructuretool():
    return inv["Knife"]

def takeCoins(coins):
    inv["Coins"] += coins 

def loseCoins(coins):
    inv["Coins"] -= coins

def numCoins():
    return inv["Coins"]

def display():
    print(Fore.BLUE+"*** INVENTORY ***")
    print("You have", numCoins(), "coins")
    if hasStructuretool():
        print("You have a knife that can cut through the beam blocking the hut door")
    print("*****************")