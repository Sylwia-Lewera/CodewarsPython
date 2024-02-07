"""
Challenge: You are given a list of numbers. The numbers each repeat a certain number of times. Remove all numbers that repeat an odd number of times while keeping everything else the same.

odd_ones_out([1, 2, 3, 1, 3, 3]) = [1, 1]

"""

def odd_ones_out(numbers):
    toRemove = {}
    for item in numbers:
        count = numbers.count(item)
        if count % 2 != 0:
            toRemove[item]= [item, count]
    for item in toRemove:
        print("item removed: ",item)
        for _ in range(toRemove[item][1]):
            numbers.remove(toRemove[item][0])        
    return numbers

"""
to improve with selecting only even from list and returining =>  [i for i in numbers if numbers.count(i) % 2 == 0]
"""