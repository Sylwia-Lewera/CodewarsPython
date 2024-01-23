"""
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.
Input validation
If an empty value ( null, None, Nothing etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.
"""

def sum_array(arr):
    if arr == None or arr == [] or (len(arr) == 1):
        return 0
    return sum(arr) - max(arr) - min(arr)

print(sum_array(None))
print(sum_array([]))