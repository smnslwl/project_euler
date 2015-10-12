"""
   The number, 1406357289, is a 0 to 9 pandigital number because it is made
   up of each of the digits 0 to 9 in some order, but it also has a rather
   interesting sub-string divisibility property.

   Let d[1] be the 1^st digit, d[2] be the 2^nd digit, and so on. In this
   way, we note the following:

     • d[2]d[3]d[4]=406 is divisible by 2
     • d[3]d[4]d[5]=063 is divisible by 3
     • d[4]d[5]d[6]=635 is divisible by 5
     • d[5]d[6]d[7]=357 is divisible by 7
     • d[6]d[7]d[8]=572 is divisible by 11
     • d[7]d[8]d[9]=728 is divisible by 13
     • d[8]d[9]d[10]=289 is divisible by 17

   Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from itertools import permutations

def to_num(numbers):
    """Return a number made from an iterable of digits"""
    n = 0
    for i, num in enumerate(numbers):
        n += 10 ** (len(numbers) - i - 1) * num
    return n

def has_ss_divisible(digits):
    """Return true if digits display substring divisibility property"""
    divisors = 2, 3, 5, 7, 11, 13, 17
    if digits[0] == 0:
        return False
    for i, d in zip(range(1, 9), divisors):
        substr = to_num((digits[i], digits[i + 1], digits[i + 2]))
        if substr % d:
            return False
    return True

if __name__ == '__main__':
    n = 10
    
    perms = (p for p in permutations(range(n), n))
    sum_pands = sum(to_num(p) for p in perms if has_ss_divisible(p))
    
    print(sum_pands)
