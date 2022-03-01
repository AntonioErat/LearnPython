from ast import Lambda
from operator import contains


inv = {
    "StructureTool": False,
    "Coins": 0
}

def findStructureKey():
    inv["StructureTool"] = True

def loseStructureKey():
    inv["StructureTool"] = False

def hasStructuretool():
    return inv["StructureTool"]

def takeCoins(coins):
    inv["Coins"] += coins 

def loseCoins(coins):
    inv["Coins"] -= coins

def numCoins():
    return inv["Coins"]