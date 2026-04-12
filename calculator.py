import math

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

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
