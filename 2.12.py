line = "to jest ciag wielu wyrazow\n    druga linijka\ntrzecia linia i GvR\n    czwarta linia"
newLine = ""
for item in line.split():   #Rozdzielenie stringa 'line' na poszczególne wyrazy
    newLine += item[0]      #pobieranie pierwszej litery z każdego wyrazu
print(newLine)              #wyświetlenie nowego napisu

newLine2 = ""
for item in line.split():    #Rozdzielenie stringa 'line' na poszczególne wyrazy
    newLine2 += item[-1]     #pobieranie ostatniej litery z każdego wyrazu
print(newLine2)              #wyświetlenie nowego napisu