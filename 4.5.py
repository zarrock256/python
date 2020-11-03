#Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie.
# Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.

def list_reverse_iterative(L, left, right):       #wersja iteracyjna
    tempL = []
    for item in L[left:right+1]:
        tempL.append(item)
    tempL.reverse()
    index = 0
    for i in range(left,right+1):
        L[i] = tempL[index]
        index += 1
    return L
print(list_reverse_iterative([1,2,3,4,5],0,2)) #result: [3, 2, 1, 4, 5]


def list_reverse_recursive(L, left, right):       #wersja rekurencyjna
    L1 = []
    if right-left+1 < len(L):
        L1 = list(list_reverse_recursive(L[left:right+1],left,right))
    elif right-left+1 == len(L):
        L.reverse()
        return L
    index = 0
    for i in range(left,right+1):
        L[i] = L1[index]
        index += 1
    return L
print(list_reverse_recursive([1,2,3,4,5],0,2))