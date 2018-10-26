"""
The module that contains the operators, that are possible to use in pycalc, the functions for those operator
Also contains the dictionary with priority values for all using operators
"""


def power(lhs, rhs):
    """
    function for power operators ("**" and "^") handling raising negative number to a fractional power exception
    :param lhs: left hand side number
    :param rhs: right hand side number
    :return: left hand side number raised to right hand side number's power
    """
    if lhs < 0 and type(rhs) == float and not rhs.is_integer():
        raise Exception("negative number cannot be raised to a fractional power")
    return lhs ** rhs


# operators functions by a sign
operators = {
    # arithmetic
    "+":  (lambda lhs, rhs: lhs + rhs),     # addition
    "-":  (lambda lhs, rhs: lhs - rhs),     # subtraction
    "*":  (lambda lhs, rhs: lhs * rhs),     # multiplication
    "/":  (lambda lhs, rhs: lhs / rhs),     # division
    "//": (lambda lhs, rhs: lhs // rhs),    # floor division
    "%":  (lambda lhs, rhs: lhs % rhs),     # modulo
    "^":  power,                            # power as ^
    "**": power,                            # power as **
    "~":  (lambda x: -x),                   # unary minus
    "#":  (lambda x: x),                    # unary plus

    # logic
    "==": (lambda lhs, rhs: lhs == rhs),    # equals
    "<":  (lambda lhs, rhs: lhs < rhs),     # less
    "<=": (lambda lhs, rhs: lhs <= rhs),    # less or equal
    ">":  (lambda lhs, rhs: lhs > rhs),     # greater
    ">=": (lambda lhs, rhs: lhs >= rhs),    # greater or equal
    "!=": (lambda lhs, rhs: lhs != rhs)     # not equal
}


# operator precedence (the more the number - the higher the priority)
priority = {
    "~": 5, "#": 5,
    "^": 4, "**": 4,
    "/": 3, "//": 3, "%": 3, "*": 3,
    "-": 2, "+": 2,
    "<": 1, "<=": 1, ">": 1, ">=": 1,
    "!=": 0, "==": 0,
}
