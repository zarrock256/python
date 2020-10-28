#Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie
# (podać kilka sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].

#Podstawowa wersja:
dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
#słownik można również stworzyć w sposób:
dict2 = {}
dict2['I'] = 1; dict2['V'] = 5; dict2['X'] = 10; dict2['L'] = 50; dict2['C'] = 100; dict2['D'] = 500; dict2['M'] = 1000
roman = input("#PODSTAWOWA WERSJA#\nProszę podać cyfrę rzymską: ")
if roman not in dict:
    print("Podano niewłaściwą liczbę rzymską")
    quit()
print("Ta cyfra odpowiada w systemie arabskim liczbie: ",dict[roman])
#Program do zamiany liczb rzymskich na arabskie
def change(str):
    if str == 'I':
        return 1
    elif str == 'V':
        return 5
    elif str == 'X':
        return 10
    elif str == 'L':
        return 50
    elif str == 'C':
        return 100
    elif str == 'D':
        return 500
    elif str == 'M':
        return 1000

romanLetter = ['I','V','X','L','C','D','M']
roman = input("#ROZSZERZONA WERSJA#\nProszę podać liczbę rzymską: ")
for index in range(len(roman)):

    if index != len(roman)-1 and roman[index] == roman[index+1]:
        temp = index
        count = 0
        while index != len(roman)-1 and roman[index] == roman[index+1]:
            count += 1
            index += 1
        if index != len(roman)-1 and count == 1 and change(roman[index]) < change(roman[index+1]):
            print("To nie liczba rzymska")
            quit()
        if (count == 3 and roman[index] == roman[index-1]) or count >= 4:
            print("To nie liczba rzymska")
            quit()
        else:
            index = temp
arab = 0
temp = 0
for index in range(len(roman)):
    if roman[index] not in romanLetter:
        print("To nie liczba rzymska")
        quit()
    if index != len(roman)-1 and change(roman[index]) >= change(roman[index+1]):
        arab += change(roman[index])
        if temp != 0:
            arab -= temp
            temp = 0
    elif index != len(roman)-1 and change(roman[index]) < change(roman[index+1]):
        temp = change(roman[index])
    if index == len(roman)-1:
        arab += change(roman[index])
        if temp != 0:
            arab -= temp
            temp = 0
print("Ta liczba odpowiada w systemie arabskim liczbie: ",arab)



