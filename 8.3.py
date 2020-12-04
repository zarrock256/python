#Obliczyć liczbę pi za pomocą algorytmu Monte Carlo. Wykorzystać losowanie punktów z kwadratu z wpisanym kołem.
# Sprawdzić zależność dokładności wyniku od liczby losowań. Wskazówka: Skorzystać z modułu random.

from points import Point
from random import randint

def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    r  = 50
    inCircle = 0
    inSquare = n

    for i in range(n):
        point = Point(randint(0,r), randint(0,r))
        if point.length() <= r:
            inCircle += 1

    return 4*inCircle/inSquare

numberOfPoints = 1
list = []
for i in range(100):
    res = calc_pi(numberOfPoints)
    if res > 3.1 and res < 3.2:
        print("{0:f} dla {1:d} punktów".format(res,numberOfPoints))
        list.append(res)
    numberOfPoints += 10
mid = 0
for i in range(len(list)):
    mid += list[i]
mid = mid/len(list)
print(mid)
