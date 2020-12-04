#Za pomocą techniki programowania dynamicznego napisać program obliczający wartości funkcji P(i, j).
# Porównać z wersją rekurencyjną programu. Wskazówka: Wykorzystać tablicę dwuwymiarową (np. słownik)
# do przechowywania wartości funkcji. Wartości w tablicy wypełniać kolejno wierszami.

# P(0, 0) = 0.5,
# P(i, 0) = 0.0 dla i > 0,
# P(0, j) = 1.0 dla j > 0,
# P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.

def function_P(i,j):
    P = [[0] * (j+1) for k in range(i+1)]   #Tworzenie tablicy dwuwymiarowej
    for k in range(i+1):                    #Uzupełnianie pierwszego wiersza i pierwszej kolumny
        P[k][0] = 0
    for k in range(j+1):
        P[0][k] = 1
    P[0][0] = 0.5
    if i > 0 and j > 0:                     #Uzupełnianie tablicy po i-ty wiersz i j-tą kolumnę
        for k in range(1,i+1):
            for l in range(1,j+1):
                P[k][l] = 0.5 * (P[k-1][l] + P[k][l-1])
        return P[i][j]                      #po uzupełnieniu zwracana wartość z tablicy
    return P[i][j]                          #jeśli i lub j są zerem, to nie ma potrzeby obliczania niczego więcej,
                                            #poza pierwszą kolumną i wierszem

print(function_P(1,3))