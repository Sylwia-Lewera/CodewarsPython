"""
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 
The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""
def digital_root(n):
    sum = 0
    for digit in str(n):  
        sum += int(digit)
    while len(str(sum)) > 1:
        prev_sum = sum
        sum = 0
        for digit in str(prev_sum):  
            sum += int(digit)    
    return sum

# short solution return n if n < 10 else digital_root(sum(map(int,str(n))))