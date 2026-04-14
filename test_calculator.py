import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4, 4), 8)
        self.assertEqual(add(0, 9), 9)
        self.assertEqual(add(a=-3, b=8), 5)

    def test_subtract(self):
        self.assertEqual(subtract(4, 4), 0)
        self.assertEqual(subtract(9, 3), 6)
        self.assertEqual(subtract(3, 9), -6)

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(9, 0), 0)
        self.assertEqual(mul(1, 1), 1)
        self.assertEqual(mul(9, 4), 36)

    def test_divide(self):
        self.assertEqual(div(a=-1, b=9), -9)
        self.assertEqual(div(2, 8), 4)
        self.assertEqual(div(3, 9), 3)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 8)

    def test_logarithm(self):
        self.assertEqual(logarithm(2, 4), 2)
        self.assertEqual(logarithm(2, 0.5), -1)
        self.assertEqual(logarithm(10, 100), 2)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(10, 0)

    ######## Partner 1
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(a=-1, b=-1), 1.4142135623730951)
        self.assertAlmostEqual(hypotenuse(a=-1, b=2), 2.23606797749979)
        self.assertAlmostEqual(hypotenuse(6, 3), 6.708203932499369)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(0), 0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()