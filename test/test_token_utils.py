import unittest
from math import *
import sys

sys.path.append("../")
from utils.token_utils import *


class CutNextTokenTests(unittest.TestCase):

    def test_operators(self):
        self.assertEqual(cut_next_token("+"), (Token(Type.OPERATOR, "+"), ""))
        self.assertEqual(cut_next_token("-"), (Token(Type.OPERATOR, "-"), ""))
        self.assertEqual(cut_next_token("*"), (Token(Type.OPERATOR, "*"), ""))
        self.assertEqual(cut_next_token("/"), (Token(Type.OPERATOR, "/"), ""))
        self.assertEqual(cut_next_token("%"), (Token(Type.OPERATOR, "%"), ""))
        self.assertEqual(cut_next_token("//"), (Token(Type.OPERATOR, "//"), ""))
        self.assertEqual(cut_next_token("**"), (Token(Type.OPERATOR, "**"), ""))
        self.assertEqual(cut_next_token("^"), (Token(Type.OPERATOR, "^"), ""))
        self.assertEqual(cut_next_token("=="), (Token(Type.OPERATOR, "=="), ""))
        self.assertEqual(cut_next_token("<"), (Token(Type.OPERATOR, "<"), ""))
        self.assertEqual(cut_next_token("<="), (Token(Type.OPERATOR, "<="), ""))
        self.assertEqual(cut_next_token(">"), (Token(Type.OPERATOR, ">"), ""))
        self.assertEqual(cut_next_token(">="), (Token(Type.OPERATOR, ">="), ""))
        self.assertEqual(cut_next_token("!="), (Token(Type.OPERATOR, "!="), ""))

    def test_numbers(self):
        self.assertEqual(cut_next_token("1234"), (Token(Type.NUMBER, "1234"), ""))
        self.assertEqual(cut_next_token("12.34"), (Token(Type.NUMBER, "12.34"), ""))
        self.assertEqual(cut_next_token(".34"), (Token(Type.NUMBER, ".34"), ""))
        self.assertEqual(cut_next_token("12."), (Token(Type.NUMBER, "12."), ""))

    def test_functions(self):
        self.assertEqual(cut_next_token("sin"), (FunctionToken("sin", sin), ""))
        self.assertEqual(cut_next_token("tanh"), (FunctionToken("tanh", tanh), ""))
        self.assertEqual(cut_next_token("log10"), (FunctionToken("log10", log10), ""))
        self.assertEqual(cut_next_token("abs"), (FunctionToken("abs", abs), ""))
        self.assertEqual(cut_next_token("round"), (FunctionToken("round", round), ""))

    def test_constants(self):
        self.assertEqual(cut_next_token("e"), (Token(Type.NUMBER, str(e)), ""))
        self.assertEqual(cut_next_token("pi"), (Token(Type.NUMBER, str(pi)), ""))

    def test_brackets_divisors(self):
        self.assertEqual(cut_next_token("("), (Token(Type.OPENING_BRACKET, "("), ""))
        self.assertEqual(cut_next_token(")"), (Token(Type.CLOSING_BRACKET, ")"), ""))
        self.assertEqual(cut_next_token(","), (Token(Type.FUNC_DIVISOR, ","), ""))


class TokenizeTests(unittest.TestCase):

    def test_combination(self):
        to_check = [FunctionToken("pow", pow), Token(Type.OPENING_BRACKET, "("), Token(Type.NUMBER, ".2"),
                    Token(Type.OPERATOR, "**"), Token(Type.NUMBER, "3"), Token(Type.FUNC_DIVISOR, ","),
                    Token(Type.NUMBER, "2."), Token(Type.OPERATOR, "+"), Token(Type.NUMBER, str(pi)),
                    Token(Type.CLOSING_BRACKET, ")")]
        self.assertEqual(tokenize("pow(.2**3, 2.+pi)", []), to_check)

    def test_insert_multiplication(self):
        to_check = [Token(Type.CLOSING_BRACKET, ")"), Token(Type.OPERATOR, "*"), Token(Type.OPENING_BRACKET, "(")]
        self.assertEqual(tokenize(")(", []), to_check)
        to_check = [Token(Type.NUMBER, "1234"), Token(Type.OPERATOR, "*"), Token(Type.OPENING_BRACKET, "(")]
        self.assertEqual(tokenize("1234(", []), to_check)

    def test_unary(self):
        to_check = [Token(Type.OPERATOR, "~"), Token(Type.NUMBER, "1")]
        self.assertEqual(tokenize("-1", []), to_check)
        to_check = [Token(Type.OPERATOR, "#"), Token(Type.NUMBER, "1")]
        self.assertEqual(tokenize("+1", []), to_check)
        to_check = [Token(Type.OPERATOR, "#"), Token(Type.OPERATOR, "~"), Token(Type.NUMBER, "1")]
        self.assertEqual(tokenize("+-1", []), to_check)
        to_check = [Token(Type.NUMBER, "1"), Token(Type.OPERATOR, "+"), Token(Type.OPERATOR, "~"),
                    Token(Type.NUMBER, "1")]
        self.assertEqual(tokenize("1+-1", []), to_check)

    def test_has_no_arguments(self):
        self.assertFalse(tokenize("sin()", [])[0].has_arguments)
        self.assertTrue(tokenize("sin(1)", [])[0].has_arguments)
        self.assertTrue(tokenize("sin(1,2)", [])[0].has_arguments)


if __name__ == "__main__":
    unittest.main()
