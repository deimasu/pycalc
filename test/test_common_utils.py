import unittest
import sys

sys.path.append("../")
from utils.common_utils import *


class TryToIntTests(unittest.TestCase):

    def test_int(self):
        self.assertEqual(try_to_int(5), 5)
        self.assertEqual(try_to_int(0), 0)
        self.assertEqual(try_to_int(-5), -5)

    def test_float(self):
        self.assertEqual(try_to_int(5.5), 5.5)
        self.assertEqual(try_to_int(-5.5), -5.5)

    def test_string_int(self):
        self.assertEqual(try_to_int("5"), 5)
        self.assertEqual(try_to_int("-5"), -5)

    def test_string_float(self):
        self.assertEqual(try_to_int("-5.5"), -5.5)

    def test_float_to_int(self):
        self.assertEqual(type(try_to_int(5.0)), int)
        self.assertEqual(type(try_to_int(0.0)), int)
        self.assertEqual(type(try_to_int(-5.0)), int)

    def test_int_to_int(self):
        self.assertEqual(type(try_to_int(5)), int)
        self.assertEqual(type(try_to_int(0)), int)
        self.assertEqual(type(try_to_int(-5)), int)

    def test_float_to_float(self):
        self.assertEqual(type(try_to_int(5.1)), float)
        self.assertEqual(type(try_to_int(-5.1)), float)

    def test_string_float_to_int(self):
        self.assertEqual(type(try_to_int("5.0")), int)
        self.assertEqual(type(try_to_int("0.0")), int)
        self.assertEqual(type(try_to_int("-5.0")), int)

    def test_string_int_to_int(self):
        self.assertEqual(type(try_to_int("5")), int)
        self.assertEqual(type(try_to_int("0")), int)
        self.assertEqual(type(try_to_int("-5")), int)

    def test_string_float_to_float(self):
        self.assertEqual(type(try_to_int("5.1")), float)
        self.assertEqual(type(try_to_int("-5.1")), float)


class ResultToIntTests(unittest.TestCase):

    @result_to_int
    def sample_function(self, value):
        return value

    def test_result_float(self):
        self.assertEqual(type(self.sample_function(5.5)), float)
        self.assertEqual(type(self.sample_function(-5.5)), float)

    def test_result_int(self):
        self.assertEqual(type(self.sample_function(5)), int)
        self.assertEqual(type(self.sample_function(-5)), int)

    def test_result_float_to_int(self):
        self.assertEqual(type(self.sample_function(5.0)), int)
        self.assertEqual(type(self.sample_function(0.0)), int)
        self.assertEqual(type(self.sample_function(-5.0)), int)


if __name__ == "__main__":
    unittest.main()
