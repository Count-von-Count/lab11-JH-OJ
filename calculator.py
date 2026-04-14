"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError
        else:
            return b / a
    except ZeroDivisionError:
        print("Can't divide by zero.")
        return 0

def logarithm(a, b):
    try:
        if b == 0 or a == 0:
            raise ValueError
        else:
            return math.log(b, a)
    except ValueError:
        print("Base and value must be positive.")
        return 0

def exp(a, b):
    return a**b

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        else:
            return math.sqrt(a)
    except ValueError:
        print("Base must be positive.")
        return 0

def hypotenuse(a, b):
    return math.hypot(a, b)
