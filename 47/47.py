"""
   The first two consecutive numbers to have two distinct prime factors are:

   14 = 2 × 7
   15 = 3 × 5

   The first three consecutive numbers to have three distinct prime factors
   are:

   644 = 2² × 7 × 23
   645 = 3 × 5 × 43
   646 = 2 × 17 × 19.

   Find the first four consecutive integers to have four distinct prime
   factors. What is the first of these numbers?
"""

def has_n_factors(x, n):
    """Return true if x has n distinct prime factors"""
    factors = set()
    divisor = 2
    while divisor <= x:
        if not x % divisor:
            factors.add(divisor)
            x /= divisor
        else:
            divisor += 1
    return len(factors) == n
    

if __name__ == '__main__':
    n = 4
    start = 134000
    
    last_n = [0] * n
    i = 0
    number = start
    while True:
        if has_n_factors(number, n):
            last_n[i] = number
            if all(number - k in last_n for k in range(1, n)):
                break
            i += 1
            if i == n:
                i = 0
        number += 1
    first = number - n + 1

    print(first)
    
"""
NOTE:
Kept increasing the starting value for the number manually till
it found a solution in a reasonable time. It's still a pretty
slow solution, needs some optimizations/change in algo.
"""
