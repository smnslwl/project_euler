"""
   The sum of the squares of the first ten natural numbers is,

                          1^2 + 2^2 + ... + 10^2 = 385

   The square of the sum of the first ten natural numbers is,

                       (1 + 2 + ... + 10)^2 = 55^2 = 3025

   Hence the difference between the sum of the squares of the first ten
   natural numbers and the square of the sum is 3025 − 385 = 2640.

   Find the difference between the sum of the squares of the first one
   hundred natural numbers and the square of the sum.
"""

if __name__ == '__main__':
    upper = 100

    sum_of_numbers, sum_of_squares = 0, 0
    for i in range(upper + 1):
        sum_of_numbers += i
        sum_of_squares += i ** 2
    difference = sum_of_numbers ** 2 - sum_of_squares
    
    print(difference)
