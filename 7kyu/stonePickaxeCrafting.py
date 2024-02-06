"""
Note: Based off Minecraft, hopefully you atleast know the game!

Task: Given an array, return the maximum amount of stone pickaxes you can craft before you run out of sticks and cobblestones. 
Within the array would be a series of strings with the exact names of the materials listed below. 
If the array has atleast 3 "Cobblestones" and 2 "Sticks" you can craft a singular stone pickaxe. Do not count any materials apart from "Cobblestones", "Sticks" and "Wood". Wood can be converted into 4 sticks!

Here are the materials you would expect in a array:

Sticks
Cobblestone
Stone (These are different from cobblestone and cannot be used to make a stone pickaxe.)
Wool
Dirt
Wood (Can be treated as sticks, typically 4 sticks for 1 wood)
Diamond

"""
def stone_pick(arr):
    sticks = arr.count("Sticks")
    sticks += arr.count("Wood") * 4 # convert wood to sticks
    cobblest = arr.count("Cobblestone")
    return min([(sticks // 2), (cobblest // 3)])  # it takes atleast 3 "Cobblestones" and 2 "Sticks" for pickaxe