#Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać.
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
print(square)


