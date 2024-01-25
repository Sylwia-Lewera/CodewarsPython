"""
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
"""
def solution(string):
    count = len(string)
    reversedStr = ''
    if string :
        for i in reversed(range(count)):
            reversedStr += string[i]        
    else:
        pass
    return reversedStr