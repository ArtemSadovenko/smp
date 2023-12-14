import unittest
from Calculator import Calculator  

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.calculate_result(5, '+', 3)
        self.assertEqual(result, 8)

    def test_addition2(self):
        result = self.calculator.calculate_result(-5, '+', -3)
        self.assertEqual(result, -8)

    def test_subtraction(self):
        result = self.calculator.calculate_result(8, '-', 3)
        self.assertEqual(result, 5)

    def test_subtraction2(self):
        result = self.calculator.calculate_result(-8, '-', 3)
        self.assertEqual(result, -11)

    def test_multiplication(self):
        result = self.calculator.calculate_result(4, '*', 2)
        self.assertEqual(result, 8)

    def test_division(self):
        result = self.calculator.calculate_result(8, '/', 2)
        self.assertEqual(result, 4)

    def test_division2(self):
        with self.assertRaises(ZeroDivisionError) as context:
            result = self.calculator.calculate_result(8, '/', 0)
        
        self.assertEqual(str(context.exception), "division by zero")
        

    def test_power(self):
        result = self.calculator.calculate_result(2, '^', 3)
        self.assertEqual(result, 8)

    def test_square_root(self):
        with self.assertRaises(ValueError) as context:
            result = self.calculator.calculate_result(-1, 'sqrt', 0)
        
        self.assertEqual(str(context.exception), "Square root of a negative number is undefined")

    def test_modulo(self):
        result = self.calculator.calculate_result(10, '%', 3)
        self.assertEqual(result, 1)

    def test_division_by_zero(self):
        result = self.calculator.calculate_result(5, '/', 0)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
