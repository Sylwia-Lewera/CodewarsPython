"""
Your goal in this kata is to determine which phrase the girls would say at the last petal for a flower of a given number of petals: 
1. "I love you"
2. "a little"
3. "a lot"
4. "passionately"
5. "madly"
6. "not at all"

The number of petals is always greater than 0.
If there are more than 6 petals, you start over with "I love you" for 7 petals, "a little" for 8 petals and so on.

"""
def how_much_i_love_you(nb_petals):
    phrases = {
        1 : "I love you",
        2 : "a little",
        3 : "a lot",
        4 : "passionately",
        5 : "madly",
        0 : "not at all",
    }
    return phrases [nb_petals % 6]