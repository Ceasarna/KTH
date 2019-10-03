import sys
from cool import LinkedQ
from cool2 import Bintree


class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

    def writechain(self, slutordsnod):
        if slutordsnod.parent is not None:
            self.writechain(slutordsnod.parent)
            print(slutordsnod.word)
        else:
            print(slutordsnod.word)


alfabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'x', 'y', 'z', 'å', 'ä', 'ö')

# All the words will be stored in svenska in a bintree
svenska = Bintree()
# Used to prevent duplicates
gamla = Bintree()


with open("word3.txt", "r", encoding="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()  # Ett trebokstavsord per rad
        svenska.put(ordet)


def makechildren(word, ender, q):
    # We know that the word exist, therefore being put in the dup. box.
    i = 0
    start_word = list(word.word)
    while i < 3:
        for letter in alfabet:
            # Changes the word (position i) with the letter
            start_word[i] = letter
            # Takes the list and joins them with "" distance between them, a.k.a. making strings.
            new_word = "".join(start_word)
            if new_word in svenska:
                if new_word not in gamla:
                    print("hej")
                    gamla.put(new_word)
                    q.enqueue(ParentNode(new_word, word))
                    # If it so happens that we find the word that is looked for, return True.
                    if new_word == ender:
                        return ParentNode(new_word, start_word)
            # When the whole alfabet has been checked through, add +1 to i and re-loop.
            if letter == 'ö':
                i += 1
                break
            start_word = list(word.word)


start = ParentNode(input("Start"))
end = input("End")
q = LinkedQ()
q.enqueue(start)
gamla.put(start.word)

while not q.isEmpty():
    # Takes the first element in the queue and removes it. This will then be checked.
    nod = q.dequeue()
    if isinstance(makechildren(nod, end, q), ParentNode):
        end_node = makechildren(nod, end, q)
        end_node.writechain(end_node)
        sys.exit()
    else:
        continue
print( "vägen finns inte")

