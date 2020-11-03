#Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

def fibonacci(number):
    if number < 0:
        print("Liczba nie może być ujemna")
        quit()
    if number == 1 or number == 2:
        return 1
    previousNumber = 1
    previousNumber2 = 1
    for i in range(2, number):
        temp = previousNumber2
        previousNumber2 = previousNumber
        previousNumber = temp + previousNumber
    return previousNumber

print(fibonacci(8))