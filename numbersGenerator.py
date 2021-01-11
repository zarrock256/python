#rzygotować moduł Pythona z funkcjami tworzącymi listy liczb całkowitych do sortowania.
# Przydatne są m.in. następujące rodzaje danych:
#(a) różne liczby int od 0 do N-1 w kolejności losowej,
#(b) różne liczby int od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji),
#(c) różne liczby int od 0 do N-1 prawie posortowane w odwrotnej kolejności,
#(d) N liczb float w kolejności losowej o rozkładzie gaussowskim,
#(e) N liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego
# (k < N, np. k*k = N).

import random
import math


def randInts(n):           #(a)
    tab = []
    for i in range(n):
        tab.append(i)
    random.shuffle(tab)
    return tab

def almostSorted(n):        #(b)
    tab = []
    for i in range(n):
        tab.append(i)
    for i in range(0, n, 2):
        if i < n-1:
            temp = tab[i]
            tab[i] = tab[i+1]
            tab[i+1] = temp
    return tab

def almostSortedReversed(n):        #(c)
    tab = []
    for i in range(n):
        tab.append(i)
    for i in range(0, n, 2):
        if i < n-1:
            temp = tab[i]
            tab[i] = tab[i+1]
            tab[i+1] = temp
    tab.reverse()
    return tab

def floatGauss(n):      #(d)
    sigma = 5
    avrg = 10
    tab = []
    for i in range(n):
        tab.append(random.gauss(avrg, sigma))
    return tab

def randomIntsRepeated(n):      #(e)    Zakładam, że n > 1, żeby n > k
    tab = []
    k = math.ceil(math.sqrt(n))
    for i in range(n):
        tab.append(random.randint(0,k))
    return tab



# print('(a): ',randInts(10))
# print('(b): ',almostSorted(10))
# print('(c): ',almostSortedReversed(10))
# print('(d): ',floatGauss(10))
# print('(e): ',randomIntsRepeated(10))