"""
   The sequence of triangle numbers is generated by adding the natural
   numbers. So the 7^th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 =
   28. The first ten terms would be:

                    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

   Let us list the factors of the first seven triangle numbers:

      1: 1
      3: 1,3
      6: 1,2,3,6
     10: 1,2,5,10
     15: 1,3,5,15
     21: 1,3,7,21
     28: 1,2,4,7,14,28

   We can see that 28 is the first triangle number to have over five
   divisors.

   What is the value of the first triangle number to have over five hundred
   divisors?
"""

from math import sqrt

def num_of_divisors(n):
    """Return the number of divisors of n"""
    divisors = {1, n}
    for divisor in range(1, int(sqrt(n)) + 1):
        if not n % divisor:
            divisors.update((divisor, n // divisor))
    return len(divisors)

if __name__ == '__main__':
    n = 500
        
    i, triangle = 1, 1
    while num_of_divisors(triangle) < 500:
        i += 1
        triangle += i

    print(triangle)
    
"""
NOTE:
Each triangle number can be expressed as n * (n + 1) / 2.

"""
