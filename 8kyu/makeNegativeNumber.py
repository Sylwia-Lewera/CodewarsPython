"""
In this simple assignment you are given a number and have to make it negative:
Notes
The number can be negative already, in which case no change is required.
Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.
"""
def make_negative( number ):
    try:
        if number <= 0:
            return number
        else:
            return -number
    except TypeError:
        pass