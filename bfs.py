from bintreeFile import Bintree
from linkedQFile import LinkedQ

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


# 1. The word that will be checked with all different letters.
# 2. The word that is looked for
# 3. The current queue.
def makechildren(word, end, q):
    # We know that the word exist, therefore being put in the dup. box.
    gamla.put(word)
    i = 0
    start_word = list(word)
    while i < 3:
        for letter in alfabet:
            # Changes the word (position i) with the letter
            start_word[i] = letter
            # Takes the list and joins them with "" distance between them, a.k.a. making strings.
            new_word = "".join(start_word)
            if new_word in svenska:
                if new_word not in gamla:
                    gamla.put(new_word)
                    q.enqueue(new_word)
                    # If it so happens that we find the word that is looked for, return True.
                    if new_word == end:
                        return True
            # When the whole alfabet has been checked through, add +1 to i and re-loop.
            if letter == 'ö':
                i += 1
                break
            start_word = list(word)


start = input("Start")
end = input("End")
q = LinkedQ()
q.enqueue(start)
while not q.isEmpty():
    # Takes the first element in the queue and removes it. This will then be checked.
    nod = q.dequeue()
    connection = makechildren(nod, end, q)

    if connection:
        print("There was a way!")
        break

if not connection:
    print("There was no way!")

