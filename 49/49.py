"""
   The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
   increases by 3330, is unusual in two ways: (i) each of the three terms are
   prime, and, (ii) each of the 4-digit numbers are permutations of one
   another.

   There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
   primes, exhibiting this property, but there is one other 4-digit
   increasing sequence.

   What 12-digit number do you form by concatenating the three terms in this
   sequence?
"""

from math import sqrt
from itertools import permutations, combinations

def is_prime(n):
    """Returns true if n is a prime number"""
    if n == 2 :
        return True
    if not n % 2 or n < 2:
        return False
    return all(n % x for x in range(3, int(sqrt(n)) + 1, 2))

def get_primes_in_range(lower, upper):
    """Generate prime numbers in the specified range"""
    p = lower if lower % 2 else lower + 1
    while p <= upper:
        if is_prime(p):
            yield p
        p += 2

if __name__ == '__main__':
    digits = 4
    n = 3
    example = 1487
    lower = pow(10, digits - 1)
    upper = pow(10, digits) - 1
    
    primes = set(get_primes_in_range(lower, upper))
    for p in primes:
        perms = {int(''.join(p)) for p in permutations(str(p), digits)}
        p_perms = {p for p in perms if p in primes}
        if len(p_perms) >= n:
           for a, b, c in combinations(p_perms, n):
               if b - a == c - b and not a == example:
                   result = ''.join(str(x) for x in (a, b, c))
                   break

    print(result)
