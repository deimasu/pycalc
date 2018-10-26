"""
The module contains function for working with tokens
"""
import re
from builtins import *
from math import *
from importlib import import_module

from data.my_token import *
from data.default_operators import operators


def cut_next_token(expr: str):
    """
    Cuts the first token from the expression and determines the type of this token.

    Performs a search for different type of tokens in the beginning of the expression.
    Returns a tuple with token and expression after cutting a token from it.

    If token was not found returns token Type.ERROR and an empty string.
    :param expr: string math expression
    :return: tuple of token and cut expression
    """
    # getting rid of trailing spaces
    expr = expr.lstrip()

    # checking for one character tokens: "(", ")" and ","
    if expr[0] == "(":
        return Token(Type.OPENING_BRACKET, expr[0]), expr[1:]
    elif expr[0] == ")":
        return Token(Type.CLOSING_BRACKET, expr[0]), expr[1:]
    elif expr[0] == ",":
        return Token(Type.FUNC_DIVISOR, expr[0]), expr[1:]

    # checking for operator
    for operator in sorted(operators.keys(), key=len, reverse=True):
        if expr.find(operator) == 0:
            return Token(Type.OPERATOR, operator), expr[len(operator):]

    # checking for number
    num_search_result = re.compile(r"(\d+\.\d+)|(\d+\.)|(\.\d+)|(\d+)").search(expr)
    if num_search_result is not None and num_search_result.start(0) == 0:
        return Token(Type.NUMBER, num_search_result.group(0)), expr[len(num_search_result.group(0)):]

    # checking for identifiers (functions and constants)
    id_search_result = re.compile(r"[^\d\W]\w*").search(expr)
    if id_search_result is not None and id_search_result.start(0) == 0:
        identifier = id_search_result.group(0).lower()
        if identifier in globals():
            if callable(globals()[identifier]):
                return FunctionToken(identifier, globals()[identifier]), expr[len(identifier):]
            elif type(globals()[identifier]) in (int, float):
                return Token(Type.NUMBER, str(globals()[identifier])), expr[len(identifier):]

    # if no tokens found
    return Token(Type.ERROR, expr), ""


def tokenize(expr: str, modules: list):
    """
    Imports modules

    Converts string math expression to list of tokens.

    Checks if "+" or "-" is unary operator.

    Inserts missing multiplication signs before opening brackets e.g. 10(1+2), (1+2)(3+4)
    :param modules: additional modules to use in expression
    :param expr: string math expression
    :return: list of tokens
    """
    if modules is not None:
        for module in modules:
            mod = import_module(module)
            globals().update(mod.__dict__)

    token_list = []
    last_token_type = None

    while expr.strip() != "":
        current_token, expr = cut_next_token(expr)

        if current_token.type == Type.ERROR:
            error_line = "".join([str(t) for t in token_list])
            raise Exception("Unexpected symbol\n"
                            + error_line + str(current_token) + "\n"
                            + " " * (len(error_line)) + "^")

        # check if there is a missed multiplication before opening bracket
        if last_token_type is not None and current_token.type == Type.OPENING_BRACKET \
                and (last_token_type in (Type.NUMBER, Type.CLOSING_BRACKET)):
            token_list.append(Token(Type.OPERATOR, "*"))
        # check if current operator plus or minus is unary
        elif current_token.s_value in ("+", "-"):
            if last_token_type is None or not (last_token_type in (Type.NUMBER, Type.CLOSING_BRACKET)):
                # converting plus or minus to unary analogs
                current_token.s_value = "#" if current_token.s_value == "+" else "~"

        token_list.append(current_token)

        # check if last processed function has no arguments
        if current_token.type == Type.CLOSING_BRACKET and len(token_list) >= 3 and \
                [t.type for t in token_list[-3:]] == [Type.FUNCTION, Type.OPENING_BRACKET, Type.CLOSING_BRACKET]:
            token_list[-3].has_arguments = False

        last_token_type = current_token.type

    return token_list
