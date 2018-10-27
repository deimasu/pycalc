"""
The main module of pycalc
"""
import argparse
import sys

from utils.rpn_utils import *
from utils.token_utils import *


def evaluate_string_expression(expression: str, modules):
    """
    A function that tokenize the string math expression considering given modules, then converts in to RPN,
    then evaluates this expression and returns the result of this expression
    :param expression: string math expression
    :param modules: additional modules to use (names)
    :return: the result of math expression
    """
    return evaluate_rpn(convert_to_rpn(tokenize(expression, modules)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="pycalc", description="Pure-python command-line calculator.")

    parser.add_argument("EXPRESSION", help="expression string to evaluate", type=str)
    parser.add_argument("-m", "--use-modules", metavar="MODULE", nargs="+", help="additional modules to use")

    if "-m" in sys.argv or "--use-modules" in sys.argv:
        sys.argv.insert(len(sys.argv) - 1, "--")

    args = parser.parse_args()

    value = str(args.EXPRESSION).replace("'", "").replace('"', "")

    try:
        print(evaluate_string_expression(value, args.use_modules))
    except Exception as exception:
        print("ERROR: %s" % exception)
