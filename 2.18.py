liczba = 103031005120510510 #Zero występuje 7 razy
liczbaZer = 0;
for item in str(liczba):    #zamiana liczby na stringa
    if item == '0':
        liczbaZer += 1      #zwiększanie zmiennej liczbaZer o jeden, jeśli występuje znak '0'
print(liczbaZer)