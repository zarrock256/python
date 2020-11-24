#W pliku rectangles.py zdefiniować klasę Rectangle wraz z potrzebnymi metodami. Prostokąt jest określony przez podanie
# dwóch wierzchołków, lewego dolnego i prawego górnego. Napisać kod testujący moduł rectangles.

from rectangles import *
import unittest
import math

class TestTime(unittest.TestCase):

    def testPrint(self):
        self.assertEqual(Rectangle(0,0,1,1).__str__(),"[(0, 0), (1, 1)]")
        self.assertEqual(Rectangle(-5,10,0,-2).__str__(),"[(-5, 10), (0, -2)]")
        self.assertEqual(Rectangle(0, 0, 1, 1).__repr__(), "Rectangle(0, 0, 1, 1)")
        self.assertEqual(Rectangle(-5,10,0,-2).__repr__(),"Rectangle(-5, 10, 0, -2)")

    def test_cmp(self):
        self.assertTrue(Rectangle(1,1,2,2) == Rectangle(1,1,2,2))
        self.assertFalse(Rectangle(1,1,2,2) == Rectangle(1,0,2,2))
        self.assertFalse(Rectangle(1,1,2,2) != Rectangle(1,1,2,2))
        self.assertTrue(Rectangle(1,1,2,2) != Rectangle(0,1,2,2))

    def test_center(self):
        self.assertEqual(Rectangle(0,0,2,2).center(),Point(1,1))
        self.assertEqual(Rectangle(0,0,1,1).center(),Point(0.5,0.5))
        self.assertEqual(Rectangle(0,0,0,0).center(),Point(0,0))
        self.assertEqual(Rectangle(-2,-2,2,2).center(),Point(0,0))

    def test_area(self):
        self.assertEqual(Rectangle(0,0,1,1).area(),1)
        self.assertEqual(Rectangle(0,0,0,0).area(),0)
        self.assertEqual(Rectangle(-1,-1,1,1).area(),4)
        self.assertEqual(Rectangle(-1,-3,3,1).area(),16)

    def test_move(self):
        self.assertEqual(Rectangle(0,0,1,1).move(1,1),Rectangle(1,1,2,2))
        self.assertEqual(Rectangle(0,0,0,0).move(-2,-2),Rectangle(-2,-2,-2,-2))
        self.assertEqual(Rectangle(-1,-2,-3,-4).move(1,1),Rectangle(0,0-1,-2,-3))
        self.assertEqual(Rectangle(-1,-2,-3,-4).move(-1,-1),Rectangle(-2,-3,-4,-5))

if __name__ == "__main__":
        unittest.main()  # wszystkie testy
