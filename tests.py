#Importing module and Calculator class
import unittest
from Calculator import Calculator

#CalculatorTest class to test the calculator functions
class CalculatorTest(unittest.TestCase):

    #Set up function to create an instance of the Calculator
    def setUp(self):
        self.calc = Calculator()
        
    #Addition test
    def test_add(self):
        self.assertEqual(self.calc.Add(5, 5), 10)

    #Division test
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.Divide(10, 0)


if __name__ == "__main__":
    unittest.main()