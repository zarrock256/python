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