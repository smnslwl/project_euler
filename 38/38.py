"""
   Take the number 192 and multiply it by each of 1, 2, and 3:

     192 × 1 = 192
     192 × 2 = 384
     192 × 3 = 576

   By concatenating each product we get the 1 to 9 pandigital, 192384576. We
   will call 192384576 the concatenated product of 192 and (1,2,3)

   The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
   and 5, giving the pandigital, 918273645, which is the concatenated product
   of 9 and (1,2,3,4,5).

   What is the largest 1 to 9 pandigital 9-digit number that can be formed as
   the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

from math import factorial

def is_pandigital(n):
    """Return true if 1 to 9 occurs exactly once in n"""
    return ''.join(sorted(str(n))) == '123456789'

def concat_product(x, numbers):
    prod = ''
    for n in numbers:
        prod += str(x * n)
    return int(prod)

if __name__ == '__main__':

    lower, upper = 9234, 9487
    longest_prod = 0
    for i in range(2, 10):
        nums = tuple(range(1, i + 1))
        for n in range(lower, upper):
            prod = concat_product(n, nums)
            if prod > longest_prod and is_pandigital(prod):
                longest_prod = prod
    
    print(longest_prod)

"""
NOTE:
The bounds for the starting number can be reduced so:
 * The starting number must be 5 digits or less, as n = 2.
 * Can be further reduced to 9234, 9487 (see url below for the math)
http://www.mathblog.dk/project-euler-38-pandigital-multiplying-fixed-number/
"""
