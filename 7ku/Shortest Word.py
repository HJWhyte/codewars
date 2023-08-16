# 7 kyu
# Shortest Word

# DESCRIPTION:
# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

# My solution: 

def find_short(s):

    words = s.split()
    l = 100              # Not a great idea, unlikely to see words greater then 100 in len but still not clean

    for x in words:
        if len(x) <= l:
            l = len(x)
    return l 

# Best Found: 

def find_short(s):
    return min(len(x) for x in s.split())               # Much more efficient solution, min func key for this problem