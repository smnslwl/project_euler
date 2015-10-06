"""
   If we list all the natural numbers below 10 that are multiples of 3 or 5,
   we get 3, 5, 6 and 9. The sum of these multiples is 23.

   Find the sum of all the multiples of 3 or 5 below 1000.
"""

if __name__ == '__main__':
    upper = 1000
    divisors = 3, 5

    sum_of_multiples = 0
    for i in range(upper):
        if not all(i % x for x in divisors):
            sum_of_multiples += i

    print(sum_of_multiples)
