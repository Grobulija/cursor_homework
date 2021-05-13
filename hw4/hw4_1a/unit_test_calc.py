import unittest
from functions_to_test import Calculator


class UTestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(0, 0), 0)
        self.assertEqual(Calculator.add(1, -2), -1)
        self.assertEqual(Calculator.add(6.3, 4.4), 10.7)
        self.assertRaises(TypeError, Calculator.add, 4, "5")
        self.assertRaises(TypeError, Calculator.add, "something", 0)
        self.assertRaises(TypeError, Calculator.add, {1}, [5])

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(0, 0), 0)
        self.assertEqual(Calculator.subtract(1, -2), 3)
        self.assertEqual(Calculator.subtract(6.5, 3.25), 3.25)
        self.assertRaises(TypeError, Calculator.subtract, 4, "5")
        self.assertRaises(TypeError, Calculator.subtract, "something", 0)
        self.assertRaises(TypeError, Calculator.subtract, {1}, [5])

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(0, 0), 0)
        self.assertEqual(Calculator.multiply(1, -2), -2)
        self.assertEqual(Calculator.multiply(6.5, 3.25), 21.125)
        self.assertRaises(TypeError, Calculator.multiply, {1}, [5])

    def test_divide(self):
        self.assertEqual(Calculator.divide(1, 1), 1)
        self.assertEqual(Calculator.divide(1, -2), -0.5)
        self.assertEqual(Calculator.divide(6.3, 4.2), 1.5)
        self.assertRaises(TypeError, Calculator.divide, 4, "5")
        self.assertRaises(TypeError, Calculator.divide, "something", 1)
        self.assertRaises(TypeError, Calculator.divide, {1}, [5])


if __name__ == "main":
    unittest.main()
