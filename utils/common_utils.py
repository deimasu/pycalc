"""
The module that contains common function for working with numbers and functions
"""


def try_to_int(number):
    """
    Returns an integer if the number may be converted to integer or is integer, returns float otherwise
    :param number: float or integer number
    :return: float or integer number
    """
    # converting to float to make able to pass a string
    number = float(number)
    return int(number) if type(number) == int or type(number) == float and number.is_integer() else float(number)


def result_to_int(func_to_call):
    """
    A decorator that tries to convert the result to int if there is no loss
    :param func_to_call: function returning number
    :return: decorated function wrapper
    """
    def wrapper(*args):
        """
        A wrapper for the function that applies the given function with given parameters
        and returns int if it's possible
        :param args: function arguments
        :return: result of try_to_int function applied to result
        """
        result = func_to_call(*args)
        return try_to_int(result)
    return wrapper


@result_to_int
def apply_function(func, arguments):
    """
    The function that applies given function to given arguments
    :param func: any function
    :param arguments: a collection of arguments that will be expanded
    :return: the result of given function with given parameters
    """
    return func(*arguments)
