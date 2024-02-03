"""
Description
An infinite number of shelves are arranged one above the other in a staggered fashion.
The cat can jump either one or three shelves at a time: from shelf i to shelf i+1 or i+3 (the cat cannot climb on the shelf directly above its head), according to the illustration:

                 ┌────────┐
                 │-6------│
                 └────────┘
┌────────┐       
│------5-│        
└────────┘  ┌─────► OK!
            │    ┌────────┐
            │    │-4------│
            │    └────────┘
┌────────┐  │
│------3-│  │     
BANG!────┘  ├─────► OK! 
  ▲  |\_/|  │    ┌────────┐
  │ ("^-^)  │    │-2------│
  │ )   (   │    └────────┘
┌─┴─┴───┴┬──┘
│------1-│
└────────┘
Input
Start and finish shelf numbers (always positive integers, finish no smaller than start)

Task
Find the minimum number of jumps to go from start to finish
"""

def solution(start, finish):  
    jumpsTotal = 0
    currShelf = start
    diff = finish - start
    smallJump = 1
    bigJump = 3
    doubleJump =bigJump + smallJump
    while diff > 0:
        if diff >=  bigJump:
            diff -= bigJump
            currShelf += 3
        elif diff >= smallJump:
            diff -= smallJump
            currShelf += 1

        jumpsTotal += 1
    return jumpsTotal
