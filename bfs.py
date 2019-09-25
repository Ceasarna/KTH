alfabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'x', 'y', 'z', 'å', 'ä', 'ö')
svenska = []
with open("word3.txt", "r", encoding="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()  # Ett trebokstavsord per rad
        svenska.append(ordet)

def makechildren(start):

    startword1 = list(start)
    startword2 = list(start)
    startword3 = list(start)

    for letter1 in alfabet:
        startword1[0] = letter1
        rest1 = "".join(startword1[1:])
        newword1 = letter1 + rest1
        if newword1 in svenska:
            if newword1 != start:
                print(newword1)

    for letter2 in alfabet:
        startword2[1] = letter2
        reststart = "".join(startword2[0])
        restend = "".join(startword2[2])
        newword2 = reststart + letter2 + restend
        if newword2 in svenska:
            if newword2 != start:
                print(newword2)

    for letter3 in alfabet:
        startword3[2] = letter3
        rest3 = "".join(startword3[0:2])
        newword3 = rest3 + letter3
        if newword3 in svenska:
            if newword3 != start:
                print(newword3)



makechildren("söt")


class Node:
    def __init__(self, key):
        self.key = key
        self.connectedTo = {}


