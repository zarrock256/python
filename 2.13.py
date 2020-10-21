line = "to jest ciag wielu wyrazow\n    druga linijka\ntrzecia linia i GvR\n    czwarta linia"
size = 0
for item in line.split():
    size += len(item)       #dodanie do siebie długości poszczególnych wyrazow
print(size)