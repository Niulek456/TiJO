import unittest
from quadratic_equation import QuadraticEquation

class QuadraticEquationTestCase(unittest.TestCase):
    def test_raise_error_when_a_is_zero(self):
        a, b, c = 0, 2, 4

        self.asserrtRaises(ValueError, QuadraticEquation, a, b, c)


if __name__ == "__main__":
    unittest.main()