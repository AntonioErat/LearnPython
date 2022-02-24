#######################################

        #Mountain Adventure

         #By Antonio Erat

#######################################

import Strings
import Utils

def doWelcome():
   print(Strings.get("Welcome"))

def doStart():
   print(Strings.get("Start"))
   choices = [
        ["B", "Go investigate the boulders"],
        ["H", "Go to the hut"],
        ["G", "Go find out whats growling"],
        ["R", "RUN!"]
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
   else:
        print("Unexpected input:", pick)

def doBoulders():
   print(Strings.get("Boulders"))
   doStart

def doHut():
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

def doLook():
   print(Strings.get("Look"))
   choice1=" "
   while not choice1 in "SR":
        print("You can:")
        print("S = Go back to structure")
        print("R = RUN!")
        choice1=input("What do you want to do? [S/R]").upper().strip()

def doGrowling():
     pass

def doRun():
   print(Strings.get("RUN"))
   gameOver()

def gameOver():
    print(Strings.get("GameOver"))

doWelcome()
doStart()