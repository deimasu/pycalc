"""
The module that contains all class definitions for working with tokens in pycalc
"""
from enum import Enum


class Type(Enum):
    """
    Enum for types of tokens in math expression
    Error type is made for catching unexpected values in the expression
    """
    ERROR = -1

    NUMBER = 1
    FUNCTION = 2
    FUNC_DIVISOR = 3
    OPERATOR = 4
    OPENING_BRACKET = 5
    CLOSING_BRACKET = 6


class Token:
    """
    A class that represents token. Token is a unit of math expression
    Has type and string value
    """
    def __init__(self, token_type: Type, s_value: str):
        """
        Token initializer
        :param token_type: type of creating token
        :param s_value: string representation of the token
        """
        self.type = token_type
        self.s_value = s_value

    def __repr__(self):
        """
        Represents a token as its string value
        :return: string value of the token
        """
        return self.s_value

    def is_right_associative(self):
        """
        Checks if the given operator is right_associative(power and unary operations)
        :return: boolean
        """
        if self.type is not Type.OPERATOR:
            raise Exception("is_right_associative must be called on OPERATOR type token")
        return self.s_value in ("**", "^", "~", "#")


class FunctionToken(Token):
    """
    Separate class for function type token. Has attribute 'has_arguments' that represents if there are
    any arguments passed to the function in the expression, also contains the function for this function name
    """
    def __init__(self, s_value: str, func):
        """
        Initializer for function type token
        :param s_value: string value of function type token
        :param func: function that matches the name of the function in token string value
        """
        super().__init__(Type.FUNCTION, s_value)
        self.has_arguments = True
        self.function = func
