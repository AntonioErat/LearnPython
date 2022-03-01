def get(id):
    if id == "Welcome":
        return("Welcome Adventurer!\n"
                "You wake in a daze, recalling nothing useful.\n"
                "Stumbling, you walk towards the light at the end of what seem to be a cave.\n"
                "You step outside. Nothing is familiar.\n"
                "The landscape is rocky and barren.\n"
                "You notice that you are wearing a suit and tie.")
    elif id == "Start":
        return("You look around. Theres a few small trees and bushes here and there. You spot some boulders in the distance, but other wise its empty.\n"
               "Theres a small hut-like structure off to the side.\n"
               "You here growling coming from another cave nearby")
    elif id == "Boulders":
        return("You walk over to the boulders. You see something shining, but its trapped between some of the boulders.\n"
               "No way to lift them up right now")
    elif id == "Hut":
        return("You examine the old hut. It looks like its been a few years since anyone has been here. A few centuries even.\n"
               "You start to walk away but then you hear some unearthly noises coming from inside.\n"
               "You see no windows but you think you see a collapsed doorway. No hope of going in that way without a tool.")
    elif id == "Look":
        return("You look around on the ground and see some rocks you grab the biggest and throw it at the door.\n"
               "It makes some dust fall but barely makes a difference.\n"
               "𝘞𝘦𝘭𝘭 𝘵𝘩𝘢𝘵 𝘸𝘢𝘴 𝘢 𝘭𝘦𝘵𝘥𝘰𝘸𝘯, you think.")
    elif id == "StructureDoorNoTool":
        return("You stand there for a minute, thinking about what to do.")
    elif id == "RUN":
        return("You run into the distance, and see a small crack.\n"
               "𝘐 𝘤𝘢𝘯 𝘫𝘶𝘮𝘱 𝘰𝘷𝘦𝘳 𝘵𝘩𝘢𝘵, 𝘦𝘢𝘴𝘺, you think.\n"
               "As you run up to it it grows bigger, and once you get within a few feet of it you realize it was a cliff.\n"
               "You fall right off the edge, thinking, 𝘵𝘩𝘢𝘵 𝘸𝘢𝘴𝘯'𝘵 𝘷𝘦𝘳𝘺 𝘴𝘮𝘢𝘳𝘵 𝘰𝘧 𝘮𝘦.\n"
               "You were never seen again.")
    elif id == "GameOver":
        return "Game over!"
    elif id == "StructureTool":
        return ("You think you have found a way into the hut.\n"
                "You take the knife and start sawing throught the wood beams blocking the entryway")
    elif id == "Knife":
        return ("You go over to the boulder pile determined to find whatever was stuck between the boulders\n"
                "You walk over to the hut grab a plank off the ground beside it and use it as a lever to get the blouders away from the thing.\n"
                "You reach between the boulder and grab it.\n"
                "It is a knife.")
    else:
        return "" 