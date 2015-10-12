"""
   It was proposed by Christian Goldbach that every odd composite number can
   be written as the sum of a prime and twice a square.

   9 = 7 + 2×1^2
   15 = 7 + 2×2^2
   21 = 3 + 2×3^2
   25 = 7 + 2×3^2
   27 = 19 + 2×2^2
   33 = 31 + 2×1^2

   It turns out that the conjecture was false.

   What is the smallest odd composite that cannot be written as the sum of a
   prime and twice a square?
"""

from math import sqrt

def is_prime(n):
    """Returns true if n is a prime number"""
    if n == 2 :
        return True
    if not n % 2 or n < 2:
        return False
    return all(n % x for x in range(3, int(sqrt(n)) + 1, 2))

def get_odd_composites():
    """Generate odd composite numbers infinitely"""
    n = 9
    while True:
        if not is_prime(n):
            yield n
        n += 2

if __name__ == '__main__':

    for odd_comp in get_odd_composites():
        for n in range(int(sqrt(odd_comp))):
            must_be_prime = odd_comp - 2 * (n ** 2)
            #~ print(odd_comp, n, must_be_prime)
            if is_prime(must_be_prime):
                break
        else:
            break
    
    print(odd_comp)

"""
NOTE:
To prove the conjecture false,
    C = P + 2 * n^2
    P = C - 2 * n^2
we need to find a number such that its difference with 
twice the square of n (where n < sqrt(C/2)) is not a prime.
"""
