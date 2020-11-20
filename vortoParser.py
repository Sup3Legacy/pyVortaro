import fixes

def checkIndic(word):
    if len(word) == 0:
        return (-2, 0)
    if word[0] == '\'':
        return ((-2), 0)
    if word[0] != "_":
        return  ((-1), 0)
    pred = 0
    taille = 1
    for i in range(1, len(word)):
        if word[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            pred = 10 * pred + int(word[i])
            taille += 1
        else:
            break
    return (pred, taille)

def checkPrefixes(word):
    found = ""
    n = len(word)
    (pred, taille) = checkIndic(word)
    word = word[taille:]
    if pred == -2:
        return ("", 0, 0)
    for p in fixes.prefixes:
        if n >= len(p):
            if word[0:len(p)] == p and len(p) > len(found):
                found = p
    if found == "":
        return ("", -1, 0)
    else:
        return (found, pred, len(found) + taille)


def checkSuffixes(word):
    found = ""
    n = len(word)
    (pred, taille) = checkIndic(word)
    if pred != -1:
        word = word[taille:]
    if pred == -2:
        return ("", 0, 0)
    for p in fixes.suffixes:
        if n >= len(p):
            if word[0:len(p)] == p and len(p) > len(found):
                found = p
    if found == "":
        return ("", -1, 0)
    else:
        return (found, pred, len(found) + taille)

def checkRadical(word):
    assert word[0] == '\''
    radics = []
    taille = 0
    i = 0
    while i < len(word):
        if word[i] == '\'':
            radics.append("")
            taille += 1
        elif word[i] == '_':
            radics.pop()
            i = len(word) - 1
            break
        else:
            radics[-1] += word[i]
            taille += 1
        i += 1
    if word[len(word) - 1] != '\'' and i == len(word):
        taille -= len(radics[-1])
        radics.pop()
    return (radics, taille)


def checkTermination(word):
    found = ""
    n = len(word)
    for p in fixes.terminaisons:
        if n >= len(p):
            if word[:len(p)] == p and len(p) > len(found):
                found = p
    return found


def decompose(word):
    n = len(word)
    res = []
    while len(word) > 0:
        pre, rad, suf = [], [], []
        term = checkTermination(word)
        n = len(word)
        while checkPrefixes(word)[2] != 0:
            new = checkPrefixes(word)
            pre.append((new[0], new[1], True))
            word = word[new[2]:]
            n = len(word)
        rad, taille = checkRadical(word)
        word = word[taille:]
        print(word)
        while checkSuffixes(word)[2] != 0:
            new = checkSuffixes(word)
            suf.append((new[0], new[1], False))
            word = word[new[2]:]
            n = len(word)
        term = checkTermination(word)
        word = word[len(term):]
        res.append((pre[::-1], rad, suf, term))
    return res


def getPath(word):
    pre, rad, suf, term = decompose(word)
    res = [(''.join(rad), "")]
    fixes = pre + suf
    fixes.sort(key = lambda x : x[1]) #liste des fixes triée par prédécence croissante
    for i in range(len(fixes)):
        fix, _, pre = fixes[i]
        if pre:
            res.append((fix + res[-1][0], "Préfixe", fix))
        else:
            res.append((res[-1][0] + fix, "Suffixe", fix))
    if len(term) > 0:
        res.append((res[-1][0] + term, "Terminaison", term))
    return (rad, res)

def getType(word):
    term = checkTermination(word)
    Verb = ["i", "as", "os", "u", "us"]
    Noun = ["o", "on", "oj", "ojn"]
    Adverb = ["e"]
    Adjective = ["a", "an", "aj", "ajn"]
    if term in Verb:
        return "Verbe"
    elif term in Noun:
        return "Nom"
    elif term in Adverb:
        return "Adverbe"
    elif term in Adjective:
        return "Adjectif"
    else:
        return "Unknown"
