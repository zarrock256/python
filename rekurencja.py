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

def factorial_iterative(number):
    try:
        int(number)
    except ValueError:
        print("Niewłaściwy typ wprowadzonych danych")
        quit()
    if number < 0:
        print("Liczba nie może być ujemna")
        quit()
    result = 1
    try:
        for i in range(1,number+1):
            result *= i
        return result
    except TypeError:
        print("Liczba nie może być przecinkowa")
        quit()