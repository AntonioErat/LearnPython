class player:
    def __init__(self):
        self.name = input("Whats your name? ").strip()
        self.livesLeft = 3
        self.boulderVisits = 0
        
    def getName(self):
        return self.name
        
    def getLivesLeft(self):
        return self.livesLeft

    def died(self):
        if self.livesLeft > 0:
            self.livesLeft-=1

    def isAlive(self):
        return True if self.livesLeft > 0 else False

    def getBoulderVisits(self):
        return self.boulderVisits

    def visitBoulder(self):
        self.boulderVisits += 1