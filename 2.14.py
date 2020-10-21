line = "to jest ciag wielu wyrazow\n    druga linijka\ntrzecia linia i GvR\n    czwarta linia"
longestWord = ""
size = 0;                       #Program przydziela miano najdłuższego słowa pierwszemu występującemu najdłuższemu słowu
for item in line.split():       #rozdzielenie zmiennej 'linia' na poszczególne słowa
    if len(item) > size:        #sprawdzania długości poszczególnych słów
        size = len(item)        #jeśli długość sprawdzanego słowa jest większa, to zastąp długość długością nowego słowa
        longestWord = item      #zastąp najdłuższe słowo nowym najdłuższym słowem
print(f"a) Longest word: {longestWord}\nb) length: {len(longestWord)}")   #wyświetlanie wyników
