"""
   The number, 197, is called a circular prime because all rotations of the
   digits: 197, 971, and 719, are themselves prime.

   There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
   71, 73, 79, and 97.

   How many circular primes are there below one million?
"""

from math import sqrt

def is_prime(n):
    """Returns true if n is a prime number"""
    if n == 2 :
        return True
    if not n % 2 or n < 2:
        return False
    return all(n % x for x in range(3, int(sqrt(n)) + 1, 2))

def get_circular_primes(n):
    """Generate circular prime numbers in range 0..n-1"""
    yield 2
    p = 3
    while p < n:
        if is_prime(p):
            s = str(p)
            rotations = (s[i:] + s[:i] for i in range(1, len(s)))
            if all(is_prime(int(x)) for x in rotations):
                yield p
        p += 2


if __name__ == '__main__':
    upper = 1000000

    n_circular_primes = sum(1 for _ in get_circular_primes(upper))
    
    print(n_circular_primes)
