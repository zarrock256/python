from points import Point

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):   # "[(x1, y1), (x2, y2)]"
        return "[({0:d}, {1:d}), ({2:d}, {3:d})]".format(self.pt1.x,self.pt1.y,self.pt2.x,self.pt2.y)

    def __repr__(self):   # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({0:d}, {1:d}, {2:d}, {3:d})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):   # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):  # obsługa rect1 != rect2
        return not self == other

    def center(self):   # zwraca środek prostokąta
        if (self.pt2.x - self.pt1.x) % 2 == 0 and (self.pt2.y - self.pt1.y)%2 == 0:
            return Point(self.pt1.x + (self.pt2.x - self.pt1.x)//2, self.pt1.y + (self.pt2.y - self.pt1.y)//2)
        else:
            return Point(self.pt1.x + (self.pt2.x - self.pt1.x) / 2, self.pt1.y + (self.pt2.y - self.pt1.y) / 2)

    def area(self):   # pole powierzchni
        return (self.pt2.x - self.pt1.x)*(self.pt2.y - self.pt1.y)

    def move(self, x, y):   # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        return self

    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        if x1 < x2 and y1 < y2:
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)
        else:
            raise ValueError("Najpierw wierzchołek w lewym dolnym rogu, a następnie prawy górny")

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        return "[({0:.2f}, {1:.2f}), ({2:.2f}, {3:.2f})]".format(self.pt1.x,self.pt1.y,self.pt2.x,self.pt2.y)

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({0:.2f}, {1:.2f}, {2:.2f}, {3:.2f})".format(self.pt1.x,self.pt1.y,self.pt2.x,self.pt2.y)

    def __eq__(self, other):    # obsługa rect1 == rect2
        if self.pt1 == other.pt1 and self.pt2 == other.pt2:
            return True
        return False

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        return Point(self.pt2.x - (self.pt2.x - self.pt1.x)/2,self.pt2.y - (self.pt2.y - self.pt1.y)/2)

    def area(self):             # pole powierzchni
        return (self.pt2.x - self.pt1.x)*(self.pt2.y - self.pt1.y)

    def move(self, x, y):       # przesunięcie o (x, y)
        return Rectangle(self.pt1.x+x,self.pt1.y+y,self.pt2.x+x,self.pt2.y+y)


    def intersection(self, other):  # część wspólna prostokątów
        x1 = max(self.pt1.x,other.pt1.x)
        y1 = max(self.pt1.y,other.pt1.y)
        x2 = min(self.pt2.x,other.pt2.x)
        y2 = min(self.pt2.y,other.pt2.y)
        return Rectangle(x1,y1,x2,y2)

    def cover(self, other):     # prostąkąt nakrywający oba
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1,y1,x2,y2)

    def make4(self):            # zwraca krotkę czterech mniejszych
        rec1 = Rectangle(self.pt1.x,self.pt1.y,self.center().x, self.center().y)
        rec2 = Rectangle(self.center().x,self.center().y,self.pt2.x,self.pt2.y)
        rec3 = Rectangle(self.pt1.x,self.center().y,self.center().x,self.pt2.y)
        rec4 = Rectangle(self.center().x,self.pt1.y,self.pt2.x,self.center().y)
        return (rec1,rec2,rec3,rec4)

