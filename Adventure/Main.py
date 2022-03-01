#######################################

        #Mountain Adventure

         #By Antonio Erat

#######################################

from Adventure.Inventory import findStructureKey
import Strings
import Utils
import Inventory as inv

def doWelcome():
   print(Strings.get("Welcome"))

def doStart():
   print(Strings.get("Start"))
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
   if not inv.hasStructuretool:
        print(Strings.get("Knife"))
        inv.findStructureKey
   elif inv.hasStructuretool:
        print("Good job, you found the knife. Put it to good use.")
        doStart
   else:
     print(Strings.get("Boulders"))
     doStart()

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

def doStructureDoor():
     print(Strings.get("HutDoor"))
     if inv.hasStructuretool():
          print(Strings.get("HutDoorNoKey"))
     else:
     
          print(Strings.get("StructureDoorNoKey"))
          choices = [
               ["S", "Back to the structure"],
               ["R", "RUN!"]
          ]
     if inv.hasStructuretool():
          choices.insert(0,["U", "Unblock the door"])
     choice = Utils.getUserChoice(choices)
     if choice == 'S':
          doHut()
     elif choice == 'R':
          doRun()
     elif choice == 'U':
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

def doGrowling():
     pass

def doRun():
   print(Strings.get("RUN"))
   gameOver()

def gameOver():
    print(Strings.get("GameOver"))

doWelcome()
doStart()