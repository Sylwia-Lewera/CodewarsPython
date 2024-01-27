"""
Help Johnny!
He can't make his code work!
Easy Code
Johnny is trying to make a function that encode 2 strings into their ASCII values and sum them together, but he can't find the error in his code! Help him!
"""
def add(s1, s2):
    if len(s1) == 1 and len(s2) == 1:
        len1 = ord(s1)
        len2 = ord(s2)
    else:
        len1 = 0
        for item in s1:
            len1 += ord(item)
        len2 = 0
        for item in s2:
            len2 += ord(item)
    return len1 + len2

"""
Improvement:
def add(s1, s2):
    return sum(ord(x) for x in s1+s2)
"""