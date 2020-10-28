#Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3

for number in range(31):
    if number%3 != 0:
        print(number)