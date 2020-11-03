#Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny string przez return.
#3.5
def func_miarka():
    length = int(input("Proszę podac długość miarki (liczbę całkowitą dodatnią): "))
    miarka = ""
    for item in range(length):
      miarka += "|...."
    miarka += '|\n'
    for item in range(length+1):
        if item < 9:
            miarka += f"{item}    "         #Działa do liczb trzycyfrowych
        elif item < 99:
            miarka += f"{item}   "
        else:
            miarka += f"{item}  "
    return miarka

print(func_miarka())

#3.6
def func_squares():
    print("Wysokość i szerokość prostokąta w założeniu są liczbami całkowitymi")
    (height, length) = (int(input("Proszę podać wysokość  prostokąta: ")), int(input("Proszę podać szerokość prostokąta: ")))
    square = ""
    for item in range(height):
        for item in range(length):
            square += "+---"
        square += "+\n"
        for item in range(length):
            square += "|   "
        square += "|\n"
    for item in range(length):
        square += "+---"
    square += "+\n"
    return square

print(func_squares())