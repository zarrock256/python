#Co jest złego w kodzie:

L = [3, 5, 4] ; L = L.sort() # Niewłaściwe jest 'L =L.sort()', wystarczy samo L.sort(), otrzymamy porządany efekt

x, y = 1, 2, 3               # Dwóm zmiennym próbujemy przypisać 3 wartości. Albo dodamy jeszcze jedną zmienną, albo nie
                             # przypiszemy liczby 3

X = 1, 2, 3 ; X[1] = 4       # Jednej zmiennej próbujemy przypisać 3 wartości. Powinniśmy zrobić z niej listę:
                             # X = [1,2,3], wtedy zadziała również X[1] = 4

X = [1, 2, 3] ; X[3] = 4     # Próbujemy podmienić czwarty element listy X, która ma tylko 3 elementy.
                             # X[3] - czwarty element listy X

X = "abc" ; X.append("d")    # Traktujemy X jako listę, a jest to łańcuch string. Należy użyć X += "d"

L = list(map(pow, range(8))) # Nie wystarczy jako funkcję w mapie podać pow, ponieważ kompilator nie wie do jakiej
                             # potęgi ma podnieść dany element listy. Można wykorzystać wyrażenie lambda, aby to naprawić:
                             # L = list(map(lambda x: pow(x,2),lista)) - przykładowo dla potęgi 2

