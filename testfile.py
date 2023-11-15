import unittest
from calculatorapp import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calculator = Calculator()
        result = calculator.add(2, 2)
        self.assertEqual(result, 4)

    def test_subtract(self):
        calculator = Calculator()
        result = calculator.subtract(5, 2)
        self.assertEqual(result, 3)

    def test_multiply(self):
        calculator = Calculator()
        result = calculator.multiply(5, 2)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
