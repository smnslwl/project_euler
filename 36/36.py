"""
   The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
   bases.

   Find the sum of all numbers, less than one million, which are palindromic
   in base 10 and base 2.

   (Please note that the palindromic number, in either base, may not include
   leading zeros.)
"""

def binary(n):
    """Returns the binary equivalent of n"""
    return int(bin(n)[2:])

def is_palindrome(n):
    """Returns true if n is a palindrome"""
    return str(n) == str(n)[::-1].lstrip('0')

def is_dual_palindrome(n):
    """Returns true if n is palindromic in both decimal and binary"""
    return is_palindrome(n) and is_palindrome(binary(n))

if __name__ == '__main__':
    upper = 1000000
    
    total = sum(i for i in range(upper) if is_dual_palindrome(i))
    
    print(total)
