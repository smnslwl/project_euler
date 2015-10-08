"""
   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

   Find the sum of all the primes below two million.
"""

from math import sqrt

if __name__ == '__main__':
    upper = 2000000

    sum_of_primes = 2
    for number in range(3, upper, 2):
        for divisor in range(3, int(sqrt(number)) + 1, 2):
            if not number % divisor:
                break
        else:
            sum_of_primes += number

    print(sum_of_primes)
