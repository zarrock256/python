#Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach. Ułamek będzie reprezentowany przez listę
# dwóch liczb całkowitych [licznik, mianownik]. Napisać kod testujący moduł fracs. Nie należy korzystać z klasy
# Fraction z modułu fractions. Można wykorzystać funkcję fractions.gcd() implementującą algorytm Euklidesa.

import unittest
from fracs import *

class Testfracs(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [2, 3])

    def test_is_positive(self):
        self.assertEqual(is_positive([-1,2]),False)
        self.assertEqual(is_positive([1,2]),True)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 2]), True)
        self.assertEqual(is_zero([1, 2]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 6], [1, 3]), -1)
        self.assertEqual(cmp_frac([1, 6], [1, 6]), 0)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([3, 6]), 0.5)
        self.assertEqual(frac2float([-5, 2]), -2.5)
        self.assertEqual(frac2float([0, 2]), 0)

    def test_shorter(self):
        self.assertEqual(shorter([5,10]),[1,2])
        self.assertEqual(shorter([3,9]),[1,3])
        self.assertEqual(shorter([5,25]),[1,5])
        self.assertEqual(shorter([0,25]),0)

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy