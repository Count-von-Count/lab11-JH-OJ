import math
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError("division by zero")
    return b / a
def log(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        return "Invalid input for logarithm"
def exp(a, b):
    return a ** b


