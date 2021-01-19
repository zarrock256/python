#Zaimplementować prostą metodę znajdowania mediany polegającą na posortowaniu zbioru i wybraniu elementu środkowego.

import random
import math

n = 5
k = 10
L = []

def mediana_sort(L1, left, right):
    L = []
    for i in range(left,right+1):
        L.append(L1[i])
    L.sort()
    print(L)
    rightL = len(L)-1
    if len(L)%2 == 0:
        mid = (rightL)/2
        return (L[math.floor(mid)] + L[math.ceil(mid)])/2
    return L[(rightL)//2]

for i in range(n):
    L.append(random.randint(0,k-1))

print(L)
print(mediana_sort(L,1,4))