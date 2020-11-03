#Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone
# podsekwencje. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją,
# wykonać przez isinstance(item, (list, tuple)).

def sum_seq(sequence):
    result = 0
    if isinstance(sequence, (list,tuple)) == True:
        for item in sequence:
           result += sum_seq(item)
    else:
        return sequence
    return result

print(sum_seq([(1,[1,2]),3,[2,3],(1,1)])) # result = 14