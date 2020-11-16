#Stworzyć plik rekurencja.py i zapisać w nim funkcje z zadań 4.3 (factorial), 4.4 (fibonacci).
# Sprawdzić operacje importu i przeładowania modułu.
import time
import rekurencja
import importlib
#import rekurencja as rek
#from rekurencja import *
# from rekurencja import factorial_iterative as fact
#from rekurencja import fibonacci as fib

print ( rekurencja.factorial_iterative(6) )
#print ( rek.fibonacci(5) )
#print ( rek.factorial_iterative(6) )
#print ( rekurencja.fibonacci(5) )
#print ( factorial_iterative(6) )
#print ( fibonacci(5) )
#print ( fact(6) )
#print ( fib(5) )

time.sleep(10)                  #Kiedy zmieni się plik rekurencja.py w czasie uśpienia programu głównego, to
importlib.reload(rekurencja)    #funkcja reload() pozwala na wczytanie tych zmian i zastosowanie nowych przepisów
print ( rekurencja.factorial_iterative(6) )
