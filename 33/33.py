"""
   The fraction 49/98 is a curious fraction, as an inexperienced
   mathematician in attempting to simplify it may incorrectly believe that
   49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

   We shall consider fractions like, 30/50 = 3/5, to be trivial
   examples.

   There are exactly four non-trivial examples of this type of fraction, less
   than one in value, and containing two digits in the numerator and
   denominator.

   If the product of these four fractions is given in its lowest common
   terms, find the value of the denominator.
"""

from fractions import gcd

def is_curious_frac(a, b):
    """Return true if the value of a / b stays the same after 
    removing the common digits from a and b"""
    r = a / b
    
    a_set, b_set = [0] * 10, [0] * 10
    while a:
        a_set[a % 10] += 1
        a //= 10
    while b:
        b_set[b % 10] += 1
        b //= 10

    common = 0
    for i in range(10):
        if a_set[i] and a_set[i] == b_set[i]:
            a_set[i] -= 1
            b_set[i] -= 1
            common += 1
    
    if common == 1:
        a_new = sum(i for i in range(len(a_set)) if a_set[i])
        b_new = sum(i for i in range(len(b_set)) if b_set[i])
        if a_new / b_new == r:
            return True
    return False

if __name__ == '__main__':
    digits = 2

    lower = 10 ** (digits - 1)
    upper = 10 ** digits - 1
    prod_num, prod_den = 1, 1
    for num in range(lower, upper + 1):
        for den in range(num + 1, upper + 1):
            if not den % 10 or num == den:
                continue 
            if is_curious_frac(num, den):
                prod_num *= num
                prod_den *= den
    den_lowest_value = prod_den // gcd(prod_num, prod_den)
    
    print(den_lowest_value)
