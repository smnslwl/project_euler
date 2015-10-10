"""
   Surprisingly there are only three numbers that can be written as the sum
   of fourth powers of their digits:

     1634 = 1^4 + 6^4 + 3^4 + 4^4
     8208 = 8^4 + 2^4 + 0^4 + 8^4
     9474 = 9^4 + 4^4 + 7^4 + 4^4

   As 1 = 1^4 is not a sum it is not included.

   The sum of these numbers is 1634 + 8208 + 9474 = 19316.

   Find the sum of all the numbers that can be written as the sum of fifth
   powers of their digits.
"""

FIFTH_POWERS = {i : i**5 for i in range(10)}

def dp5sum(n):
    """Return the sum of the 5th powers of the digits of n"""
    s = 0
    while n:
        s += FIFTH_POWERS[n % 10]
        n //= 10
    return s

if __name__ == '__main__':
    r = 5
    
    upper = (r + 1) * 9 ** r
    total_sum = sum(i for i in range(2, upper) if i == dp5sum(i))
    
    print(total_sum)
