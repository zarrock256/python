import math

def shorter(result):                #sprowadza ułamek do prostszej postaci
    if result[0]%result[1] == 0:
        return [result[0]//result[1],1]
    temp = result[0]
    result[0] //= math.gcd(result[0],result[1])
    result[1] //= math.gcd(temp,result[1])
    return result

def add_frac(frac1, frac2):         # frac1 + frac2
    result = [frac1[0] * frac2[1] + frac1[1] * frac2[0], frac1[1] * frac2[1]]
    return shorter(result)

def sub_frac(frac1, frac2):       # frac1 - frac2
    result = [frac1[0] * frac2[1] - frac1[1] * frac2[0], frac1[1] * frac2[1]]
    return shorter(result)

def mul_frac(frac1, frac2):      # frac1 * frac2
    result = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
    return shorter(result)

def div_frac(frac1, frac2):        # frac1 / frac2
    temp = frac1[0]
    frac1[0] = frac1[1]
    frac1[1] = temp
    result = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
    return shorter(result)

def is_positive(frac):              # bool, czy dodatni
    if frac[0] > 0 and frac[1] > 0:     #Zakładam, że zero nie jest dodatnie
        return True
    elif frac[0] < 0 and frac[1] < 0:
        return True
    return False

def is_zero(frac):               # bool, typu [0, x]
    if frac[0] == 0:
        return True
    return False

def cmp_frac(frac1, frac2):        #porównuje ułamki: -1 | 0 | +1
    if frac1 == frac2:
        return 0
    temp = frac1[1]
    frac1[0] *= frac2[1]
    frac1[1] *= frac2[1]
    frac2[0] *= temp
    if frac1[0] < frac2[0]:
        return -1
    if frac1[0] == frac2[0]:
        return 0
    return 1

def frac2float(frac):               # konwersja do float
    return float(frac[0]/frac[1])

class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        if y == 0:
            raise ValueError("Mianownik nie może być zerem!")
        divisor = math.gcd(x, y)    #Uproszczenie ułamka
        self.x = x//divisor
        self.y = y//divisor
        if x == 0:
            self.y //= self.y       #jeśli licznik jest zerem, to mianownik jest ustawiam na 1, żeby łatwiej porównywać ułamki,
        if self.x < 0 and self.y < 0 or self.x > 0 and self.y < 0:
            self.x *= -1
            self.y *= -1



    def __str__(self):          # zwraca "x/y" lub "x" dla y=1
        if self.y != 1:
            return "{0:d}/{1:d}".format(self.x,self.y)
        else:
            return "{0:d}".format(self.x)

    def __repr__(self):         # zwraca "Frac(x, y)"
        return "Frac({0:d}, {1:d})".format(self.x, self.y)

    # Python 2
    # def __cmp__(self, other):   # cmp(frac1, frac2)
    #     if self == other:
    #         return 0
    #     temp = self.y
    #     self.x *= other.y
    #     self.y *= other.y
    #     other.x *= temp
    #     if self.x < other.x:
    #         return -1
    #     if self.x == other.x:
    #         return 0
    #     return 1

    # Python 2.7 i Python 3
    def __eq__(self, other):        #Można porównywać ułamki Frac z intami i floatami
        if isinstance(other,Frac):
            if self.x == other.x and self.y == other.y:
                return True
            return False
        if isinstance(other,int):
            if self.y == 1 and self.x == other:
                return True
            return False
        if isinstance(other,float):
            otherFrac = Frac(other.as_integer_ratio()[0],other.as_integer_ratio()[1])
            if self.x == otherFrac.x and self.y == otherFrac.y:
                return True
            return False

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other, Frac):
            if self.x * other.y < self.y * other.x:
                return True
            return False
        if isinstance(other, int):
            if self.x/self.y < other:
                return True
            return False
        if isinstance(other, float):
            otherFrac = Frac(other.as_integer_ratio()[0], other.as_integer_ratio()[1])
            if self < otherFrac:
                return True
            return False

    def __le__(self, other):
        if isinstance(other, Frac):
            if self.x * other.y <= self.y * other.x:
                return True
            return False
        if isinstance(other, int):
            if self.x / self.y <= other:
                return True
            return False
        if isinstance(other, float):
            otherFrac = Frac(other.as_integer_ratio()[0], other.as_integer_ratio()[1])
            if self <= otherFrac:
                return True
            return False

    def __gt__(self, other):
        if isinstance(other, Frac):
            if self.x * other.y > self.y * other.x:
                return True
            return False
        if isinstance(other, int):
            if self.x / self.y > other:
                return True
            return False
        if isinstance(other, float):
            otherFrac = Frac(other.as_integer_ratio()[0], other.as_integer_ratio()[1])
            if self > otherFrac:
                return True
            return False

    def __ge__(self, other):
        if isinstance(other, Frac):
            if self.x * other.y >= self.y * other.x:
                return True
            return False
        if isinstance(other, int):
            if self.x / self.y >= other:
                return True
            return False
        if isinstance(other, float):
            otherFrac = Frac(other.as_integer_ratio()[0], other.as_integer_ratio()[1])
            if self >= otherFrac:
                return True
            return False

    def __add__(self, other):   # frac1+frac2, frac+int
        if isinstance(other,Frac):
            return Frac(self.x*other.y + other.x*self.y,self.y*other.y)
        if isinstance(other, int):
            return Frac(self.x + other*self.y, self.y)
        if isinstance(other,float):
            otherFrac = Frac(other.as_integer_ratio()[0],other.as_integer_ratio()[1])
            return self+otherFrac

    __radd__ = __add__              # int+frac

    def __sub__(self, other):   # frac1-frac2, frac-int
        if isinstance(other,Frac):
            return Frac(self.x*other.y - other.x*self.y,self.y*other.y)
        if isinstance(other, int):
            return Frac(self.x - other*self.y, self.y)
        if isinstance(other,float):
            otherFrac = Frac(other.as_integer_ratio()[0],other.as_integer_ratio()[1])
            return self-otherFrac

    def __rsub__(self, other):      # int-frac
        if isinstance(other, int):
            return Frac(other * self.y - self.x, self.y)
        if isinstance(other, float):
            otherFrac = Frac(other.as_integer_ratio()[0], other.as_integer_ratio()[1])
            return otherFrac - self

    def __mul__(self, other):   # frac1*frac2, frac*int
        if isinstance(other,Frac):
            return Frac(self.x*other.x,self.y*other.y)
        if isinstance(other, int):
            return Frac(self.x*other, self.y)
        if isinstance(other,float):
            otherFrac = Frac(other.as_integer_ratio()[0],other.as_integer_ratio()[1])
            return otherFrac*self

    __rmul__ = __mul__              # int*frac, float*int

    def __truediv__(self, other):   # frac1/frac2, frac/int, Python 3
        if isinstance(other,Frac):
            try:
                return Frac(self.x*other.y,self.y*other.x)
            except ValueError:
                print("Nie dzielimy przez zero!")
        if isinstance(other, int):
            try:
                return Frac(self.x, self.y*other)
            except ValueError:
                print("Nie dzielimy przez zero!")
        if isinstance(other,float):
            otherFrac = Frac(other.as_integer_ratio()[0],other.as_integer_ratio()[1])
            try:
                return Frac(self.x*otherFrac.y,self.y*otherFrac.x)
            except ValueError:
                print("Nie dzielimy przez zero!")

    def __rtruediv__(self, other):   # int/frac, float/frac Python 3
        if isinstance(other, int):
            try:
                return Frac(other*self.y, self.x)
            except ValueError:
                print("Nie dzielimy przez zero!")
        if isinstance(other, float):
            otherFrac = Frac(other.as_integer_ratio()[0], other.as_integer_ratio()[1])
            try:
                return otherFrac/self
            except ValueError:
                print("Nie dzielimy przez zero!")

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):          # -frac = (-1)*frac
        return Frac(self.x*(-1),self.y)

    def __invert__(self):       # odwrotnosc: ~frac
        return Frac(self.y,self.x)

    def __float__(self):        # float(frac)
        return float(self.x/self.y)

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # assert set([2]) == set([2.0])

