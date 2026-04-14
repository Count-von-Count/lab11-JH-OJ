import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(9, 4), 13)
        
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(9, 4), 5)
        
    def test_multiply(self):
        self.assertEqual(mul(9, 0), 0)
        self.assertEqual(mul(-1, -1), 1)
        self.assertEqual(mul(9, 4), 36)

    def test_divide(self):
        self.assertEqual(div(1, -9), -9)
        self.assertEqual(div(-2, -8), 4)
        with self.assertRaises(ZeroDivisionError):
            div(0, 9)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(10, 1), 0)
        self.assertEqual(logarithm(3, 9), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 5)

    def test_log_invalid_argument(self):
       with self.assertRaises(ValueError):
           logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(-1, -1), 1.4142135623730951)
        self.assertAlmostEqual(hypotenuse(-1, 2), 2.23606797749979)
        self.assertAlmostEqual(hypotenuse(6, 3), 6.708203932499369)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)

        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(0), 0)

if __name__ == "__main__":
    unittest.main()
