"""
Create a combat function that takes the player's current health and the amount of damage recieved, 
and returns the player's new health. Health can't be less than 0.
"""

def combat(health, damage):
    current = 0
    try:
        current = health - damage
        if current >= 0 : return current
        else: return 0
    except TypeError:
        print('Invalid data provided')

print(combat(100,5))