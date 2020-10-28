#Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący parę x i trzecią
# potęgę x. Zatrzymanie programu następuje po wpisaniu z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast
# liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.
while True:

    x = input()
    if x == "stop":
        quit(0)
    try:
        x = float(x)
    except ValueError:
        print("Wpisz liczbę, nie tekst")
        continue
    print(f"{x} {pow(x,3)}")
