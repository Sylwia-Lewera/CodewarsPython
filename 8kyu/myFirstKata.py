"""
Fix the Bugs (Syntax) - My First Kata

Hello, this is my first Kata so forgive me if it is of poor quality.

In this Kata you should fix/create a program that returns the following values:

false/False if either a or b (or both) are not numbers
a % b plus b % a if both arguments are numbers
You may assume the following:

If a and b are both numbers, neither of a or b will be 0.
"""

def my_first_kata(a,b):
    if type(a) != 'int' or type(b) != 'int': return False
    elif type(a) =='int' and type(b) == 'int': return (a % b + b % a)

print(my_first_kata(3,5))
print(type(3))
print(type(5))


""" improvement
def my_first_kata(a, b):
    try:
        return a % b + b % a
    except (TypeError, ZeroDivisionError):
        return False
"""