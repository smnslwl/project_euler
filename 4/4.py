"""
   A palindromic number reads the same both ways. The largest palindrome made
   from the product of two 2-digit numbers is 9009 = 91 × 99.

   Find the largest palindrome made from the product of two 3-digit numbers.
"""

from itertools import combinations_with_replacement

def is_palindrome_number(n):
    """Returns true if n is a palindrome number"""
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    digits = 3
    lower = 10 ** (digits - 1)
    upper = 10 ** digits - 1

    largest_palindrome = 0
    for a, b in combinations_with_replacement(range(lower, upper + 1), 2):
        x = a * b
        if is_palindrome_number(x) and x > largest_palindrome:
            largest_palindrome = x

    print(largest_palindrome)
