"""
Make multiple functions that will return the sum, difference, modulus, product, quotient, and the exponent respectively.

Please use the following function names:

addition = add

multiply = multiply

division = divide (both integer and float divisions are accepted)

modulus = mod

exponential = exponent

subtraction = subt

Note: All math operations will be: a (operation) b
"""
def add(a, b):
    try:
        return a + b
    except TypeError:
        print('Invalid data provided!')

def multiply(a, b):
    try:
        return a * b
    except TypeError:
        print('Invalid data provided!')

def divide(a, b):
    try:
        return a / b
    except (TypeError, ZeroDivisionError):
        print('Invalid data provided!')

def mod(a, b):
    try:
        return a % b
    except (TypeError, ZeroDivisionError):
        print('Invalid data provided!')

def exponent(a, b):
    try:
        return a ** b
    except TypeError:
        print('Invalid data provided!')

def subt(a, b):
    try:
        return a - b
    except TypeError:
        print('Invalid data provided!')