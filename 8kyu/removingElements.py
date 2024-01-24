"""
Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

None of the arrays will be empty, so you don't have to worry about that!
"""

def remove_every_other(my_list):
    count = len(my_list)
    if my_list:
        for i in reversed(range(count)):
            if i % 2 != 0:
                del my_list[i]                            
        return my_list
    else:
        pass