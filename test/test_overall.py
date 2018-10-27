"""
Tests for main pycalc function
"""
import unittest
from math import *
import sys

sys.path.append("../")
try:
    import pycalc
except Exception:
    raise


class OverallTests(unittest.TestCase):
    """
    Tests evaluating real math string expressions
    """
    def test_unary_operators(self):
        """
        unary operators
        """
        self.assertEqual(pycalc.evaluate_string_expression("-13", []), -13)
        self.assertEqual(pycalc.evaluate_string_expression("6-(-13)", []), 6 - (-13))
        self.assertEqual(pycalc.evaluate_string_expression("1---1", []), 1 - --1)
        self.assertEqual(pycalc.evaluate_string_expression("-+---+-1", []), -+---+-1)

    def test_operation_priority(self):
        """
        priority of operations in expression
        """
        self.assertEqual(pycalc.evaluate_string_expression("1+2*2", []), 1 + 2 * 2)
        self.assertEqual(pycalc.evaluate_string_expression("1+(2+3*2)*3", []), 1 + (2 + 3 * 2) * 3)
        self.assertEqual(pycalc.evaluate_string_expression("10*(2+1)", []), 10 * (2 + 1))
        self.assertEqual(pycalc.evaluate_string_expression("10^(2+1)", []), 10 ** (2 + 1))
        self.assertEqual(pycalc.evaluate_string_expression("100/3^2", []), 100 / 3 ** 2)
        self.assertEqual(pycalc.evaluate_string_expression("100/3%2^2", []), 100 / 3 % 2 ** 2)

    def test_functions_and_constants(self):
        """
        functions and constants are recognized by pycalc
        """
        self.assertEqual(pycalc.evaluate_string_expression("pi+e", []), pi + e)
        self.assertEqual(pycalc.evaluate_string_expression("log(e)", []), log(e))
        self.assertEqual(pycalc.evaluate_string_expression("sin(pi/2)", []), sin(pi / 2))
        self.assertEqual(pycalc.evaluate_string_expression("log10(100)", []), log10(100))
        self.assertEqual(pycalc.evaluate_string_expression("sin(pi/2)*111*6", []), sin(pi / 2) * 111 * 6)
        self.assertEqual(pycalc.evaluate_string_expression("2*sin(pi/2)", []), 2 * sin(pi / 2))

    def test_associative(self):
        """
        left and right associative
        """
        self.assertEqual(pycalc.evaluate_string_expression("102%12%7", []), 102 % 12 % 7)
        self.assertEqual(pycalc.evaluate_string_expression("100/4/3", []), 100 / 4 / 3)
        self.assertEqual(pycalc.evaluate_string_expression("2^3^4", []), 2 ** 3 ** 4)

    def test_comparison_operators(self):
        """
        logical operators
        """
        self.assertEqual(pycalc.evaluate_string_expression("1+2*3==1+2*3", []), 1 + 2 * 3 == 1 + 2 * 3)
        self.assertEqual(pycalc.evaluate_string_expression("e^5>=e^5+1", []), e ** 5 >= e ** 5 + 1)
        self.assertEqual(pycalc.evaluate_string_expression("1+2*4/3+1!=1+2*4/3+2", []),
                         1 + 2 * 4 / 3 + 1 != 1 + 2 * 4 / 3 + 2)

    def test_common(self):
        """
        other tests
        """
        self.assertEqual(pycalc.evaluate_string_expression("(100)", []), (100))
        self.assertEqual(pycalc.evaluate_string_expression("666", []), 666)
        self.assertEqual(pycalc.evaluate_string_expression("10(2+1)", []), 10 * (2 + 1))
        self.assertEqual(pycalc.evaluate_string_expression("-.1", []), -.1)
        self.assertEqual(pycalc.evaluate_string_expression("1/3", []), 1 / 3)
        self.assertEqual(pycalc.evaluate_string_expression("1.0/3.0", []), 1.0 / 3.0)
        self.assertEqual(pycalc.evaluate_string_expression(".1 * 2.0^56.0", []), .1 * 2.0 ** 56.0)
        self.assertEqual(pycalc.evaluate_string_expression("e^34", []), e ** 34)
        self.assertEqual(pycalc.evaluate_string_expression("(2.0^(pi/pi+e/e+2.0^0.0))", []),
                         (2.0 ** (pi / pi + e / e + 2.0 ** 0.0)))
        self.assertEqual(pycalc.evaluate_string_expression("(2.0^(pi/pi+e/e+2.0^0.0))^(1.0/3.0)", []),
                         (2.0 ** (pi / pi + e / e + 2.0 ** 0.0)) ** (1.0 / 3.0))
        self.assertEqual(pycalc.evaluate_string_expression("sin(pi/2^1) + log(1*4+2^2+1, 3^2)", []),
                         sin(pi / 2 ** 1) + log(1 * 4 + 2 ** 2 + 1, 3 ** 2))
        self.assertEqual(pycalc.evaluate_string_expression("10*e^0*log10(.4 -5/ -0.1-10) - -abs(-53/10) + -5", []),
                         10 * e ** 0 * log10(.4 - 5 / -0.1 - 10) - -abs(-53 / 10) + -5)
        self.assertEqual(pycalc.evaluate_string_expression(
            "sin(-cos(-sin(3.0)-cos(-sin(-3.0*5.0)-sin(cos(log10(43.0))))" +
            "+cos(sin(sin(34.0-2.0^2.0))))--cos(1.0)--cos(0.0)^3.0)",
            []), sin(
            -cos(-sin(3.0) - cos(-sin(-3.0 * 5.0) - sin(cos(log10(43.0)))) + cos(sin(sin(34.0 - 2.0 ** 2.0)))) - -cos(
                1.0) - -cos(0.0) ** 3.0))
        self.assertEqual(pycalc.evaluate_string_expression("2.0^(2.0^2.0*2.0^2.0)", []),
                         2.0 ** (2.0 ** 2.0 * 2.0 ** 2.0))
        self.assertEqual(pycalc.evaluate_string_expression("sin(e^log(e^e^sin(23.0),45.0) + cos(3.0+log10(e^-e)))", []),
                         sin(e ** log(e ** e ** sin(23.0), 45.0) + cos(3.0 + log10(e ** -e))))

    def test_error(self):
        """
        error cases when the exception is thrown
        """
        self.assertRaises(Exception, pycalc.evaluate_string_expression, "", [])
        self.assertRaises(Exception, pycalc.evaluate_string_expression, "+", [])
        self.assertRaises(Exception, pycalc.evaluate_string_expression, "1-", [])
        self.assertRaises(Exception, pycalc.evaluate_string_expression, "1 2", [])
        self.assertRaises(Exception, pycalc.evaluate_string_expression, "ee", [])
        self.assertRaises(Exception, pycalc.evaluate_string_expression, "==7", [])
        self.assertRaises(Exception, pycalc.evaluate_string_expression, "1 + 2(3 * 4))", [])
        self.assertRaises(Exception, pycalc.evaluate_string_expression, "((1+2)", [])
        self.assertRaises(Exception, pycalc.evaluate_string_expression, "1 + 1 2 3 4 5 6 ", [])
        self.assertRaises(Exception, pycalc.evaluate_string_expression, "log100(100)", [])
        self.assertRaises(Exception, pycalc.evaluate_string_expression, "------", [])
        self.assertRaises(Exception, pycalc.evaluate_string_expression, "5 > = 6", [])
        self.assertRaises(Exception, pycalc.evaluate_string_expression, "5 / / 6", [])
        self.assertRaises(Exception, pycalc.evaluate_string_expression, "6 < = 6", [])
        self.assertRaises(Exception, pycalc.evaluate_string_expression, "6 * * 6", [])
        self.assertRaises(Exception, pycalc.evaluate_string_expression, "(((((", [])


if __name__ == "__main__":
    unittest.main()
