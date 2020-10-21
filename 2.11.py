word = "word"
newWord = ""
for item in word:
    newWord += item + "_"
newWord = newWord[:-1] #Usunięcie podkreślenia po ostatnim znaku, żeby podkreślenia znajdowały się tylko pomiędzy nimi
print(newWord)  #wypisanie nowego słowa, gdzie znaki oddzielone są podkresleniem