import Items

def getItems():
    result = []
    for item in Items:
        i=[]
        i.append(item["key"])
        i.append(item["description"]+" ("+str(item["cost"])+" )")
        result.append(i)
    return result