#Zaimplementować prostą metodę znajdowania mediany polegającą na posortowaniu zbioru i wybraniu elementu środkowego.

import random
import math

n = 5
k = 10
L = []

def mediana_sort(L, left, right):
    L.sort()
    print(L)
    if len(L)%2 == 0:
        mid = (left+right)/2
        return (L[math.floor(mid)] + L[math.ceil(mid)])/2
    return L[(left+right)//2]

for i in range(n):
    L.append(random.randint(0,k-1))

print(L)
print(mediana_sort(L,0,len(L)-1))