#######################################

        #Mountain Adventure

         #By Antonio Erat

#######################################

import Strings
import Utils
import Inventory as inv
import Player
from colorama import init, Fore
import Items
import random
import Enemies

p = Player.player()
init()

def doWelcome():
     print(Fore.GREEN+Strings.get("Welcome"))
   

def doStart():
   print(Fore.YELLOW+Strings.get("Start"))
   choices = [
        ["B", "Go investigate the boulders"],
        ["H", "Go to the hut"],
        ["G", "Go find out whats growling"],
        ["R", "RUN!"],
        ["I", "Inventory"]
   ]
   pick = Utils.getUserChoice(choices)
   if pick == 'B':
       doBoulders()
   elif pick == 'H':
       doHut()
   elif pick == 'G':
       doGrowling()
   elif pick == 'R':
       doRun()
   elif pick == 'I':
        inv.display()
        doStart()
   else:
        print("Unexpected input:", pick)


def doBoulders():
     p.visitBoulder()
     if p.getBoulderVisits() == 1:
          print(Strings.get("Boulders"))
          doStart()
     elif p.getBoulderVisits() == 3:
          print(Strings.get("Knife"))
          inv.takeStructureKey()
          doStart()
     elif inv.hasStructuretool():
          print("You have the knife. Use it.")
     else:
          print(Strings.get("Boulders2"))
     doStart()

def doHut():
     if inv.hasStructuretool() == True:
          doStructureDoor()
     else:
       print(Strings.get("Hut"))
       choice0=" "
       while not choice0 in "SLR":
          print("You can:")
          print("S = Go back to start")
          print("L = Look for a rock or something to help open the door")
          print("R = RUN!")
          choice0=input("What do you want to do? [S/L/R]").upper().strip()
     if choice0 == 'S':
        doStart()
     elif choice0 == 'L':
        doLook()
     elif choice0 == 'R':
        doRun()

def doStructureDoor():
     print(Fore.CYAN+Strings.get("HutDoor"))
     if inv.hasStructuretool():
          print(Strings.get("StructureTool"))
          print(Strings.get("EnterHut"))
          doStart()
     else:
     
          print(Strings.get("StructureDoorNoKey"))
          choices = [
               ["S", "Back to the structure"],
               ["R", "RUN!"]
          ]
     if inv.hasStructuretool():
          choices.insert(0,["U", "Unblock the door"])
     choice0 = Utils.getUserChoice(choices)
     if choice0 == 'S':
          doHut()
     elif choice0 == 'R':
          doRun()
     elif choice0 == 'U':
          doEnterHut()
def doLook():
   print(Strings.get("Look"))
   choice1=" "
   while not choice1 in "SR":
        print("You can:")
        print("S = Go back to structure")
        print("R = RUN!")
        choice1=input("What do you want to do? [S/R]").upper().strip()
   if choice1 == 'S':
          doHut()
   elif choice1 == 'R':
          doRun()

def doEnterHut():
     print(Strings.get("EnterHut"))

def doGrowling():
     pass
     doStart()

def getRandomEnemy():
     return random.choice(Enemies.enemies)

def doRun():
   print(Strings.get("RUN"))
   if p.livesLeft > 0:
        p.died()
        doStart()
   else:
        gameOver()

if Utils.randomEvent(4):
     coins=random.randrange(1, 101)
     print("You see",  coins, "coins on the ground.")
     print("You pick them up.")
     inv.takeCoins(coins)

def gameOver():
    print(Strings.get("GameOver"))

doWelcome()
doStart()