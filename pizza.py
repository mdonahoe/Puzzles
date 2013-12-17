"""
Pizza

Input: list of numbers
Goal: maximize your sum
Rules:
1. can only take from head or tail (left or right)
2. two players
3. take turns
"""

def pizza(slices):
    if not slices: return (0,)
    left = pizza(slices[1:])[0]
    right = pizza(slices[:-1])[0]
    return max((slices[0] - left, 'Left'), (slices[-1] - right, 'Right'))

import sys
print pizza(list(int(x) for x in sys.argv[1:]))
