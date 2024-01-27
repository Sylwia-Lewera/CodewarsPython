"""
The notorious Captain Schneider has given you a very straight forward mission. 
Any data that comes through the system make sure that only non-special characters see the light of day.

Create a function that given a string, retains only the letters A-Z (upper and lowercase), 0-9 digits, and whitespace characters. 
Also, returns "Not a string!" if the entry type is not a string.
"""
def nothing_special(st):
    if type(st) != str:
        return "Not a string!"
    else:
        output = ""
        for item in st:
            if ord(item) in range(48,58) or ord(item) in range(65,91) or ord(item) in range(97,123) or item.isspace():
                output += item
        return output