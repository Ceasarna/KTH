import timeit

class Song:
    def __init__(self, id, time, name, title):
        self.id = id
        self.time = time
        self.name = name
        self.title = title

    def __repr__(self):
        return "ID: %s TIME: %s NAME: %s TITLE: %s" % (self.id, self.time, self.name, self.title)

    #def __lt__(self, other):
        #if self.name < other:
            #pass


def readfile():
    list_with_songs = []
    with open("unique_tracks.txt", encoding="utf8") as file:
        for index in file:
            line = index.strip()
            fields = line.split("<SEP>")
            list_with_songs.append(Song(fields[0], fields[1], fields[2], fields[3]))
    return list_with_songs


def linsok(list, testartist):
    for song in list:
        if testartist == song.title:
            return True
    return False


def binarySearch(list, testartist):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        if list[midpoint].titel == testartist:
            return True
        else:
            if testartist<list[midpoint].titel:
                return binarySearch(list[:midpoint], testartist)
            else:
                return binarySearch(list[midpoint+1], testartist)



def main():
    lista = readfile()
    mindreLista = lista[0:250000]
    n = len(mindreLista)

    print("Antal element =", n)

    sista = mindreLista[n-1]
    testartist = sista.title

    linjtid = timeit.timeit(stmt=lambda: linsok(mindreLista, testartist), number=100)
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")


main()
