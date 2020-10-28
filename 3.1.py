#Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?

#1  -  Poprawny kod - kompiluje się i wyświetla prawidłowo, średniki na końcach linii nie przeszkadzają
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
print(result)

#2 Niepoprawny kod - warunek if powinien być w następnej linijce
for i in "qwerty": if ord(i) < 100: print (i)
#Poprawiona wersja:
for i in "qwerty":
    if ord(i) < 100: print (i)
#3 Poprawny kod
for i in "axby": print (ord(i) if ord(i) < 100 else i)
