# Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby składające się z kilku cyfr
#(ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). Należy zbudować pełny string, a potem go wypisać.

length = int(input("Proszę podac długość miarki (liczbę całkowitą dodatnią): "))
miarka = ""
for item in range(length):
    miarka += "|...."
miarka += '|\n'
for item in range(length+1):
    if item < 9:
        miarka += f"{item}    "         #Działa do liczb trzycyfrowych
    elif item < 99:
        miarka += f"{item}   "
    else:
        miarka += f"{item}  "
print(miarka)