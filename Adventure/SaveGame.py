from os import path
import pickle

saveDataFile = "savedGame.p"

db = {
    "inv":inv,
    "player":player
}

pickle.dump(db, open(saveDataFile, "wb"))

if path.isfile(saveDataFile):
    db = pickle.load(open(saveDataFile, "rb"))
    inv = db[inv]
    player = db[player]