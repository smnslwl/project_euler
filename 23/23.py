"""
   A perfect number is a number for which the sum of its proper divisors is
   exactly equal to the number. For example, the sum of the proper divisors
   of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
   number.

   A number n is called deficient if the sum of its proper divisors is less
   than n and it is called abundant if this sum exceeds n.

   As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
   smallest number that can be written as the sum of two abundant numbers is
   24. By mathematical analysis, it can be shown that all integers greater
   than 28123 can be written as the sum of two abundant numbers. However,
   this upper limit cannot be reduced any further by analysis even though it
   is known that the greatest number that cannot be expressed as the sum of
   two abundant numbers is less than this limit.

   Find the sum of all the positive integers which cannot be written as the
   sum of two abundant numbers.
"""

from math import sqrt

def is_abundant(n):
    """Return true if the sum of proper divisors of n exceeds n"""
    divisors = {1}
    for divisor in range(2, int(sqrt(n)) + 1):
        if not n % divisor:
            divisors.update((divisor, n // divisor))
    return sum(divisors) > n

if __name__ == '__main__':    
    upper = 28123
    
    abundants = set()
    non_abundant_sum = 0
    for i in range(1, upper):
        if not any(i - a in abundants for a in abundants):
            non_abundant_sum += i
        if is_abundant(i):
            abundants.add(i)
    
    print(non_abundant_sum)
