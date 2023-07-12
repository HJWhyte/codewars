## Is this a triangle?
# Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.
# (In this case, all triangles must have surface greater than 0 to be accepted).

# My solution:

def is_triangle(a, b, c):

    args = [a, b, c]
    max_val = max(args)
    args.remove(max_val)
    x = sum(args)
    if x > max_val:            
        return True
    else: 
        return False
    
# Best solution found: 

def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c


    