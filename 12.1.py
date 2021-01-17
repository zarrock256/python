#Napisać program, który na listę L wstawi n liczb wylosowanych z zakresu od 0 do k-1. Następnie program wylosuje
# liczbę y z tego samego zakresu i znajdzie wszystkie jej wystąpienia na liście L przy pomocy wyszukiwania liniowego.
# [n=100, k=10]

import random

n = 100
k = 10
L = []

for i in range(n):
    L.append(random.randint(0,k-1))

pattern = random.randint(0,k-1)
found = []
print("Tablica n losowych liczb z zakresu (0,k-1):")
print(L)
print("Miejsca wystąpienia liczby ",pattern)
for i in range(n):
    if L[i] == pattern:
        found.append(i)
if len(found) == 0:
    found.append(-1)    #-1 sygnalizuje, że szukana liczba nie występuje w przeszukiwanym zbiorze
print(found)