"""
Tests for common_utils.py
"""
import unittest
import sys

sys.path.append("../")
from utils.common_utils import *


class TryToIntTests(unittest.TestCase):
    """
    Tests for try_to_int function
    """
    def test_int(self):
        """
        with integer
        """
        self.assertEqual(try_to_int(5), 5)
        self.assertEqual(try_to_int(0), 0)
        self.assertEqual(try_to_int(-5), -5)

    def test_float(self):
        """
        with float
        """
        self.assertEqual(try_to_int(5.5), 5.5)
        self.assertEqual(try_to_int(-5.5), -5.5)

    def test_string_int(self):
        """
        string to int conversion
        """
        self.assertEqual(try_to_int("5"), 5)
        self.assertEqual(try_to_int("-5"), -5)

    def test_string_float(self):
        """
        string to float conversion
        """
        self.assertEqual(try_to_int("-5.5"), -5.5)

    def test_float_to_int(self):
        """
        float to int conversion
        """
        self.assertEqual(type(try_to_int(5.0)), int)
        self.assertEqual(type(try_to_int(0.0)), int)
        self.assertEqual(type(try_to_int(-5.0)), int)

    def test_int_to_int(self):
        """
        int stays int
        """
        self.assertEqual(type(try_to_int(5)), int)
        self.assertEqual(type(try_to_int(0)), int)
        self.assertEqual(type(try_to_int(-5)), int)

    def test_float_to_float(self):
        """
        float stays float
        """
        self.assertEqual(type(try_to_int(5.1)), float)
        self.assertEqual(type(try_to_int(-5.1)), float)

    def test_string_float_to_int(self):
        """
        float string to int conversion
        """
        self.assertEqual(type(try_to_int("5.0")), int)
        self.assertEqual(type(try_to_int("0.0")), int)
        self.assertEqual(type(try_to_int("-5.0")), int)

    def test_string_int_to_int(self):
        """
        int string stays int
        """
        self.assertEqual(type(try_to_int("5")), int)
        self.assertEqual(type(try_to_int("0")), int)
        self.assertEqual(type(try_to_int("-5")), int)

    def test_string_float_to_float(self):
        """
        float string stays float
        """
        self.assertEqual(type(try_to_int("5.1")), float)
        self.assertEqual(type(try_to_int("-5.1")), float)


class ResultToIntTests(unittest.TestCase):
    """
    Tests for result_to_int decorator
    """
    @result_to_int
    def sample_function(self, value):
        """
        sample function that returns given value
        """
        return value

    def test_result_float(self):
        """
        result stays float
        """
        self.assertEqual(type(self.sample_function(5.5)), float)
        self.assertEqual(type(self.sample_function(-5.5)), float)

    def test_result_int(self):
        """
        result stays int
        """
        self.assertEqual(type(self.sample_function(5)), int)
        self.assertEqual(type(self.sample_function(-5)), int)

    def test_result_float_to_int(self):
        """
        float result is converted to int
        """
        self.assertEqual(type(self.sample_function(5.0)), int)
        self.assertEqual(type(self.sample_function(0.0)), int)
        self.assertEqual(type(self.sample_function(-5.0)), int)


if __name__ == "__main__":
    unittest.main()
