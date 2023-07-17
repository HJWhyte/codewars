# CamelCase Method

# DESCRIPTION:
# Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter capitalized without spaces.

# For instance:
# camelcase("hello case") => HelloCase
# camelcase("camel case word") => CamelCaseWord

# My solution:

def camel_case(s):
    out = []
    words = s.split()
    for x in words:
        cap = x.capitalize()
        out.append(cap)
    fin = ''.join(out)
    return fin

# Best found solution: 

def camel_case(string):
    return string.title().replace(" ", "")