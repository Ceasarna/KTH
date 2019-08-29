class Pokemon:
    def __init__(self, nr, name, type_1, type_2, total, HP, attack, defense, sp_Atk, sp_Def, speed, generation, legendary):
        self.nr = nr
        self.name = name
        self.type_1 = type_1
        self.type_2 = type_2
        self.total = total
        self.HP = HP
        self.attack = attack
        self.defense = defense
        self.sp_Atk = sp_Atk
        self.sp_Def = sp_Def
        self.speed = speed
        self.generation = generation
        self.legendary = legendary

    def __str__(self):
        return "Nr {}. Name {}. TYPE1 {}. TYPE2 {}. Total {}. HP {}. Attack {}. Defense {}. sp_Atk {}. sp_Def {}." \
               " Speed {}. Generation {}. Legendary {}.".format(self.nr, self.name, self.type_1, self.type_2, self.total,
                                                     self.HP, self.attack, self.defense, self.sp_Atk, self.sp_Def, self.speed,
                                                     self.generation, self.legendary)

    def __lt__(self, other):
        return self.attack < other.attack

    def add_health(self, health):
        self.HP += health

    def add_attack(self, attack):
        self.attack += attack

    def check_name(self, name_input):
        return name_input == self.name

# Reads a file in which the program saves all the pokemon inside into a list. Returns the list of pokemon.
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
    return list_of_pokemon


# List of pokemon
all_pokemon_list = read_create_pokemon_from_file()

def search_pokemon_by_name(all_pokemon_list):
    name_of_pokemon = input("Write the name of a pokemon to see more details!")
    found = False

    for pokemon in all_pokemon_list:
        if pokemon.check_name(name_of_pokemon):
            return pokemon
    if not found:
        return "Pokemon not found"



def sort_pokemon_by_attack(all_pokemon_list):
    sorted_by_attack = sorted(all_pokemon_list)
    for i in sorted_by_attack:
        #print(i)
        pass


while True:
    print(search_pokemon_by_name(all_pokemon_list))
    sort_pokemon_by_attack(all_pokemon_list)

    """print(all_pokemon_list[1])
    all_pokemon_list[1].add_health(10)
    all_pokemon_list[1].add_attack(10)
    print(all_pokemon_list[1])"""