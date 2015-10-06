"""
   By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
   that the 6th prime is 13.

   What is the 10001st prime number?
"""

from math import ceil, sqrt

def is_prime(n):
    """Returns true if n is a prime number"""
    if n == 2 :
        return True
    if not n % 2 or n < 2:
        return False
    return all(n % x for x in range(3, ceil(sqrt(n)) + 1))

if __name__ == '__main__':
    n = 10001

    i = 0
    while n:
        i += 1
        if is_prime(i):
            n -= 1

    print(i)
