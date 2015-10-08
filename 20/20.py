"""
   n! means n × (n − 1) × ... × 3 × 2 × 1

   For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
   and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 =
   27.

   Find the sum of the digits in the number 100!
"""

from math import factorial

if __name__ == '__main__':
    n = 100
    number = factorial(n)
    
    digits = []
    while number:
        digits.append(number % 10)
        number //= 10
    sum_of_digits = sum(digits)

    print(sum_of_digits)
    
"""
ONE-LINER (sort of)

    from math import factorial
    print(sum(int(x) for x in str(factorial(100))))

"""    
    
