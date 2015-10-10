"""
   We shall say that an n-digit number is pandigital if it makes use of all
   the digits 1 to n exactly once; for example, the 5-digit number, 15234, is
   1 through 5 pandigital.

   The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
   multiplicand, multiplier, and product is 1 through 9 pandigital.

   Find the sum of all products whose multiplicand/multiplier/product
   identity can be written as a 1 through 9 pandigital.

   HINT: Some products can be obtained in more than one way so be sure to
   only include it once in your sum.
"""

def is_pandigital(a, b):
    """Return true if 1 to 9 occurs exactly once in a, b and a * b"""
    text = ''.join((str(a), str(b), str(a * b)))
    return ''.join(sorted(text)) == '123456789'

if __name__ == '__main__':

    products = set()
    for i in range(2, 80):
        start = 1234 if i < 10 else 123
        for j in range(start, 10000 // i):
            if is_pandigital(i, j):
                products.add(i * j) 

    print(sum(products))

"""
NOTE:
Since the product has to be 9 digits long, possible combinations are:
    1-digit times 4-digit = 5-digit product
    2-digit times 3-digit = 5-digit product
"""
