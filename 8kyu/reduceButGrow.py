"""
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
"""
def grow(arr):
    result = 1
    try:
        for item in arr:
            result *= item
        return result
    except TypeError:
        print('Invalid data provided')