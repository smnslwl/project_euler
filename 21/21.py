"""
   Let d(n) be defined as the sum of proper divisors of n (numbers less than
   n which divide evenly into n).
   If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
   and each of a and b are called amicable numbers.

   For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
   44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
   2, 4, 71 and 142; so d(284) = 220.

   Evaluate the sum of all the amicable numbers under 10000.
"""

from math import sqrt

def d(n):
    """Return the sum of proper divisors of n"""
    sum_d = 1
    for divisor in range(2, int(sqrt(n)) + 1):
        if not n % divisor:
            sum_d += divisor + n // divisor
    return sum_d

if __name__ == '__main__':
    upper = 10000
    
    a_sum = sum(i for i in range(1, upper) if i == d(d(i)) and not i == d(i))
    
    print(a_sum)

