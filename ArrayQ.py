from array import array

class ArrayQ:
    def __init__(self):
        self.__array = array("i", [])

    def enqueue(self, data):
        self.__array.append(data)

    def dequeue(self):
        return self.__array.pop(0)

    def __str__(self):
        return self.__array

longNumber = input("Write a long number")

firstArray = ArrayQ()
listWithNumbers = [int(i) for i in str(longNumber)]
for i in listWithNumbers:
    firstArray.enqueue(i)

while q.isEmpty == False
    x = q.dequeue()
        q.enqueue(x)
    y = q.dequeue(y)
        print(y)


"""Inmatningstips är att använda input() för att läsa in hela raden,
 split() för att dela upp den och int() för
  att konvertera till heltal. Experimentera sedan med olika inmatade ordningar 
och se om du kan lista ut i vilken ordning korten ska ligga 
innan man börjar trolla för att man ska få ut alla tretton i rätt ordning"""