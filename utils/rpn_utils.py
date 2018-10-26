"""
The module that contains functions for working with reversed polish notation: converting from infix notation to RPN
and evaluating the expression in RPN
"""
from inspect import signature

from data.my_token import *
from utils.common_utils import *
from data.default_operators import *


def convert_to_rpn(token_list: list):
    """
    Converts a list of tokens to reversed polish notation using shunting-yard algorithm
    :param token_list: list of tokens in infix notation
    :return: list of tokens in RPN
    """
    result = []
    stack = []

    while token_list or stack:
        # check if there are tokens in input and get next token
        token = token_list.pop(0) if len(token_list) > 0 else None

        # if there are only tokens in stack left
        if token is None:
            while stack:
                stack_top = stack.pop()
                if stack_top.type in (Type.OPENING_BRACKET, Type.CLOSING_BRACKET):
                    raise Exception("brackets are not balanced")
                result.append(stack_top)
            break

        # if token is a number push it to the output queue
        if token.type == Type.NUMBER:
            result.append(token)
        # if token is a function push it onto the stack
        elif token.type == Type.FUNCTION:
            stack.append(token)
        # if token is a function divisor e.g. "," push operators to the output queue until opening bracket
        elif token.type == Type.FUNC_DIVISOR:
            while stack and stack[-1].type != Type.OPENING_BRACKET:
                result.append(stack.pop())
            result.append(token)
        # if token is operator check the priority of stack operators and if needed push it to the output
        # then push the token onto the stack
        elif token.type == Type.OPERATOR:
            while stack and stack[-1].type == Type.OPERATOR and (
                    not token.is_right_associative() and priority[token.s_value] <= priority[stack[-1].s_value]
                    or token.is_right_associative() and priority[token.s_value] < priority[stack[-1].s_value]):
                result.append(stack.pop())
            else:
                stack.append(token)
        # if token is an opening bracket put it to the stack
        elif token.type == Type.OPENING_BRACKET:
            stack.append(token)
        # if token is closing bracket push operators to the output queue until opening bracket
        # if after it there is a function on the top of stack push it to the output
        elif token.type == Type.CLOSING_BRACKET:
            if stack:
                stack_top = stack.pop()
            else:
                raise Exception("brackets are not balanced")
            while stack_top.type != Type.OPENING_BRACKET:
                result.append(stack_top)
                if stack:
                    stack_top = stack.pop()
                else:
                    raise Exception("brackets are not balanced")
            if stack and stack[-1].type == Type.FUNCTION:
                result.append(stack.pop())

    return result


def evaluate_rpn(token_list: list):
    """
    Evaluates the expression converted to reversed polish notation
    :param token_list: RPN token list
    :return: the result of the RPN expression
    """
    # check if given token list is empty
    if not token_list:
        raise Exception("empty expression given")

    stack = []
    # function arguments stack
    function_stack = []

    while token_list:
        token = token_list.pop(0)

        # if token is a number put it onto stack
        if token.type == Type.NUMBER:
            stack.append(try_to_int(token.s_value))
        # if token is an operator
        elif token.type == Type.OPERATOR:
            # determine number of parameters for this operator
            sig = signature(operators[token.s_value])
            num_of_params = len(sig.parameters)
            # fill the arguments list according to number of parameters
            arguments = []
            for i in range(num_of_params):
                arguments.append(stack.pop())
            # apply the operator to the argument(s) and put the result onto the stack
            stack.append(apply_function(operators[token.s_value], reversed(arguments)))
        # if token is a function divisor e.g. "," put the top stack value to the function stack
        elif token.type == Type.FUNC_DIVISOR:
            function_stack.append(stack.pop())
        # if token is a function
        elif token.type == Type.FUNCTION:
            # complete the function stack with the top stack value
            if token.has_arguments:
                function_stack.append(stack.pop())
            # apply the function to the function stack values and put the result onto the stack
            stack.append(apply_function(token.function, function_stack))
            # flush function arguments stack
            function_stack = []

    # if there are more or less than one elements in the stack then there is a missing operation or operands
    if len(stack) != 1:
        raise Exception("Operation mismatch")

    return stack[0]
