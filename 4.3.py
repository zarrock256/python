#Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

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

print(factorial_iterative(1))