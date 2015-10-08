"""
   Starting in the top left corner of a 2×2 grid, and only being able to move
   to the right and down, there are exactly 6 routes to the bottom right
   corner.

                {{ p_015.gif }}
   
   How many such routes are there through a 20×20 grid?
"""

from math import factorial

if __name__ == '__main__':
    m, n = 20, 20
    
    number_of_routes = factorial(m + n) // (factorial(m) * factorial(n))
    
    print(number_of_routes)

"""
RECURSIVE SOLUTION (exponential-time, DO NOT ATTEMPT)

    def number_of_routes(m, n):
        if not m or not n:
            return 1
        return number_of_routes(m - 1, n) + number_of_routes(m, n - 1) 

    m, n = 20, 20
    print(number_of_routes(m, n))

TODO: Dynamic Programming : cache previously calculated results
see: http://stackoverflow.com/questions/2200236/project-euler-15
"""
