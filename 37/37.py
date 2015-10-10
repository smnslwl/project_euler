"""
   The number 3797 has an interesting property. Being prime itself, it is
   possible to continuously remove digits from left to right, and remain
   prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
   right to left: 3797, 379, 37, and 3.

   Find the sum of the only eleven primes that are both truncatable from left
   to right and right to left.

   NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from math import sqrt

def is_prime(n):
    """Returns true if n is a prime number"""
    if n == 2 :
        return True
    if not n % 2 or n < 2:
        return False
    return all(n % x for x in range(3, int(sqrt(n)) + 1, 2))

def get_truncatable_primes():
    """Generate prime numbers infinitely that are both truncatable 
    from left to right and right to left (apparently, only 11 exist)"""
    p = 11 # skip 2, 3, 5, 7
    while True:
        if is_prime(p):
            s = str(p)
            trunks = ((int(s[i:]), int(s[:i])) for i in range(1, len(s)))
            if all(is_prime(x) and is_prime(y) for x, y in trunks):
                yield p
        p += 2


if __name__ == '__main__':
    n = 11
    
    sum_truncables = 0
    for i, prime in enumerate(get_truncatable_primes()):
        sum_truncables += prime
        if i + 1 == n:
            break
            
    print(sum_truncables)
 
