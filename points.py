import math
class Point:
    """Klasa reprezentująca punkty na płaszczyźnie. Współrzędne są całkowite"""

    def __init__(self, x, y):  # konstruktor
        self.x = x
        self.y = y

    def __str__(self):          # zwraca string "(x, y)"
        if isinstance(self.x,float) and isinstance(self.y,float):   #Dla klasy Rectangle, gdzie wyliczane współrzędne
            return "({0:.2f},{1:.2f})".format(self.x, self.y)       # środka mogą zawierać ułamek
        else:
            return "({0:d},{1:d})".format(self.x, self.y)


    def __repr__(self):         # zwraca string "Point(x, y)"
        return "Point({0:d},{1:d})".format(self.x, self.y)

    def __eq__(self, other):    # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):                  # v1 + v2   współrzędne wektorów będą dokładnie takie same jak współrzędne
        return Point(self.x + other.x, self.y + other.y)      #punktów, które są ich końcami (z uwagi na zaczepienie
                                                                #w punkcie (0,0)
    def __sub__(self, other):   # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny (liczba)
        return self.x*other.x + self.y*other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D (liczba)
        return self.x * other.y - self.y * other.x

    def length(self):           # długość wektora
        return math.sqrt(self.x*self.x + self.y*self.y)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points