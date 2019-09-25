from bintreeFile import Bintree
from linkedQFile import LinkedQ

alfabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'x', 'y', 'z', 'å', 'ä', 'ö')

svenska = Bintree()
gamla = Bintree()

with open("word3.txt", "r", encoding="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()  # Ett trebokstavsord per rad
        svenska.put(ordet)

def makechildren(start, end):
    gamla.put(start)
    startword1 = list(start)
    startword2 = list(start)
    startword3 = list(start)

    for letter1 in alfabet:
        startword1[0] = letter1
        rest1 = "".join(startword1[1:])
        newword1 = letter1 + rest1
        if newword1 in svenska:
            if newword1 not in gamla:
                q.enqueue(newword1)
                gamla.put(newword1)
                if newword1 == end:
                    return True

    for letter2 in alfabet:
        startword2[1] = letter2
        reststart = "".join(startword2[0])
        restend = "".join(startword2[2])
        newword2 = reststart + letter2 + restend
        if newword2 in svenska:
            if newword2 not in gamla:
                q.enqueue(newword2)
                gamla.put(newword2)
                if newword2 == end:
                    return True

    for letter3 in alfabet:
        startword3[2] = letter3
        rest3 = "".join(startword3[0:2])
        newword3 = rest3 + letter3
        if newword3 in svenska:
            if newword3 not in gamla:
                q.enqueue(newword3)
                gamla.put(newword3)
                if newword3 == end:
                    return True

start = input("Start")
end = input("End")
q = LinkedQ()
q.enqueue(start)
while not q.isEmpty():
    nod = q.dequeue()
    found_it = makechildren(nod, q)

    if found_it:
        print("There was a way!")
        break

if not found_it:
    print("There was no way!")