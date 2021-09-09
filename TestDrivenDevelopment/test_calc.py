import unittest
import calc

# Creating test cases
# We need to create a class to inheret from unittest.TestCase

class TestCalc(unittest.TestCase):

    # testing methods have to start with "test_" so unittest knows to run them
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()
