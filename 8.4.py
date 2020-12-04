#Zaimplementować algorytm obliczający pole powierzchni trójkąta, jeżeli dane są trzy liczby będące długościami jego
#boków. Jeżeli podane liczby nie spełniają warunku trójkąta, to program ma generować wyjątek ValueError.
from math import sqrt

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if a + b > c and a + c > b and c + b > a:
        p = (a + b + c) / 2.
        S = sqrt(p * (p - a) * (p - b) * (p - c))
        return S
    else:
        raise ValueError("Z tych odcinków nie da się zbudować trójkąta")

print(heron(10,20,25))
