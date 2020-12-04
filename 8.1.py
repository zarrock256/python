#Zbadać problem szukania rozwiązań równania liniowego postaci a * x + b * y + c = 0. Podać specyfikację problemu.
# Podać algorytm rozwiązania w postaci listy kroków, schematu blokowego, drzewa. Podać implementację algorytmu w
# Pythonie w postaci funkcji solve1(), która rozwiązania wypisuje w formie komunikatów.


def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0 and b == 0 and c == 0:
        print("Jest to równanie tożsamościowe. Każda para (x,y) jest rozwiązaniem.")
    elif a != 0 and b == 0:
        print("Rozwiązaniem równania jest para: x = {0:f} i dowolny y.".format(-c/a))
    elif a == 0 and b != 0:
        print("Rozwiązaniem równania jest para: dowolny x i y = {0:f}.".format(-c/b))
    elif a == 0 and b == 0:
        print("Równanie jest równaniem sprzecznym.")
    else:
        message = "Rozwiązaniem jest para x i y takie, że: "
        if c == 0:
            message += "\nx = {0:.2f}y  \ny = {1:.2f}x ".format(-b / a, -a / b )
        else:
            if -c/a > 0:
                message += "\nx = {0:.2f}y + {1:.2f}".format(-b/a,-c/a)
            elif -c/a < 0:
                message += "\nx = {0:.2f}y - {1:.2f}".format(-b/a,-c/a)
            if -c/b > 0:
                message += "\ny = {0:.2f}x + {1:.2f}.".format(-a/b,-c/b)
            elif -c/b < 0:
                message += "\ny = {0:.2f}x - {1:.2f}.".format(-a/b,-c/b)
        print(message)

solve1(2,1,-1)
_ = 1
print(_)