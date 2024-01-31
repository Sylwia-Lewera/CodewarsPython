"""
Create a moreZeros function which will receive a string for input, and return an array (or null terminated string in C) containing only the characters from that string whose binary representation of its ASCII value consists of more zeros than ones.

You should remove any duplicate characters, keeping the first occurrence of any such duplicates, so they are in the same order in the final array as they first appeared in the input string.

All input will be valid strings of length > 0. Leading zeros in binary should not be counted.
"""
def more_zeros(s):
    moreZeros = []
    
    for item in s:
        if item not in moreZeros:
            byteItem = item.encode()
            binaryInt = int.from_bytes(byteItem, "big")
            binaryString = bin(binaryInt)
            converted = binaryString[2:]
            if converted.count('0') > converted.count('1') :
                moreZeros.append(item)
    return moreZeros

