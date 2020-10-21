line = "to jest ciag wielu wyrazow\n    druga linijka\ntrzecia linia i GvR\n    czwarta linia"
print(f"Alfabetycznie:  {sorted(line.lower().split())}")
print(f"Według długości wyrazów: {sorted(line.split(), key=len)}")