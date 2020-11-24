#W pliku points.py zdefiniować klasę Point wraz z potrzebnymi metodami. Punkty są traktowane jak wektory zaczepione w
#początku układu współrzędnych, o końcu w położeniu (x, y). Napisać kod testujący moduł points.

from points import Point
import unittest
import math

class TestTime(unittest.TestCase):
    def setUp(self):
        self.x = 0
        self.y = 0

    def testPrint(self):
        self.assertEqual(Point(1, 2).__repr__(), 'Point(1,2)')
        self.assertEqual(Point(1, 2).__str__(), '(1,2)')
        self.assertEqual(Point(-1, 0).__str__(), '(-1,0)')
        self.assertEqual(Point(-1, 0).__repr__(), 'Point(-1,0)')
        self.assertEqual(Point(0, 0).__repr__(), 'Point(0,0)')

    def test_cmp(self):
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertFalse(Point(1, 2) == Point(1, 3))
        self.assertFalse(Point(1, 2) != Point(1, 2))
        self.assertTrue(Point(1, 2) != Point(1, 3))

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(3, 4), Point(4, 6))
        self.assertEqual(Point(-1, -2) + Point(3, 4), Point(2, 2))
        self.assertEqual(Point(0, 0) + Point(2, 2), Point(2, 2))

    def test_sub(self):
        self.assertEqual(Point(1, 2) - Point(3, 4), Point(-2, -2))
        self.assertEqual(Point(-1, -2) - Point(3, 4), Point(-4, -6))
        self.assertEqual(Point(0, 0) - Point(2, 2), Point(-2, -2))

    def test_mul(self):
        self.assertEqual(Point(1,2)*Point(3,4),11)
        self.assertEqual(Point(-1,-2)*Point(3,4),-11)
        self.assertEqual(Point(0,0)*Point(3,4),0)

    def test_cross(self):
        self.assertEqual(Point(1,2).cross(Point(1,2)),0)
        self.assertEqual(Point(-1,-2).cross(Point(1,2)),0)
        self.assertEqual(Point(-1,2).cross(Point(1,2)),-4)
        self.assertEqual(Point(0,0).cross(Point(1,2)),0)
        self.assertEqual(Point(2,4).cross(Point(1,2)),0)

    def test_length(self):
        self.assertEqual(Point(3,0).length(),3)
        self.assertEqual(Point(5,4).length(),math.sqrt(5*5+4*4))
        self.assertEqual(Point(-2,-5).length(),math.sqrt(math.pow(-2,2)+math.pow(-5,2)))


if __name__ == "__main__":
    unittest.main()     # wszystkie testy