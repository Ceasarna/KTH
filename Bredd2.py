import sys
from linkedQFile import LinkedQ
from bintreeFile import Bintree


class ParentNode:
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent

def writechain(slutordsnod):
    if slutordsnod.parent is not None:
        writechain(slutordsnod.parent)
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


def makechildren(word, end, queue):
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
                    gamla.put(new_word)
                    queue.enqueue(ParentNode(new_word, word))
                    # If it so happens that we find the word that is looked for, return ParentNode.
                    if new_word == end:
                        writechain(ParentNode(end, word))
                        return True
            # When the whole alfabet has been checked through, add +1 to i and re-loop.
            if letter == 'ö':
                i += 1
                start_word = list(word.word)
                break


start = ParentNode(input("Start"))
end = input("End")
q = LinkedQ()
q.enqueue(start)
gamla.put(start.word)

while not q.isEmpty():
    # Takes the first element in the queue and removes it. This will then be checked.
    nod = q.dequeue()
    exist = makechildren(nod, end, q)

    if exist:
        print("There was a way!")
        sys.exit()
if not exist:
    print("There was no way.")

    """
    if isinstance(makechildren(nod, end, q), ParentNode):
        end_node = makechildren(nod, end, q)
        writechain(end_node)
        sys.exit()

print("nein")
    """