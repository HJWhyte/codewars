# Find the perfect square!

# You might know some pretty large perfect squares. But what about the NEXT one?
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

# Examples:(Input --> Output)

# 121 --> 144
# 625 --> 676
# 114 --> -1 since 114 is not a perfect square

# My solution: 

import math

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise

    if (type(sq) == int) and ((math.sqrt(sq)).is_integer() == True):
        x = sq**0.5
        x += 1
        y = x**2
        return y
    else: 
        return -1
    
# Best found solution:

def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1