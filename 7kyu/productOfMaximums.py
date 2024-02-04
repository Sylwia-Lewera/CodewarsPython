"""
Given an array/list [] of integers , Find the product of the k maximal numbers.

Notes
Array/list size is at least 3 .

Array/list's numbers Will be mixture of positives , negatives and zeros

Repetition of numbers in the array/list could occur.
"""

import math

def max_product(lst, n_largest_elements):    
    lstSorted = sorted(lst, reverse = True) # sorting list in desc order
    maximals = lstSorted[: n_largest_elements]    # selecting n largest elements from list
    return math.prod(maximals) # returning the product of the k maximal numbers