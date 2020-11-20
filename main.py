import vortoParser
import bdd
import getpass


print("Mot de passe ?")
mdp = getpass.getpass()

bdd = bdd.Interface(mdp)

def addWordToBdd(word, trad, type=""):
    rad, path = vortoParser.getPath(word)
    n = len(path)
    if bdd.checkNode(word):
        print("word already in database")
        return True
    else:
        i = 0
        while i < n and bdd.checkNode(path[i][0]):
            i += 1
        j = i
        while i < n:
            if i == 0:
                label = "Radical" if len(rad) == 1 else "Radical_compose"
            elif i == n-1:
                label = type if type != "" else vortoParser.getType(word)
            else:
                label = "Compose"
            bdd.addNode(label, path[i][0], trad if i == n-1 else "")
            i += 1
        for k in range(max(1, j), n):
            #Draw relations
            bdd.addRelation(path[k - 1][0], path[k][0], path[k][1], path[k][2])
    if len(rad) > 1:
        for r in rad:
            if not bdd.checkNode(r):
                bdd.addNode("Radical", r, "")
            bdd.addRelation(r, path[0][0], "Fusion", "")
