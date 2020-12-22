#Stworzyć ADT w postaci kolejki losowej, z której elementy będą pobierane w losowej kolejności. Zadbać o to, aby
# każda operacja była wykonywana w stałym czasie, niezależnie od liczby elementów w kolejce.

import random

class RandomQueue:

    def __init__(self):
        self.tab = []
        self.size = 0

    def insert(self, item):
        self.tab.insert(self.size,item)
        self.size += 1

    def remove(self):                   # zwraca losowy element, w każdym przypadku wykonuje się tyle samo operacji
        if not self.is_empty():     #Następuje zwrócenie wartości, a następnie uzupełnienie dziury w tablicy wartością
            rand = random.randint(0,self.size-1)    #ostatnią
            result = self.tab[rand]
            if rand != self.size-1:
                self.tab[rand] = self.tab[self.size-1]
            self.tab[self.size - 1] = None
            self.size -= 1
            return result
        return None

    def is_empty(self):
        return self.size == 0

    def is_full(self): pass     #Moja implementacja nie przewiduje przepełnienia kolejki

    def clear(self):      # czyszczenie listy
        self.tab = []
        self.size = 0

# randQueue = RandomQueue()
#
# randQueue.insert(1)
# randQueue.insert(2)
# randQueue.insert(3)
#
# print(randQueue.remove())
# print(randQueue.remove())
# print(randQueue.remove())
#
# randQueue.insert(1)
# randQueue.insert(2)
# randQueue.insert(5)
#
# print(randQueue.remove())
# print(randQueue.remove())
# print(randQueue.remove())
