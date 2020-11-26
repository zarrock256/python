#W pliku fracs.py zdefiniować klasę Frac wraz z potrzebnymi metodami. Wykorzystać wyjątek ValueError do obsługi
#błędów w ułamkach. Dodać możliwości dodawania liczb (int, long) do ułamków (działania lewostronne i prawostronne).
#Rozważyć możliwość włączenia liczb float do działań na ułamkach [Wskazówka: metoda float.as_integer_ratio()].
#Napisać kod testujący moduł fracs.

from fracs import Frac
import unittest

class TestFrac(unittest.TestCase):
    def test_print(self):
        self.assertEqual(str(Frac(1,1)),"1")
        self.assertEqual(str(Frac(1,2)),"1/2")
        self.assertEqual(str(Frac(-1,2)),"-1/2")
        self.assertEqual(str(Frac(-1,-2)),"1/2") #Dwa minusy zamieniam w plusa
        self.assertEqual(str(Frac(0,1)),"0")

        self.assertEqual(repr(Frac(1, 1)), "Frac(1, 1)")
        self.assertEqual(repr(Frac(1, 2)), "Frac(1, 2)")
        self.assertEqual(repr(Frac(-1, 2)), "Frac(-1, 2)")
        self.assertEqual(repr(Frac(-1, -2)), "Frac(1, 2)") #Dwa minusy zamieniam w plusa
        self.assertEqual(repr(Frac(0, 1)), "Frac(0, 1)")


    def test_cmp(self):
        result = [Frac(1, 2), Frac(5, 4), Frac(1, 4), Frac(-1, 2), Frac(0, 1)]                 #Sortowanie
        result.sort()                                                                          #Sortowanie
        self.assertEqual(result,[Frac(-1, 2), Frac(0, 1), Frac(1, 4), Frac(1, 2), Frac(5, 4)]) #Sortowanie
        self.assertTrue(Frac(4,12) == Frac(1,3))                                                #Można porównywać zarówno
        self.assertTrue(Frac(-4,12) == Frac(1,-3))                                              #z int jak i float
        self.assertTrue(Frac(0,12) == 0)
        self.assertTrue(0 == Frac(0,12))
        self.assertTrue(Frac(-4,12) == Frac(1,-3))
        self.assertTrue(Frac(4,2) == 2)
        self.assertTrue(Frac(1,12) > Frac(1,-3))
        self.assertTrue(Frac(2,12) > Frac(2,16))
        self.assertFalse(Frac(1,12) < Frac(1,-3))
        self.assertTrue(Frac(1,12) >= Frac(1,-3))
        self.assertFalse(Frac(1,12) <= Frac(1,-3))
        self.assertTrue(Frac(0,12) >= Frac(1,-3))
        self.assertTrue(Frac(0,12) <= Frac(-1,-3))
        self.assertTrue(Frac(0,12) != Frac(-1,-3))
        self.assertFalse(Frac(0,12) != Frac(0,-3))
        self.assertTrue(Frac(1,2) == 0.5)
        self.assertTrue(Frac(1,2) >= 0.5)
        self.assertFalse(Frac(1,2) < 0.5)
        self.assertTrue(Frac(1,2) < 1)
        self.assertTrue(Frac(1,2) > 0)

    def test_add(self):
        self.assertEqual(Frac(1,2)+Frac(-1,2),Frac(0,1))
        self.assertEqual(Frac(1,2) + 1,Frac(3,2))
        self.assertEqual(1 + Frac(1,2),Frac(3,2))
        self.assertEqual(Frac(-1,2)+1,Frac(1,2))
        self.assertEqual(-1 + Frac(-1,2),Frac(-3,2))
        self.assertEqual(Frac(1,2)+Frac(1,4),Frac(3,4))
        self.assertEqual(Frac(1,2)+2.5,3.0)
        self.assertEqual(2.5+Frac(1,2),3.0)
        self.assertEqual(2.2+Frac(5,10),2.7)

    def test_sub(self):
        self.assertEqual(Frac(1,2)-Frac(1,2),Frac(0,4))
        self.assertEqual(Frac(1,2)-1,Frac(1,-2))
        self.assertEqual(1-Frac(1,2),Frac(2,4))
        self.assertEqual(0.5-Frac(1,2),0)
        self.assertEqual(Frac(1,2)-1.5,Frac(-1,1))

    def test_mul(self):
        self.assertEqual(Frac(1,2)*Frac(1,2),Frac(1,4))
        self.assertEqual(Frac(-1,2)*Frac(1,2),Frac(1,-4))
        self.assertEqual(Frac(0,2)*Frac(1,2),0)
        self.assertEqual(Frac(1,2)*2,1)
        self.assertEqual((-2)*Frac(1,2),-1)
        self.assertEqual(Frac(1,2)*0.5,Frac(1,4))
        self.assertEqual(0.5*Frac(1,2),Frac(1,4))
        self.assertEqual(0.4*Frac(2,1),0.8)
        self.assertEqual(Frac(2,1)*0.2,0.4)
        self.assertEqual(Frac(1,4)*0.5,Frac(1,8))

    def test_div(self):
        self.assertEqual(Frac(1,2)/2,Frac(1,4))
        self.assertEqual(Frac(1,2)/Frac(1,2),1)
        self.assertEqual(Frac(1,2)/Frac(-1,2),-1)
        self.assertEqual(2/Frac(-1,2),-4)
        self.assertEqual(2/Frac(3,2),Frac(4,3))
        self.assertEqual(Frac(3,2)/2,Frac(3,4))
        self.assertEqual(2.5/Frac(1,2),5)
        self.assertEqual(Frac(1,2)/2.5,Frac(1,5))

    def test_pos_neg(self):
        self.assertEqual(+Frac(1,2), Frac(1,2))
        self.assertEqual(-Frac(1,2), Frac(-1,2))
        self.assertEqual(-Frac(1,2), +Frac(-1,2))
        self.assertEqual(-Frac(0,2), 0)

    def test_invert(self):
        self.assertEqual(~Frac(1,2),2)
        self.assertEqual(~Frac(4,5),Frac(5,4))
        self.assertEqual(~Frac(4,-5),Frac(-5,4))

    def test_float(self):
        self.assertEqual(float(Frac(1,2)),0.5)
        self.assertEqual(float(Frac(0,2)),0.0)
        self.assertEqual(float(Frac(-1,5)),-0.2)
        self.assertEqual(float(Frac(7,10)),0.7)

if __name__ == "__main__":
    unittest.main()  # wszystkie testy





