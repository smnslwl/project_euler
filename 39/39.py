"""
   If p is the perimeter of a right angle triangle with integral length
   sides, {a,b,c}, there are exactly three solutions for p = 120.

   {20,48,52}, {24,45,51}, {30,40,50}

   For which value of p ≤ 1000, is the number of solutions maximised?
"""

from math import sqrt

if __name__ == '__main__':
    upper = 1000
    
    max_solutions, max_p = 0, 0
    for p in range(2, upper + 1, 2):
        solutions = 0
        for a in range(2, p // 3 + 1):
            if not p * (p - 2 * a) % (2 * (p - a)):
                solutions += 1
        if solutions > max_solutions:
            max_solutions, max_p = solutions, p

    print(max_p)

"""
NOTE:
    a^2 + b^2 = c^2
    a + b + c = p
    or c = p - a - b
    by substitution
    a^2 + b^2 = (p - a - b)^2 = p^2 + a^2 + b^2 -2pa – 2pb + 2ab
    we get,
    b = (p^2 - 2pa) / (2p - 2a) 
"""
