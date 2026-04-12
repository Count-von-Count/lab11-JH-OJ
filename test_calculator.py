import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code
    def test_multiply(self):
        self.assertEqual(multiply(9, 0), 0)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(9, 4), 36)

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################
    def test_divide(self):
        self.assertEqual(divide(-9,1), -9)
        self.assertEqual(divide(-8, -2), 4)
        self.assertEqual(divide(9, 0), ZeroDivisionError)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################

    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
    def test_log_invalid_argument(self):
       with self.assertRaises(ValueError):
           logarithm(0, 5),

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code
    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(-1, -1), 1.4142135623730950488016887242097)
        self.assertAlmostEqual(hypotenuse(-1, 2), 1.7320508075688772935274463415059)
        self.assertAlmostEqual(hypotenuse(6, 3),6.7082039324993690892275210061938)
    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################
    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)

        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(0), 0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()