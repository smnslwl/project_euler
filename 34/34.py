"""
   145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

   Find the sum of all numbers which are equal to the sum of the factorial of
   their digits.

   Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial

FACTS = [factorial(i) for i in range(10)]

def is_curious(n):
    """Return true if n equals the sum of the factorial of its digits"""
    return sum(map(lambda x: FACTS[int(x)], str(n))) == n
    
if __name__ == '__main__':

    upper = FACTS[9]
    curious_sum = sum(i for i in range(3, upper) if is_curious(i))

    print(curious_sum)

"""
NOTE:
Only two numbers are "curious", 145 and 40585.
The upper bound should be 9! * 8.
"""
