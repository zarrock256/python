#Podany fragment programu pokaże problem z wyświetlaniem list obiektów stworzonych przez użytkownika,
# jeżeli nie została zdefiniowana metoda __repr__. Jeżeli zdefiniowano tylko metodę __repr__,
# to zostanie ona użyta również wtedy, gdy zwykle pracuje __str__.
# Sprawdzić działanie kodu, jeżeli wykomentujemy metodę __str__() lub metodę __repr__().
class Time:

    def __init__(self, seconds=0):
        self.s = seconds

    def __str__(self):
        #print("Metoda __str__")
        return "{} sec".format(self.s)

    def __repr__(self):
        #print("Metoda __repr__")
        return "Time({})".format(self.s)

time1 = Time(12)
time2 = Time(3456)
print (time1, time2)        #Użycie __str__
print (time1.__repr__(), time2.__repr__())  #Użycie __repr__
#Jeżeli nie zaimplementujemy metody __repr__, to program wyświetla
#"<__main__.Time object at 0x00000236EE1EEFD0> <__main__.Time object
#at 0x00000236EE1EEDC0>", czyli nie podstawia w miejscu repr funkcji str.
#Natomiast jeśli zaimplementujemy funkcję __str__, a funkcji __repr__ już nie, to program posłuży się funkcją
# __str__ nawet przy wywołaniu funkcji __repr__.