from Pokemon import Pokemon


CAPACITY = 100


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class hashtable:
    def __init__(self):
        self.size = 0
        self.capacity = CAPACITY
        self.slots = [None] * self.capacity

    def hashfunction(self, key):
        hashsum = 0

        for index, char in enumerate(key):
            hashsum += (index + len(key)) ** ord(char)
            hashsum = hashsum % self.capacity

        return hashsum

    def store(self, key, data):
        self.size += 1

        index = self.hashfunction(key)

        node = self.slots[index]

        if node is None:
            self.slots[index] = Node(key, data)
            return

        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, data)

    def search(self, key):
        index = self.hashfunction(key)
        node = self.slots[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value


blabla = hashtable()


def read_create_pokemon_from_file():
    fr = open("pokemon.csv")
    fr_list = []
    list_of_pokemon = []
    fr.readline()
    var = 0
    for i in fr.readlines():
        fr_list.append(i.strip().split(","))
        list_of_pokemon.append(Pokemon(fr_list[var][0], fr_list[var][1], fr_list[var][2], fr_list[var][3],
                                       float(fr_list[var][4]), float(fr_list[var][5]), float(fr_list[var][6]),
                                       float(fr_list[var][7]), float(fr_list[var][8]), float(fr_list[var][9]),
                                       float(fr_list[var][10]), int(fr_list[var][11]), fr_list[var][12]))
        var += 1
    fr.close()
    for pokemon in list_of_pokemon:
        blabla.store(pokemon.name, pokemon)
    return list_of_pokemon

read_create_pokemon_from_file()

