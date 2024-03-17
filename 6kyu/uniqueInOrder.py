"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements 
with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
"""
def unique_in_order(sequence):
    
    result = []
    if len(sequence) == 1:
        return list(sequence)
    if sequence:
        prev = sequence[0]
        result.append(prev)
    for item in sequence[1:]:
        if item == prev:
            pass
        else:
            result.append(item)
            prev = item
    return result