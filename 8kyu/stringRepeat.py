"""
Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.
"""
def repeat_str(repeat, string):
    try:
        return repeat * string
    except TypeError:
        print('Invalid data provided')