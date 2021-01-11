#Porównaj czasy działania wybranych algorytmów dla listy zawierającej N różnych liczb,
# przy N = 10**2, 10**3, 10**4, 10**5, 10**6.

import numbersGenerator as ng
import datetime

def shakersort(L, left, right):
    k = right
    while left < right:
        for j in range(right, left, -1):   # od prawej
            if L[j-1] > L[j]:
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
                k = j
        left = k
        for j in range(left, right):   # od lewej
            if L[j] > L[j+1]:
                temp = L[j]
                L[j] = L[j + 1]
                L[j + 1] = temp
                k = j
        right = k

def bubblesort(L, left, right):
    limit = right
    while True:
        k = left-1   # lewy wskaźnik przestawianej pary
        for i in range(left, limit):
            if L[i] > L[i+1]:
                temp = L[i+1]
                L[i+1] = L[1]
                L[i] = temp
                k = i
        if k > left:
            limit = k
        else:
            break

def quicksort(L, left, right):
    """Sortowanie szybkie wg Cormena str. 169."""
    if left >= right:
        return
    pivot = partition(L, left, right)
    # pivot jest na swoim miejscu.
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)

def partition(L, left, right):
    """Zwraca indeks elementu rozdzielającego."""
    # Element rozdzielający to ostatni z prawej,
    # dlatego na końcu trzeba go przerzucić do środka.
    # Będzie on na docelowej pozycji ze względu na sortowanie.
    x = L[right]   # element rozdzielający
    i = left
    for j in range(left, right):
        if L[j] <= x:
            temp = L[i]
            L[i] = L[j]
            L[j] = temp
            i += 1
    temp = L[i]
    L[i] = L[right]
    L[right] = temp
    return i

def mergesort(L, left, right):
    """Sortowanie przez scalanie."""
    if left < right:
        middle = (left + right) // 2   # wyznaczanie środka
        mergesort(L, left, middle)
        mergesort(L, middle + 1, right)
        merge(L, left, middle, right)   # scalanie

def merge(L, left, middle, right):
    """Łączenie posortowanych sekwencji."""
    T = [None] * (right - left + 1)
    left1 = left
    right1 = middle
    left2 = middle + 1
    right2 = right
    i = 0
    while left1 <= right1 and left2 <= right2:
        if L[left1] <= L[left2]:   # mniejsze lub równe
            T[i] = L[left1]
            left1 += 1
        else:
            T[i] = L[left2]
            left2 += 1
        i += 1
    # Lewa lub prawa część może mieć elementy.
    while left1 <= right1:
        T[i] = L[left1]
        left1 += 1
        i += 1
    while left2 <= right2:
        T[i] = L[left2]
        left2 += 1
        i += 1
    # Skopiuj z tablicy tymczasowej do oryginalnej.
    for i in range(right - left +1):
        L[left + i] = T[i]

#-----------------------------------------------------------------------------------------
N = 10**2

tab = ng.randInts(N)

start = datetime.datetime.now()
quicksort(tab,0,N-1)
duration = datetime.datetime.now() - start

print('QuickSort dla rzędu 10^2: ', duration.microseconds)
#print(tab) Można odkomentować, żeby sprawdzić, czy rzeczywiście tablica jest posortowana

tab = ng.randInts(N)

start = datetime.datetime.now()
mergesort(tab,0,N-1)
duration = datetime.datetime.now() - start

print('MergeSort dla rzędu 10^2: ',duration.microseconds)
#print(tab) Można odkomentować, żeby sprawdzić, czy rzeczywiście tablica jest posortowana

tab = ng.randInts(N)

start = datetime.datetime.now()
bubblesort(tab,0,N-1)
duration = datetime.datetime.now() - start

print('BubbleSort dla rzędu 10^2: ',duration.microseconds)
#print(tab) Można odkomentować, żeby sprawdzić, czy rzeczywiście tablica jest posortowana

tab = ng.randInts(N)

start = datetime.datetime.now()
shakersort(tab,0,N-1)
duration = datetime.datetime.now() - start

print('ShakeSort dla rzędu 10^2: ',duration.microseconds,'\n')
#print(tab) Można odkomentować, żeby sprawdzić, czy rzeczywiście tablica jest posortowana

#-----------------------------------------------------------------------------------------
N = 10**3

tab = ng.randInts(N)

start = datetime.datetime.now()
quicksort(tab,0,N-1)
duration = datetime.datetime.now() - start

print('QuickSort dla rzędu 10^3: ', duration.microseconds)
#print(tab) Można odkomentować, żeby sprawdzić, czy rzeczywiście tablica jest posortowana

tab = ng.randInts(N)

start = datetime.datetime.now()
mergesort(tab,0,N-1)
duration = datetime.datetime.now() - start

print('mergesort dla rzędu 10^3: ',duration.microseconds)
#print(tab) Można odkomentować, żeby sprawdzić, czy rzeczywiście tablica jest posortowana

tab = ng.randInts(N)

start = datetime.datetime.now()
bubblesort(tab,0,N-1)
duration = datetime.datetime.now() - start

print('BubbleSort dla rzędu 10^3: ',duration.microseconds)
#print(tab) Można odkomentować, żeby sprawdzić, czy rzeczywiście tablica jest posortowana

tab = ng.randInts(N)

start = datetime.datetime.now()
shakersort(tab,0,N-1)
duration = datetime.datetime.now() - start

print('ShakeSort dla rzędu 10^3: ',duration.microseconds,'\n')
#print(tab) Można odkomentować, żeby sprawdzić, czy rzeczywiście tablica jest posortowana
#-----------------------------------------------------------------------------------------
N = 10**4

tab = ng.randInts(N)

start = datetime.datetime.now()
quicksort(tab,0,N-1)
duration = datetime.datetime.now() - start

print('QuickSort dla rzędu 10^4: ', duration.microseconds)
#print(tab) Można odkomentować, żeby sprawdzić, czy rzeczywiście tablica jest posortowana

tab = ng.randInts(N)

start = datetime.datetime.now()
mergesort(tab,0,N-1)
duration = datetime.datetime.now() - start

print('mergesort dla rzędu 10^4: ',duration.microseconds)
#print(tab) Można odkomentować, żeby sprawdzić, czy rzeczywiście tablica jest posortowana

tab = ng.randInts(N)

start = datetime.datetime.now()
bubblesort(tab,0,N-1)
duration = datetime.datetime.now() - start

print('BubbleSort dla rzędu 10^4: ',duration.microseconds)
#print(tab) Można odkomentować, żeby sprawdzić, czy rzeczywiście tablica jest posortowana


tab = ng.randInts(N)

start = datetime.datetime.now()
shakersort(tab,0,N-1)
duration = datetime.datetime.now() - start

print('ShakeSort dla rzędu 10^4: ',duration.microseconds,'\n')
#print(tab) Można odkomentować, żeby sprawdzić, czy rzeczywiście tablica jest posortowana
#-----------------------------------------------------------------------------------------
N = 10**5

tab = ng.randInts(N)

start = datetime.datetime.now()
quicksort(tab,0,N-1)
duration = datetime.datetime.now() - start

print('QuickSort dla rzędu 10^5: ', duration.microseconds)
#print(tab) Można odkomentować, żeby sprawdzić, czy rzeczywiście tablica jest posortowana

tab = ng.randInts(N)

start = datetime.datetime.now()
mergesort(tab,0,N-1)
duration = datetime.datetime.now() - start

print('mergesort dla rzędu 10^5: ',duration.microseconds,'\n')
#print(tab) Można odkomentować, żeby sprawdzić, czy rzeczywiście tablica jest posortowana

# tab = ng.randInts(N)                  Wykonuje się bardzo długo, dlatego zostało zakomentowane
#
# start = datetime.datetime.now()
# shakersort(tab,0,N-1)
# duration = datetime.datetime.now() - start
#
# print('ShakeSort dla rzędu 10^5: ',duration.microseconds,'\n')
#print(tab) Można odkomentować, żeby sprawdzić, czy rzeczywiście tablica jest posortowana
#-----------------------------------------------------------------------------------------
N = 10**6

tab = ng.randInts(N)

start = datetime.datetime.now()
quicksort(tab,0,N-1)
duration = datetime.datetime.now() - start

print('QuickSort dla rzędu 10^6: ', duration.microseconds)
#print(tab) Można odkomentować, żeby sprawdzić, czy rzeczywiście tablica jest posortowana

tab = ng.randInts(N)

start = datetime.datetime.now()
mergesort(tab,0,N-1)
duration = datetime.datetime.now() - start

print('mergesort dla rzędu 10^6: ',duration.microseconds)
#print(tab) Można odkomentować, żeby sprawdzić, czy rzeczywiście tablica jest posortowana

# tab = ng.randInts(N)      Wykonuje się bardzo długo, dlatego zostało zakomentowane
#
# start = datetime.datetime.now()
# shakersort(tab,0,N-1)
# duration = datetime.datetime.now() - start
#
# print('ShakeSort dla rzędu 10^6y: ',duration.microseconds,'\n')
#print(tab) Można odkomentować, żeby sprawdzić, czy rzeczywiście tablica jest posortowana

