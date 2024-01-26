"""
Given an array of integers a and integers t and x, count how many elements in the array you can make equal to t by increasing / decreasing it by x (or doing nothing). EASY!

# ex 1

a = [11, 5, 3]
t = 7
x = 2

count(a, t, x) # => 3

you can make 11 equal to 7 by subtracting 2 twice
you can make 5 equal to 7 by adding 2
you can make 3 equal to 7 by adding 2 twice

Constraints
-1018 <= a[i],t,x <= 1018

3 <= |a| <= 104
"""
def count(a, t, x):
    count = 0
    if a != '[]' and len(a) >= 3 and len(a) <= 10 ** 4 and x <= 10 ** 18:
        for item in a:
            if item == t:
                count += 1
            elif item < (-10 ** 18) or x == 0:
                continue
            elif  x != 0:
                if ((item - t) % x == 0) or ((item + t) % x == 0):
                    count += 1
        return count 
