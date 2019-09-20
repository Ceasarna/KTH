from Pokemon import Pokemon

class Node:
    def __init__(self, key = "", value = None):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.dictionary = {}
        self.size = size

    def __getitem__(self, item):
        return self.search(item)

    def __contains__(self, item):
        for i in self.dictionary:
            if i == item:
                return True
        return False

    def store(self, key, value):
        self.dictionary[key] = value

    def search(self, key):
        try:
            if key in self.dictionary:
                return print(self.dictionary[key])
        except KeyError as Error:
            print("There was a KeyError! Here is the message: ", Error)

    def hashfunction(self, key):
        counter = 0.1
        for i in key:
            (ord(i) * 10000) / (counter * 10)
            counter *= 10


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

blabla = HashTable()

read_create_pokemon_from_file()

blabla["Bulbasaur"]


