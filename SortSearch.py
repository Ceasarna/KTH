import timeit


class Song:
    def __init__(self, id, time, name, title):
        self.id = id
        self.time = time
        self.name = name
        self.title = title

    def __repr__(self):
        return "ID: %s TIME: %s NAME: %s TITLE: %s" % (self.id, self.time, self.name, self.title)

    def __lt__(self, other):
        return self.title < other.title


def readfile():
    list_with_songs = []
    hash_dict = {}
    with open("unique_tracks.txt", encoding="utf8") as file:
        for index in file:
            line = index.strip()
            fields = line.split("<SEP>")
            list_with_songs.append(Song(fields[0], fields[1], fields[2], fields[3]))
    sorted_list = sorted(list_with_songs)
    """
    for element in sorted_list:
        hash_dict[element.title] = element
    return hash_dict
    """
    return sorted_list

def pop_dict(dict):
    pos = 0
    with open("unique_tracks.txt", encoding="utf8") as file:
        for index in file:
            if pos < 0:
                if index.title in dict:
                    dict.pop(index.title)
                pos += 1
    return dict


def search_dict(dict, searchword):
    if searchword in dict:
        return searchword + "was found."
    else:
        return "Nothing was found."


def linsok(list, testartist):
    for song in list:
        if testartist == song.title:
            return True
    return False


def binary_search(the_list, key):
   low = 0
   high = len(the_list)-1
   found = False

   while low <= high and not found:
      middle = (low + high)//2
      if the_list[middle].title == key:
         found = True
      else:
         if key < the_list[middle].title:
            high = middle - 1
         else:
            low = middle + 1
   return found


def main():
    lista = readfile()
    mindreLista = lista
    n = len(mindreLista)

    print("Antal element =", n)

    sista = mindreLista[n-1]
    testartist = sista.title

    linjtid = timeit.timeit(stmt=lambda: binary_search(mindreLista, testartist), number=100)
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")


def mainmain():
    lista = readfile()
    mindreLista = lista
    n = len(mindreLista)
    sista = mindreLista[n - 1]
    testartist = sista.title
    print(len(lista))

    linjtid = timeit.timeit(stmt=lambda: search_dict(lista, testartist), number=100)
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")

main()



def mergeSort(alist):
    print("Splitting ", alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ", alist)

