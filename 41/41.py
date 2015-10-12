"""
   We shall say that an n-digit number is pandigital if it makes use of all
   the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
   and is also prime.

   What is the largest n-digit pandigital prime that exists?
"""

from math import sqrt
from itertools import permutations

def is_prime(n):
    """Returns true if n is a prime number"""
    if n == 2 :
        return True
    if not n % 2 or n < 2:
        return False
    return all(n % x for x in range(3, int(sqrt(n)) + 1, 2))

def to_num(numbers):
    """Return a number made from an iterable of digits"""
    n = 0
    for i, num in enumerate(numbers):
        n += 10 ** (len(numbers) - i - 1) * num
    return n

if __name__ == '__main__':

    max_pprime = 2143
    for n in range(4, 10):
        perms = (to_num(p) for p in permutations(range(1, n + 1), n))
        for perm in perms:
            if is_prime(perm):
                max_pprime = perm

    print(max_pprime)
    
"""
NOTE:
We start from the 2143 and the 4th digit because we are given
an example in the problem. As we are going through permutations,
there is no need to check for pandigital-ness. Similarly, the last
found result is always going to be the max as we are iterating in order.
"""
