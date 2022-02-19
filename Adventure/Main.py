#######################################

        #Mountain Adventure

         #By Antonio Erat

#######################################

import Strings

def doWelcome():
   print(Strings.get("Welcome"))

def doStart():
   print(Strings.get("Start"))
   choice=" "
   while not choice in "PSBR":
        print("You can:")
        print("B = Go investigate the boulders")
        print("H = Go to the hut")
        print("G = Go find out whats growling")
        print("R = RUN!")
        choice=input("What do you want to do? [B/H/G/R]").upper().strip()
   if choice == 'P':
        doBoulders()
   elif choice == 'H':
        doHut()
   elif choice == 'G':
        doGrowling()
   elif choice == 'R':
        doRun()

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