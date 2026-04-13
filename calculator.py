"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    pass

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def logarithm(a, b):
    try:
        if b == 0 or a == 0:
            raise ValueError
        else:
            return math.log(b, a)
    except ValueError:
        print("Base and value must be positive.")
        return 0

def exponent(a, b):
    return a**b
