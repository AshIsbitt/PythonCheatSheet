import unittest
import calc

# Creating test cases
# We need to create a class to inheret from unittest.TestCase

class TestCalc(unittest.TestCase):

    # testing methods have to start with "test_" so unittest knows to run them
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)

    # Despite multiple lines, this only counts as one test
    def test_add_two(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract_two(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), -0)

    def test_multiply_two(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide_two(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # Testing raising errors
        # args: exception, function without parameters, then parameters
        # self.assertRaises(ValueError, calc.divide, 10, 0)

        # A better way to do the above
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
