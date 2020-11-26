#W pliku rectangles.py zdefiniować klasę Rectangle wraz z potrzebnymi metodami. Wykorzystać wyjątek ValueError do
# obsługi błędów. Napisać kod testujący moduł rectangles.

from rectangles import Rectangle
from points import Point
import unittest
import math

class TestRectangle(unittest.TestCase):
    def test_print(self):
        self.assertEqual(str(Rectangle(1,1,2,2)),"[(1.00, 1.00), (2.00, 2.00)]")
        self.assertEqual(repr(Rectangle(1,1,2,2)),"Rectangle(1.00, 1.00, 2.00, 2.00)")

    def test_eq(self):
        self.assertTrue(Rectangle(1,1,4,4) == Rectangle(1,1,4,4))
        self.assertFalse(Rectangle(1,1,4,4) == Rectangle(0,1,4,4))
        self.assertFalse(Rectangle(1,1,4,4) != Rectangle(1,1,4,4))
        self.assertTrue(Rectangle(1,1,4,4) != Rectangle(3,1,4,4))


    def test_center(self):
        self.assertEqual(Rectangle(0,0,2,2).center(),Point(1,1))
        self.assertEqual(Rectangle(-2,-2,2,2).center(),Point(0,0))

    def test_area(self):
        self.assertEqual(Rectangle(0,0,2,2).area(),4)
        self.assertEqual(Rectangle(0,0,1,1).area(),1)

    def test_move(self):
        self.assertEqual(Rectangle(0,0,2,2).move(2,2),Rectangle(2,2,4,4))
        self.assertEqual(Rectangle(0,0,2,2).move(-2,-2),Rectangle(-2,-2,0,0))

    def test_intersection(self):
        self.assertEqual(Rectangle(0,0,2,2).intersection(Rectangle(1,1,2,2)),Rectangle(1,1,2,2))
        self.assertEqual(Rectangle(0,0,2,2).intersection(Rectangle(0,0,2,2)),Rectangle(0,0,2,2))
        self.assertEqual(Rectangle(0,0,4,4).intersection(Rectangle(2,2,6,6)),Rectangle(2,2,4,4))
        self.assertEqual(Rectangle(0,0,4,4).intersection(Rectangle(1,1,7,3)),Rectangle(1,1,4,3))

    def test_cover(self):
        self.assertEqual(Rectangle(0,0,2,2).cover(Rectangle(4,4,8,8)),Rectangle(0,0,8,8))
        self.assertEqual(Rectangle(-1,-2,2,2).cover(Rectangle(4,4,8,8)),Rectangle(-1,-2,8,8))
        self.assertEqual(Rectangle(1,1,2,2).cover(Rectangle(4,4,16,10)),Rectangle(1,1,16,10))

    def test_make4(self):
        self.assertEqual(Rectangle(0,0,1,1).make4(),(Rectangle(0,0,0.5,0.5),Rectangle(0.5,0.5,1,1),Rectangle(0,0.5,0.5,1),Rectangle(0.5,0,1,0.5)))
        self.assertEqual(Rectangle(-1,-1,1,1).make4(),(Rectangle(-1,-1,0,0),Rectangle(0,0,1,1),Rectangle(-1,0,0,1),Rectangle(0,-1,1,0)))


if __name__ == "__main__":
    unittest.main()  # wszystkie testy





