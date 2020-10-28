#Dla dwóch sekwencji znaleźć: (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
#(b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

sekw1 = [6,3,67,9,9,4,2,4,5,76,8,9,4,2,5,4,21,1,2,1,2,3,1,45,43,6]
sekw2 = [2,5,6,7,9,5,3,2,4,56,7,85,4,6,8,1,2,3,4,5,6,4,7,9,1,5,6]
sekw3 = []

# a)
for item1 in sekw1:
    for item2 in sekw2:
        if item1 in sekw2 and item1 not in sekw3:
            sekw3.append(item1)
sekw3.sort()
print("a) ",sekw3)

# b)
sekw3 = []
for item in sekw1:
    if item not in sekw3:
        sekw3.append(item)
for item in sekw2:
    if item not in sekw3:
        sekw3.append(item)
sekw3.sort()
print("b) ",sekw3)