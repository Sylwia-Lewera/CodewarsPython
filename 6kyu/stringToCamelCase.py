"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). 
The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""
def to_camel_case(text):
    result = ""
    
    if text == '':
        return ''
    firstFlag = text[0].islower()
    if text.find('_'):
        textList = text.split('_')
        print("underscores",textList)
    if text.find('-'):
        textList = text.split('-')
        print("dashes",textList)
                
    for item in textList:
        if firstFlag:
            result += item
            firstFlag = False
            continue
        result += item.title()    
    return result
  
print(to_camel_case(""))
print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))
print(to_camel_case("A-B-C"))
"""  print("underscore find","the_stealth_warrior".find("_"))
print("split undescores","the_stealth_warrior".split("_"))"""

print("firstFlag","the_stealth_warrior"[0].islower())

