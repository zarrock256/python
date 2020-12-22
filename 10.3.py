#Stworzyć implementację tablicową stosu do przechowywania bez powtórzeń liczb całkowitych od 0 do size-1.
# Powtarzająca się liczba ma być ignorowana bez żadnej akcji (inne podejście to wyzwolenie wyjątku). Wskazówka:
# stworzyć drugą tablicę, w której 0 lub 1 na pozycji i oznacza odpowiednio brak lub istnienie liczby i na stosie.

class Stack:
    def __init__(self, startSize):
        self.start = startSize
        self.tab = []
        self.size = 0
        self.addTab = []
        for i in range(startSize+1):    #Przewiduje przechowywanie liczb całkowitych od 0 do startSize
            self.addTab.append(0)


    def push(self, data):
        if data <= self.start:
            if self.addTab[data] == 0:
                self.addTab[data] = 1
                self.tab.append(data)
                self.size += 1

    def pop(self):
        if not self.isEmpty():
            temp = self.tab.pop()
            self.addTab[temp] = 0
            self.size -= 1
            return temp
        return 'Empty'

    def isEmpty(self):
        if self.size == 0:
            return True
        return False





